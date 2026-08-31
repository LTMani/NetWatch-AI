import sys
sys.path.insert(0, '.')
from scripts.writer import write

# Schemas
schemas_code = """from typing import Dict, Any, Optional
from app.errors.exceptions import ValidationError
from app.utils.validators import validate_email, validate_username

class LoginRequestSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, str]:
        if not isinstance(data, dict):
            raise ValidationError('Invalid JSON body.')
        identifier = data.get('identifier') or data.get('username') or data.get('email')
        password = data.get('password')
        if not identifier or not str(identifier).strip():
            raise ValidationError('Username or email is required.')
        if not password or not str(password).strip():
            raise ValidationError('Password is required.')
        return {
            'identifier': str(identifier).strip(),
            'password': str(password).strip(),
            'remember_me': bool(data.get('remember_me', False))
        }

class RegisterRequestSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValidationError('Invalid JSON body.')
        username = validate_username(data.get('username', ''))
        email = validate_email(data.get('email', ''))
        password = data.get('password', '')
        full_name = data.get('full_name', '').strip()
        if not password or len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        if not full_name:
            raise ValidationError('Full name is required.')
        return {
            'username': username,
            'email': email,
            'password': password,
            'full_name': full_name,
            'role': data.get('role', 'security_analyst')
        }

class PasswordChangeSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, str]:
        current_password = data.get('current_password', '')
        new_password = data.get('new_password', '')
        if not current_password:
            raise ValidationError('Current password is required.')
        if not new_password or len(new_password) < 8:
            raise ValidationError('New password must be at least 8 characters long.')
        return {
            'current_password': current_password,
            'new_password': new_password
        }
"""
write('app/schemas/auth_schemas.py', schemas_code)
write('app/schemas/__init__.py', 'from app.schemas.auth_schemas import LoginRequestSchema, RegisterRequestSchema, PasswordChangeSchema\n')

# Services
auth_service = """from datetime import datetime, timezone, timedelta
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
"""
write('app/services/auth_service.py', auth_service)

audit_service = """from typing import Dict, Any, List
from app.repositories.audit_repository import AuditRepository

class AuditService:
    def __init__(self, audit_repo: AuditRepository = None):
        self.audit_repo = audit_repo or AuditRepository()

    def get_logs(self, action: str = None, username: str = None, status: str = None, page: int = 1, per_page: int = 25):
        return self.audit_repo.list_logs(action=action, username=username, status=status, page=page, per_page=per_page)

    def verify_chain_integrity(self) -> Dict[str, Any]:
        return self.audit_repo.verify_integrity()
"""
write('app/services/audit_service.py', audit_service)

notif_service = """from typing import List, Optional
from app.models.notification import SystemNotification, WebhookEndpoint
from app.models.base import db

class NotificationService:
    def get_notifications_for_user(self, user_id: Optional[str] = None, unread_only: bool = False, limit: int = 20) -> List[SystemNotification]:
        query = SystemNotification.query.filter(
            (SystemNotification.user_id == user_id) | (SystemNotification.user_id == None),
            SystemNotification.is_deleted == False
        )
        if unread_only:
            query = query.filter_by(is_read=False)
        return query.order_by(SystemNotification.created_at.desc()).limit(limit).all()

    def create_notification(self, title: str, message: str, category: str = 'ALERT', severity: str = 'INFO', user_id: str = None, action_url: str = None) -> SystemNotification:
        notif = SystemNotification(
            title=title,
            message=message,
            category=category,
            severity=severity,
            user_id=user_id,
            action_url=action_url
        )
        db.session.add(notif)
        db.session.commit()
        return notif

    def mark_as_read(self, notification_id: str):
        notif = SystemNotification.query.get(notification_id)
        if notif:
            notif.is_read = True
            db.session.commit()
            return True
        return False
"""
write('app/services/notification_service.py', notif_service)
write('app/services/__init__.py', '''from app.services.auth_service import AuthService
from app.services.audit_service import AuditService
from app.services.notification_service import NotificationService
''')

# Middleware
auth_mid = """from functools import wraps
from flask import request, g, jsonify, session
from app.utils.crypto import decode_jwt_token
from app.repositories.user_repository import UserRepository
from app.errors.exceptions import AuthenticationError, AuthorizationError

def get_current_user():
    if hasattr(g, 'current_user') and g.current_user:
        return g.current_user

    # 1. Check Session Cookie (for web browser views)
    user_id = session.get('user_id')
    if user_id:
        user = UserRepository().get_by_id(user_id)
        if user and user.is_active:
            g.current_user = user
            return user

    # 2. Check Authorization Header (for REST API calls)
    auth_header = request.headers.get('Authorization', '')
    if auth_header.startswith('Bearer '):
        token = auth_header.split(' ', 1)[1].strip()
        try:
            payload = decode_jwt_token(token)
            user = UserRepository().get_by_id(payload.get('sub'))
            if user and user.is_active:
                g.current_user = user
                return user
        except Exception:
            pass

    return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = get_current_user()
        if not user:
            raise AuthenticationError('Authentication required.')
        return f(*args, **kwargs)
    return decorated_function

def roles_required(*required_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = get_current_user()
            if not user:
                raise AuthenticationError('Authentication required.')
            user_roles = [r.name for r in user.roles]
            # Super admin bypasses all role checks
            if 'super_admin' in user_roles:
                return f(*args, **kwargs)
            if not any(r in user_roles for r in required_roles):
                raise AuthorizationError(f'Access requires one of the following roles: {", ".join(required_roles)}')
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def permissions_required(*required_perms):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = get_current_user()
            if not user:
                raise AuthenticationError('Authentication required.')
            if user.has_role('super_admin'):
                return f(*args, **kwargs)
            for perm in required_perms:
                if not user.has_permission(perm):
                    raise AuthorizationError(f'Missing required permission: {perm}')
            return f(*args, **kwargs)
        return decorated_function
    return decorator
"""
write('app/middleware/auth_middleware.py', auth_mid)

rate_mid = """import time
from collections import defaultdict
from functools import wraps
from flask import request
from app.errors.exceptions import RateLimitExceededError

_request_history = defaultdict(list)

def rate_limit(max_requests: int = 60, window_seconds: int = 60):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ip = request.remote_addr or '127.0.0.1'
            now = time.time()
            # Clean expired timestamps
            _request_history[ip] = [ts for ts in _request_history[ip] if now - ts < window_seconds]
            if len(_request_history[ip]) >= max_requests:
                raise RateLimitExceededError(f'Rate limit of {max_requests} requests per {window_seconds}s exceeded.')
            _request_history[ip].append(now)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
"""
write('app/middleware/rate_limiter.py', rate_mid)

sec_headers = """def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=()'
    return response
"""
write('app/middleware/security_headers.py', sec_headers)
write('app/middleware/__init__.py', '''from app.middleware.auth_middleware import login_required, roles_required, permissions_required, get_current_user
from app.middleware.rate_limiter import rate_limit
from app.middleware.security_headers import add_security_headers
''')

# Routes
auth_api = """from flask import Blueprint, request, jsonify, session
from app.services.auth_service import AuthService
from app.schemas.auth_schemas import LoginRequestSchema, RegisterRequestSchema, PasswordChangeSchema
from app.middleware.auth_middleware import login_required, get_current_user
from app.middleware.rate_limiter import rate_limit

auth_api_bp = Blueprint('auth_api', __name__, url_prefix='/api/v1/auth')
auth_service = AuthService()

@auth_api_bp.route('/login', methods=['POST'])
@rate_limit(max_requests=15, window_seconds=60)
def login():
    data = LoginRequestSchema.validate(request.get_json() or {})
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    result = auth_service.authenticate(data['identifier'], data['password'], ip_address=ip, user_agent=ua)
    
    session['user_id'] = result['user']['id']
    session['username'] = result['user']['username']
    session['role'] = result['user']['primary_role']
    if data['remember_me']:
        session.permanent = True

    return jsonify({
        'status': 'success',
        'message': 'Authentication successful.',
        'data': result
    }), 200

@auth_api_bp.route('/register', methods=['POST'])
@rate_limit(max_requests=10, window_seconds=60)
def register():
    data = RegisterRequestSchema.validate(request.get_json() or {})
    current_user = get_current_user()
    creator_id = current_user.id if current_user else None
    user = auth_service.register(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        full_name=data['full_name'],
        role_name=data['role'],
        creator_id=creator_id
    )
    return jsonify({
        'status': 'success',
        'message': 'User registered successfully.',
        'data': user.to_dict()
    }), 201

@auth_api_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({
        'status': 'success',
        'message': 'Logged out successfully.'
    }), 200

@auth_api_bp.route('/me', methods=['GET'])
@login_required
def get_me():
    user = get_current_user()
    return jsonify({
        'status': 'success',
        'data': user.to_dict()
    }), 200

@auth_api_bp.route('/change-password', methods=['POST'])
@login_required
def change_password():
    user = get_current_user()
    data = PasswordChangeSchema.validate(request.get_json() or {})
    auth_service.change_password(user.id, data['current_password'], data['new_password'])
    session.clear()
    return jsonify({
        'status': 'success',
        'message': 'Password updated successfully. Please log in again.'
    }), 200
"""
write('app/routes/auth_api.py', auth_api)

users_api = """from flask import Blueprint, request, jsonify
from app.repositories.user_repository import UserRepository
from app.middleware.auth_middleware import login_required, roles_required, get_current_user
from app.errors.exceptions import NotFoundError, ValidationError

users_api_bp = Blueprint('users_api', __name__, url_prefix='/api/v1/users')
user_repo = UserRepository()

@users_api_bp.route('', methods=['GET'])
@login_required
@roles_required('super_admin', 'network_admin', 'security_analyst')
def list_users():
    search = request.args.get('search')
    role = request.args.get('role')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    result = user_repo.list_users(search=search, role=role, page=page, per_page=per_page)
    return jsonify({
        'status': 'success',
        'data': {
            'items': [u.to_dict() for u in result['items']],
            'total': result['total'],
            'page': result['page'],
            'pages': result['pages']
        }
    }), 200

@users_api_bp.route('/<user_id>', methods=['GET'])
@login_required
def get_user(user_id):
    user = user_repo.get_by_id(user_id)
    if not user:
        raise NotFoundError('User not found.')
    return jsonify({'status': 'success', 'data': user.to_dict()}), 200

@users_api_bp.route('/<user_id>/status', methods=['PATCH'])
@login_required
@roles_required('super_admin')
def toggle_user_status(user_id):
    user = user_repo.get_by_id(user_id)
    if not user:
        raise NotFoundError('User not found.')
    data = request.get_json() or {}
    is_active = data.get('is_active', not user.is_active)
    user_repo.update(user, {'is_active': is_active})
    return jsonify({'status': 'success', 'message': 'User status updated.', 'data': user.to_dict()}), 200

@users_api_bp.route('/roles', methods=['GET'])
@login_required
def list_roles():
    roles = user_repo.list_roles()
    return jsonify({'status': 'success', 'data': [r.to_dict() for r in roles]}), 200
"""
write('app/routes/users_api.py', users_api)

audit_api = """from flask import Blueprint, request, jsonify
from app.services.audit_service import AuditService
from app.middleware.auth_middleware import login_required, roles_required
from app.utils.exporters import export_to_csv_response

audit_api_bp = Blueprint('audit_api', __name__, url_prefix='/api/v1/audit-logs')
audit_service = AuditService()

@audit_api_bp.route('', methods=['GET'])
@login_required
@roles_required('super_admin', 'security_analyst', 'auditor')
def list_audit_logs():
    action = request.args.get('action')
    username = request.args.get('username')
    status = request.args.get('status')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 25))
    result = audit_service.get_logs(action=action, username=username, status=status, page=page, per_page=per_page)
    return jsonify({
        'status': 'success',
        'data': {
            'items': [log.to_dict() for log in result['items']],
            'total': result['total'],
            'page': result['page'],
            'pages': result['pages']
        }
    }), 200

@audit_api_bp.route('/verify-integrity', methods=['GET'])
@login_required
@roles_required('super_admin', 'auditor')
def verify_audit_integrity():
    result = audit_service.verify_chain_integrity()
    return jsonify({
        'status': 'success',
        'message': 'Cryptographic chain verification complete.',
        'data': result
    }), 200

@audit_api_bp.route('/export', methods=['GET'])
@login_required
@roles_required('super_admin', 'auditor')
def export_audit_logs():
    result = audit_service.get_logs(page=1, per_page=1000)
    rows = [l.to_dict() for l in result['items']]
    fields = ['id', 'created_at', 'username', 'action', 'resource_type', 'resource_id', 'status', 'ip_address', 'current_block_hash']
    return export_to_csv_response(rows, fields, filename='audit_log_export.csv')
"""
write('app/routes/audit_api.py', audit_api)

print('M1 Services, Middleware and APIs successfully generated.')
