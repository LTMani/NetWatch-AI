# -*- coding: utf-8 -*-
"
NetWatch AI - Models Builder (Part 1: Base, User, Organization, Audit, Notification)
"
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def write_file(rel_path, content):
    full_path = BASE_DIR / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, w, encoding=utf-8) as f:
        f.write(content.strip() + \n)
    print(f [+] Created {rel_path} ({len(content.splitlines())} lines))

# Base Model
write_file(app/models/base.py, '''"
NetWatch AI - Base ORM Entity and Mixins.
Provides UUID primary keys, timestamp tracking, soft-deletion, and robust dictionary serialization.
"
import uuid
from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def generate_uuid() -> str:
    "Generates standard UUID4 string for entity primary keys."
    return str(uuid.uuid4())

class BaseModel(db.Model):
    "Abstract base model with standard enterprise metadata fields."
    __abstract__ = True

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False, index=True)

    def to_dict(self, exclude=None):
        "Serializes model attributes to a JSON-friendly dictionary."
        exclude = set(exclude or [])
        result = {}
        for column in self.__table__.columns:
            if column.name in exclude:
                continue
            val = getattr(self, column.name)
            if isinstance(val, datetime):
                result[column.name] = val.replace(tzinfo=timezone.utc).isoformat()
            else:
                result[column.name] = val
        return result

    def update_from_dict(self, data, allowed_fields=None):
        "Safely updates model fields from input dictionary."
        allowed = set(allowed_fields) if allowed_fields else {c.name for c in self.__table__.columns if c.name not in ('id', 'created_at')}
        for key, value in data.items():
            if key in allowed and hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now(timezone.utc)
''')

# User Models
write_file(app/models/user.py, '''"
NetWatch AI - Identity, Authentication & Role-Based Access Control Entities.
"
from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db, generate_uuid
from app.constants import UserRole

# Association Table for User <-> Role (Many to Many)
user_roles = Table(
    'nw_user_roles',
    db.metadata,
    Column('user_id', String(36), ForeignKey('nw_users.id', ondelete='CASCADE'), primary_key=True),
    Column('role_id', String(36), ForeignKey('nw_roles.id', ondelete='CASCADE'), primary_key=True)
)

# Association Table for Role <-> Permission (Many to Many)
role_permissions = Table(
    'nw_role_permissions',
    db.metadata,
    Column('role_id', String(36), ForeignKey('nw_roles.id', ondelete='CASCADE'), primary_key=True),
    Column('permission_id', String(36), ForeignKey('nw_permissions.id', ondelete='CASCADE'), primary_key=True)
)

class User(BaseModel):
    "Enterprise authorized administrative user account."
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
    
    # Relationships
    roles = relationship('Role', secondary=user_roles, back_populates='users', lazy='joined')
    sessions = relationship('UserSession', back_populates='user', cascade='all, delete-orphan')
    api_keys = relationship('ApiKey', back_populates='user', cascade='all, delete-orphan')
    organization = relationship('Organization', back_populates='users')
    department = relationship('Department', back_populates='users')

    @property
    def primary_role(self) -> str:
        "Returns highest privileged role name for the user."
        role_priority = [UserRole.SUPER_ADMIN, UserRole.NETWORK_ADMIN, UserRole.SECURITY_ANALYST, UserRole.AUDITOR]
        user_role_names = [r.name for r in self.roles]
        for r in role_priority:
            if r.value in user_role_names:
                return r.value
        return user_role_names[0] if user_role_names else UserRole.AUDITOR.value

    def has_role(self, role_name: str) -> bool:
        "Checks if user possesses a specific role."
        return any(r.name == role_name for r in self.roles)

    def has_permission(self, permission_slug: str) -> bool:
        "Checks if any of the user's assigned roles grant the requested permission."
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
    "Enterprise security role definition."
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
    "Granular operational security permission."
    __tablename__ = 'nw_permissions'

    name = Column(String(128), nullable=False)
    slug = Column(String(64), unique=True, nullable=False, index=True)
    category = Column(String(64), nullable=False, index=True)
    description = Column(String(256), nullable=True)

    roles = relationship('Role', secondary=role_permissions, back_populates='permissions')

class UserSession(BaseModel):
    "Tracks active authenticated user sessions for security validation and revocation."
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
    "Telemetry collector and integration API credentials."
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
''')

# Organization Models
write_file(app/models/organization.py, '''"
NetWatch AI - Enterprise Organization, Subnet & Network Site Topology Entities.
"
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class Organization(BaseModel):
    "Top-level enterprise tenant or company organization."
    __tablename__ = 'nw_organizations'

    name = Column(String(128), unique=True, nullable=False, index=True)
    domain = Column(String(128), nullable=True)
    office_start_time = Column(String(5), default='09:00', nullable=False)
    office_end_time = Column(String(5), default='18:00', nullable=False)
    work_days = Column(String(32), default='0,1,2,3,4', nullable=False) # Mon-Fri
    timezone = Column(String(64), default='UTC', nullable=False)
    retention_days = Column(Integer, default=90, nullable=False)

    departments = relationship('Department', back_populates='organization', cascade='all, delete-orphan')
    sites = relationship('NetworkSite', back_populates='organization', cascade='all, delete-orphan')
    users = relationship('User', back_populates='organization')
    devices = relationship('Device', back_populates='organization')

class Department(BaseModel):
    "Organizational business unit or division (e.g., Engineering, Finance)."
    __tablename__ = 'nw_departments'

    organization_id = Column(String(36), ForeignKey('nw_organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = Column(String(128), nullable=False, index=True)
    code = Column(String(32), nullable=True)
    manager_name = Column(String(128), nullable=True)
    manager_email = Column(String(128), nullable=True)
    risk_threshold = Column(Integer, default=70, nullable=False)

    organization = relationship('Organization', back_populates='departments')
    users = relationship('User', back_populates='department')
    subnets = relationship('Subnet', back_populates='department')
    devices = relationship('Device', back_populates='department')

class NetworkSite(BaseModel):
    "Physical office campus, datacenter, or branch location."
    __tablename__ = 'nw_network_sites'

    organization_id = Column(String(36), ForeignKey('nw_organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = Column(String(128), nullable=False, index=True)
    location_code = Column(String(32), nullable=False)
    city = Column(String(64), nullable=True)
    country = Column(String(64), nullable=True)
    primary_gateway_ip = Column(String(45), nullable=True)
    is_headquarters = Column(Boolean, default=False, nullable=False)

    organization = relationship('Organization', back_populates='sites')
    subnets = relationship('Subnet', back_populates='site')
    devices = relationship('Device', back_populates='site')

class Subnet(BaseModel):
    "Authorized enterprise CIDR network segment."
    __tablename__ = 'nw_subnets'

    site_id = Column(String(36), ForeignKey('nw_network_sites.id'), nullable=True, index=True)
    department_id = Column(String(36), ForeignKey('nw_departments.id'), nullable=True, index=True)
    name = Column(String(128), nullable=False)
    cidr = Column(String(45), unique=True, nullable=False, index=True)
    network_address = Column(String(45), nullable=False)
    netmask = Column(String(45), nullable=False)
    gateway_ip = Column(String(45), nullable=True)
    vlan_id = Column(Integer, nullable=True, index=True)
    is_guest_network = Column(Boolean, default=False, nullable=False)
    is_dmz = Column(Boolean, default=False, nullable=False)
    description = Column(String(256), nullable=True)

    site = relationship('NetworkSite', back_populates='subnets')
    department = relationship('Department', back_populates='subnets')
    devices = relationship('Device', back_populates='subnet')
''')

# Audit & Notification Models
write_file(app/models/audit.py, '''"
NetWatch AI - Immutable Cryptographic Audit Logs and Security Event Ledger.
"
from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class AuditLog(BaseModel):
    "
    Cryptographically chained enterprise audit log.
    Ensures zero tampering and records all administrative and security actions.
    "
    __tablename__ = 'nw_audit_logs'

    user_id = Column(String(36), ForeignKey('nw_users.id'), nullable=True, index=True)
    username = Column(String(64), nullable=False, index=True)
    action = Column(String(64), nullable=False, index=True)
    resource_type = Column(String(64), nullable=False, index=True)
    resource_id = Column(String(64), nullable=True, index=True)
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(String(256), nullable=True)
    status = Column(String(16), default='SUCCESS', nullable=False) # SUCCESS, FAILURE, DENIED
    
    details_json = Column(Text, nullable=True)
    previous_block_hash = Column(String(64), nullable=True)
    current_block_hash = Column(String(64), nullable=False, index=True)

    user = relationship('User')

class SecurityEvent(BaseModel):
    "High-priority security telemetry and authentication anomalies."
    __tablename__ = 'nw_security_events'

    event_type = Column(String(64), nullable=False, index=True)
    severity = Column(String(16), default='MEDIUM', nullable=False, index=True)
    source_ip = Column(String(45), nullable=True, index=True)
    target_username = Column(String(64), nullable=True, index=True)
    description = Column(Text, nullable=False)
    is_mitigated = Column(Boolean, default=False, nullable=False)
    mitigation_notes = Column(Text, nullable=True)
''')

write_file(app/models/notification.py, '''"
NetWatch AI - In-App Notification and Real-Time Dispatch System.
"
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class SystemNotification(BaseModel):
    "Real-time enterprise notification delivered to administrators."
    __tablename__ = 'nw_notifications'

    user_id = Column(String(36), ForeignKey('nw_users.id'), nullable=True, index=True) # None = Broadcast to all
    title = Column(String(128), nullable=False)
    message = Column(Text, nullable=False)
    category = Column(String(32), default='ALERT', nullable=False, index=True) # ALERT, INCIDENT, SYSTEM, POLICY
    severity = Column(String(16), default='INFO', nullable=False, index=True)
    is_read = Column(Boolean, default=False, nullable=False, index=True)
    action_url = Column(String(256), nullable=True)

    user = relationship('User')

class WebhookEndpoint(BaseModel):
    "External alerting webhooks (Slack, Microsoft Teams, PagerDuty, Syslog)."
    __tablename__ = 'nw_webhooks'

    name = Column(String(128), nullable=False)
    target_url = Column(String(512), nullable=False)
    event_filter = Column(String(256), default='alert.critical,incident.created')
    secret_token = Column(String(128), nullable=True)
    is_enabled = Column(Boolean, default=True, nullable=False, index=True)
    failure_count = Column(Integer, default=0, nullable=False)
''')

print(Milestone 1 Models (Base, User, Organization, Audit, Notification) written successfully.)
