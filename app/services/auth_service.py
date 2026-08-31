from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional
from flask import current_app
from app.repositories.user_repository import UserRepository
from app.repositories.audit_repository import AuditRepository
from app.models.user import User, UserSession
from app.utils.crypto import hash_password, verify_password, generate_jwt_token, calculate_sha256
from app.errors.exceptions import AuthenticationError, ConflictError, NotFoundError, ValidationError
from app.constants import UserRole, AuditAction

class AuthService:
    def __init__(self, user_repo: UserRepository = None, audit_repo: AuditRepository = None):
        self.user_repo = user_repo or UserRepository()
        self.audit_repo = audit_repo or AuditRepository()

    def authenticate(self, identifier: str, password: str, ip_address: str = None, user_agent: str = None) -> Dict[str, Any]:
        user = self.user_repo.get_by_username_or_email(identifier)
        if not user or not user.is_active or user.is_deleted:
            self.audit_repo.log_event(
                action=AuditAction.USER_LOGIN_FAILED,
                resource_type='User',
                username=identifier,
                ip_address=ip_address,
                user_agent=user_agent,
                status='FAILURE',
                details={'reason': 'User not found or inactive'}
            )
            raise AuthenticationError('Invalid username/email or password.')

        if user.locked_until and user.locked_until > datetime.now(timezone.utc):
            raise AuthenticationError('Account is temporarily locked due to excessive failed attempts. Please try again later.')

        if not verify_password(password, user.password_hash):
            user.failed_login_attempts += 1
            if user.failed_login_attempts >= 5:
                user.locked_until = datetime.now(timezone.utc) + timedelta(minutes=15)
            self.user_repo.update(user, {'failed_login_attempts': user.failed_login_attempts, 'locked_until': user.locked_until})
            self.audit_repo.log_event(
                action=AuditAction.USER_LOGIN_FAILED,
                resource_type='User',
                username=user.username,
                user_id=user.id,
                ip_address=ip_address,
                user_agent=user_agent,
                status='FAILURE',
                details={'reason': 'Password mismatch', 'failed_attempts': user.failed_login_attempts}
            )
            raise AuthenticationError('Invalid username/email or password.')

        user.failed_login_attempts = 0
        user.locked_until = None
        user.last_login_at = datetime.now(timezone.utc)
        user.last_login_ip = ip_address
        self.user_repo.update(user, {
            'failed_login_attempts': 0,
            'locked_until': None,
            'last_login_at': user.last_login_at,
            'last_login_ip': ip_address
        })

        access_token = generate_jwt_token(user.id, user.email, user.primary_role, expires_in_seconds=3600)
        refresh_token = generate_jwt_token(user.id, user.email, user.primary_role, expires_in_seconds=86400*30, token_type='refresh')

        session_hash = calculate_sha256(access_token)
        session = UserSession(
            user_id=user.id,
            session_token_hash=session_hash,
            ip_address=ip_address,
            user_agent=user_agent,
            expires_at=datetime.now(timezone.utc) + timedelta(hours=1)
        )
        self.user_repo.create(session)

        self.audit_repo.log_event(
            action=AuditAction.USER_LOGIN,
            resource_type='User',
            username=user.username,
            user_id=user.id,
            ip_address=ip_address,
            user_agent=user_agent,
            status='SUCCESS',
            details={'primary_role': user.primary_role}
        )

        return {
            'user': user.to_dict(),
            'access_token': access_token,
            'refresh_token': refresh_token,
            'token_type': 'Bearer',
            'expires_in': 3600
        }

    def register(self, username: str, email: str, password: str, full_name: str, role_name: str = 'security_analyst', creator_id: str = None) -> User:
        if self.user_repo.get_by_username(username):
            raise ConflictError(f'Username "{username}" is already registered.')
        if self.user_repo.get_by_email(email):
            raise ConflictError(f'Email "{email}" is already registered.')

        role = self.user_repo.get_role_by_name(role_name) or self.user_repo.get_role_by_name(UserRole.SECURITY_ANALYST.value)
        if not role:
            role = self.user_repo.list_roles()[0] if self.user_repo.list_roles() else None

        user = User(
            username=username,
            email=email.lower(),
            password_hash=hash_password(password),
            full_name=full_name
        )
        if role:
            user.roles.append(role)

        created_user = self.user_repo.create(user)
        self.audit_repo.log_event(
            action='user_registered',
            resource_type='User',
            username=username,
            user_id=creator_id,
            resource_id=created_user.id,
            status='SUCCESS',
            details={'role': role.name if role else 'none'}
        )
        return created_user

    def change_password(self, user_id: str, current_password: str, new_password: str):
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise NotFoundError('User not found.')
        if not verify_password(current_password, user.password_hash):
            raise AuthenticationError('Current password is incorrect.')
        
        user.password_hash = hash_password(new_password)
        self.user_repo.update(user, {'password_hash': user.password_hash})
        self.user_repo.revoke_all_user_sessions(user_id)
        self.audit_repo.log_event(
            action=AuditAction.PASSWORD_CHANGE,
            resource_type='User',
            username=user.username,
            user_id=user.id,
            status='SUCCESS'
        )
        return True
