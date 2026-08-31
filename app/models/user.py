from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db
from app.constants import UserRole

user_roles = Table(
    'nw_user_roles',
    db.metadata,
    Column('user_id', String(36), ForeignKey('nw_users.id', ondelete='CASCADE'), primary_key=True),
    Column('role_id', String(36), ForeignKey('nw_roles.id', ondelete='CASCADE'), primary_key=True)
)

role_permissions = Table(
    'nw_role_permissions',
    db.metadata,
    Column('role_id', String(36), ForeignKey('nw_roles.id', ondelete='CASCADE'), primary_key=True),
    Column('permission_id', String(36), ForeignKey('nw_permissions.id', ondelete='CASCADE'), primary_key=True)
)

class User(BaseModel):
    __tablename__ = 'nw_users'

    username = Column(String(64), unique=True, nullable=False, index=True)
    email = Column(String(128), unique=True, nullable=False, index=True)
    password_hash = Column(String(256), nullable=False)
    full_name = Column(String(128), nullable=False)
    organization_id = Column(String(36), ForeignKey('nw_organizations.id'), nullable=True, index=True)
    department_id = Column(String(36), ForeignKey('nw_departments.id'), nullable=True, index=True)
    
    is_active = Column(Boolean, default=True, nullable=False, index=True)
    is_mfa_enabled = Column(Boolean, default=False, nullable=False)
    mfa_secret = Column(String(64), nullable=True)
    
    last_login_at = Column(DateTime, nullable=True)
    last_login_ip = Column(String(45), nullable=True)
    failed_login_attempts = Column(Integer, default=0, nullable=False)
    locked_until = Column(DateTime, nullable=True)
    
    roles = relationship('Role', secondary=user_roles, back_populates='users', lazy='joined')
    sessions = relationship('UserSession', back_populates='user', cascade='all, delete-orphan')
    api_keys = relationship('ApiKey', back_populates='user', cascade='all, delete-orphan')
    organization = relationship('Organization', back_populates='users')
    department = relationship('Department', back_populates='users')

    @property
    def primary_role(self) -> str:
        role_priority = [UserRole.SUPER_ADMIN, UserRole.NETWORK_ADMIN, UserRole.SECURITY_ANALYST, UserRole.AUDITOR]
        user_role_names = [r.name for r in self.roles]
        for r in role_priority:
            if r.value in user_role_names:
                return r.value
        return user_role_names[0] if user_role_names else UserRole.AUDITOR.value

    def has_role(self, role_name: str) -> bool:
        return any(r.name == role_name for r in self.roles)

    def has_permission(self, permission_slug: str) -> bool:
        for role in self.roles:
            for perm in role.permissions:
                if perm.slug == permission_slug:
                    return True
        return False

    def to_dict(self, exclude=None):
        base_dict = super().to_dict(exclude={'password_hash', 'mfa_secret'}.union(exclude or set()))
        base_dict['roles'] = [r.name for r in self.roles]
        base_dict['primary_role'] = self.primary_role
        base_dict['organization_name'] = self.organization.name if self.organization else None
        base_dict['department_name'] = self.department.name if self.department else None
        return base_dict

class Role(BaseModel):
    __tablename__ = 'nw_roles'

    name = Column(String(64), unique=True, nullable=False, index=True)
    display_name = Column(String(128), nullable=False)
    description = Column(String(256), nullable=True)
    is_system_role = Column(Boolean, default=True, nullable=False)

    users = relationship('User', secondary=user_roles, back_populates='roles')
    permissions = relationship('Permission', secondary=role_permissions, back_populates='roles', lazy='joined')

    def to_dict(self, exclude=None):
        base_dict = super().to_dict(exclude=exclude)
        base_dict['permissions'] = [p.slug for p in self.permissions]
        return base_dict

class Permission(BaseModel):
    __tablename__ = 'nw_permissions'

    name = Column(String(128), nullable=False)
    slug = Column(String(64), unique=True, nullable=False, index=True)
    category = Column(String(64), nullable=False, index=True)
    description = Column(String(256), nullable=True)

    roles = relationship('Role', secondary=role_permissions, back_populates='permissions')

class UserSession(BaseModel):
    __tablename__ = 'nw_user_sessions'

    user_id = Column(String(36), ForeignKey('nw_users.id', ondelete='CASCADE'), nullable=False, index=True)
    session_token_hash = Column(String(64), unique=True, nullable=False, index=True)
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(String(256), nullable=True)
    expires_at = Column(DateTime, nullable=False, index=True)
    is_revoked = Column(Boolean, default=False, nullable=False, index=True)
    last_activity_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship('User', back_populates='sessions')

class ApiKey(BaseModel):
    __tablename__ = 'nw_api_keys'

    user_id = Column(String(36), ForeignKey('nw_users.id', ondelete='CASCADE'), nullable=False, index=True)
    key_name = Column(String(128), nullable=False)
    key_prefix = Column(String(16), nullable=False, index=True)
    key_hash = Column(String(64), unique=True, nullable=False, index=True)
    scopes = Column(String(256), default='telemetry:write,metrics:read')
    expires_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False, index=True)
    last_used_at = Column(DateTime, nullable=True)

    user = relationship('User', back_populates='api_keys')
