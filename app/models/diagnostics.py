from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class DiagnosticSession(BaseModel):
    """Executed slow network diagnostic session recording end-to-end telemetry probe results."""
    __tablename__ = 'nw_diagnostic_sessions'

    target_scope = Column(String(128), default='Global Gateway', nullable=False)
    initiated_by = Column(String(64), default='system', nullable=False)
    status = Column(String(32), default='COMPLETED', nullable=False) # RUNNING, COMPLETED, FAILED
    
    overall_health_score = Column(Float, default=100.0, nullable=False)
    detected_bottleneck = Column(String(128), nullable=True)
    confidence_level = Column(Float, default=0.85, nullable=False) # 0.0 to 1.0
    root_cause_summary = Column(Text, nullable=True)
    remediation_playbook = Column(Text, nullable=True)
    
    duration_seconds = Column(Float, default=1.5, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    steps = relationship('DiagnosticStepResult', back_populates='session', cascade='all, delete-orphan')

class DiagnosticStepResult(BaseModel):
    """Individual stage in the 7-step diagnostic pipeline."""
    __tablename__ = 'nw_diagnostic_step_results'

    session_id = Column(String(36), ForeignKey('nw_diagnostic_sessions.id', ondelete='CASCADE'), nullable=False, index=True)
    step_number = Column(Integer, nullable=False)
    step_name = Column(String(64), nullable=False) # Connectivity, Latency, Loss, DNS, Bandwidth, Hardware, Synthesis
    status = Column(String(16), default='PASSED', nullable=False) # PASSED, WARNING, FAILED
    metric_value = Column(String(64), nullable=True)
    threshold_value = Column(String(64), nullable=True)
    finding_details = Column(Text, nullable=False)

    session = relationship('DiagnosticSession', back_populates='steps')
