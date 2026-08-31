from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db
from app.constants import PolicyAction, AlertSeverity

class NetworkPolicy(BaseModel):
    """Configurable enterprise network traffic policy."""
    __tablename__ = 'nw_policies'

    name = Column(String(128), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    category = Column(String(64), default='BANDWIDTH', nullable=False, index=True) # BANDWIDTH, DOMAIN, TIME, SECURITY
    severity = Column(String(16), default=AlertSeverity.HIGH.value, nullable=False)
    action = Column(String(32), default=PolicyAction.CREATE_INCIDENT.value, nullable=False)
    
    is_enabled = Column(Boolean, default=True, nullable=False, index=True)
    condition_json = Column(Text, nullable=False) # e.g. {'metric': 'bytes_out', 'operator': '>', 'threshold': 524288000, 'window_seconds': 300}
    created_by = Column(String(64), default='admin', nullable=False)
    violation_count = Column(Integer, default=0, nullable=False)
    last_triggered_at = Column(DateTime, nullable=True)

    violations = relationship('PolicyViolationEvent', back_populates='policy', cascade='all, delete-orphan')

class PolicyViolationEvent(BaseModel):
    """Audit event recorded when network traffic breaches a policy."""
    __tablename__ = 'nw_policy_violations'

    policy_id = Column(String(36), ForeignKey('nw_policies.id', ondelete='CASCADE'), nullable=False, index=True)
    device_id = Column(String(36), ForeignKey('nw_devices.id'), nullable=True, index=True)
    severity = Column(String(16), nullable=False)
    violation_details = Column(Text, nullable=False)
    observed_value = Column(String(64), nullable=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    policy = relationship('NetworkPolicy', back_populates='violations')
    device = relationship('Device')
