from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db
from app.constants import HealthStatus

class HealthSnapshot(BaseModel):
    """Point-in-time calculation of composite enterprise network health."""
    __tablename__ = 'nw_health_snapshots'

    site_id = Column(String(36), ForeignKey('nw_network_sites.id'), nullable=True, index=True)
    overall_score = Column(Float, default=100.0, nullable=False, index=True) # 0-100
    health_status = Column(String(32), default=HealthStatus.OPTIMAL.value, nullable=False)
    
    latency_score = Column(Float, default=100.0, nullable=False)
    packet_loss_score = Column(Float, default=100.0, nullable=False)
    jitter_score = Column(Float, default=100.0, nullable=False)
    bandwidth_score = Column(Float, default=100.0, nullable=False)
    error_rate_score = Column(Float, default=100.0, nullable=False)
    link_flap_score = Column(Float, default=100.0, nullable=False)
    
    avg_latency_ms = Column(Float, default=0.0, nullable=False)
    avg_packet_loss_pct = Column(Float, default=0.0, nullable=False)
    avg_jitter_ms = Column(Float, default=0.0, nullable=False)
    total_bandwidth_mbps = Column(Float, default=0.0, nullable=False)
    active_device_count = Column(Integer, default=0, nullable=False)
    
    score_change_24h = Column(Float, default=0.0, nullable=False)
    explanation = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

class SubnetHealth(BaseModel):
    """Health state evaluated at individual subnet granularity."""
    __tablename__ = 'nw_subnet_health'

    subnet_id = Column(String(36), ForeignKey('nw_subnets.id', ondelete='CASCADE'), nullable=False, index=True)
    health_score = Column(Float, default=100.0, nullable=False)
    avg_latency_ms = Column(Float, default=0.0, nullable=False)
    packet_loss_pct = Column(Float, default=0.0, nullable=False)
    utilization_pct = Column(Float, default=0.0, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)
