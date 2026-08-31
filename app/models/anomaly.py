from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db
from app.constants import AnomalyType, AlertSeverity

class AnomalyEvent(BaseModel):
    """Detected network telemetry anomaly identified by statistical or ML models."""
    __tablename__ = 'nw_anomaly_events'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=True, index=True)
    subnet_id = Column(String(36), ForeignKey('nw_subnets.id'), nullable=True, index=True)
    
    anomaly_type = Column(String(64), default=AnomalyType.BANDWIDTH_SURGE.value, nullable=False, index=True)
    severity = Column(String(16), default=AlertSeverity.MEDIUM.value, nullable=False, index=True)
    
    algorithm_used = Column(String(32), default='Z-Score', nullable=False) # Z-Score, EWMA, IsolationForest, MAD
    score = Column(Float, default=3.5, nullable=False)
    threshold = Column(Float, default=3.0, nullable=False)
    
    baseline_value = Column(Float, default=0.0, nullable=False)
    observed_value = Column(Float, default=0.0, nullable=False)
    unit = Column(String(16), default='bytes', nullable=False)
    
    description = Column(Text, nullable=False)
    is_acknowledged = Column(Boolean, default=False, nullable=False, index=True)
    is_false_positive = Column(Boolean, default=False, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    device = relationship('Device')

class AnomalyBaseline(BaseModel):
    """Calculated 30-day historical baseline metrics for devices and subnets."""
    __tablename__ = 'nw_anomaly_baselines'

    target_type = Column(String(16), default='DEVICE', nullable=False) # DEVICE, SUBNET, GLOBAL
    target_id = Column(String(36), nullable=False, index=True)
    metric_name = Column(String(64), nullable=False, index=True) # bandwidth_hourly, dns_query_rate, off_hours_volume
    
    mean_value = Column(Float, default=0.0, nullable=False)
    stddev_value = Column(Float, default=1.0, nullable=False)
    p95_value = Column(Float, default=0.0, nullable=False)
    sample_count = Column(Integer, default=100, nullable=False)
    last_updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
