from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db
from app.constants import RiskLevel

class RiskScoreSnapshot(BaseModel):
    """Historical risk posture evaluation snapshot for devices or subnets."""
    __tablename__ = 'nw_risk_snapshots'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=True, index=True)
    subnet_id = Column(String(36), ForeignKey('nw_subnets.id'), nullable=True, index=True)
    
    risk_score = Column(Float, default=0.0, nullable=False, index=True) # 0.0 to 100.0
    risk_level = Column(String(16), default=RiskLevel.NEGLIGIBLE.value, nullable=False, index=True)
    
    policy_penalty = Column(Float, default=0.0, nullable=False)
    anomaly_penalty = Column(Float, default=0.0, nullable=False)
    reputation_penalty = Column(Float, default=0.0, nullable=False)
    vulnerability_penalty = Column(Float, default=0.0, nullable=False)
    
    primary_risk_driver = Column(String(256), nullable=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

class RiskFactor(BaseModel):
    """Granular contributor attributing points to an asset's overall risk score."""
    __tablename__ = 'nw_risk_factors'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=False, index=True)
    factor_name = Column(String(128), nullable=False)
    category = Column(String(32), default='POLICY', nullable=False) # POLICY, ANOMALY, REPUTATION, NETWORK
    severity = Column(String(16), default='MEDIUM', nullable=False)
    score_impact = Column(Float, default=15.0, nullable=False)
    description = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
