from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class AuditLog(BaseModel):
    __tablename__ = 'nw_audit_logs'

    user_id = Column(String(36), ForeignKey('nw_users.id'), nullable=True, index=True)
    username = Column(String(64), nullable=False, index=True)
    action = Column(String(64), nullable=False, index=True)
    resource_type = Column(String(64), nullable=False, index=True)
    resource_id = Column(String(64), nullable=True, index=True)
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(String(256), nullable=True)
    status = Column(String(16), default='SUCCESS', nullable=False)
    
    details_json = Column(Text, nullable=True)
    previous_block_hash = Column(String(64), nullable=True)
    current_block_hash = Column(String(64), nullable=False, index=True)

    user = relationship('User')

class SecurityEvent(BaseModel):
    __tablename__ = 'nw_security_events'

    event_type = Column(String(64), nullable=False, index=True)
    severity = Column(String(16), default='MEDIUM', nullable=False, index=True)
    source_ip = Column(String(45), nullable=True, index=True)
    target_username = Column(String(64), nullable=True, index=True)
    description = Column(Text, nullable=False)
    is_mitigated = Column(Boolean, default=False, nullable=False)
    mitigation_notes = Column(Text, nullable=True)
