from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db
from app.constants import IncidentStatus, IncidentSeverity

class Incident(BaseModel):
    """Formal enterprise network incident with investigation timeline and root-cause analysis."""
    __tablename__ = 'nw_incidents'

    incident_number = Column(String(32), unique=True, nullable=False, index=True) # e.g. INC-2026-0042
    title = Column(String(256), nullable=False, index=True)
    summary = Column(Text, nullable=False)
    
    status = Column(String(32), default=IncidentStatus.OPEN.value, nullable=False, index=True)
    severity = Column(String(32), default=IncidentSeverity.SEV2_HIGH.value, nullable=False, index=True)
    category = Column(String(64), default='Performance Degradation', nullable=False)
    
    assigned_to = Column(String(128), nullable=True) # User email or username
    lead_investigator = Column(String(128), nullable=True)
    
    affected_device_id = Column(String(36), ForeignKey('nw_devices.id'), nullable=True, index=True)
    affected_subnet_id = Column(String(36), ForeignKey('nw_subnets.id'), nullable=True, index=True)
    
    root_cause = Column(Text, nullable=True)
    remediation_steps = Column(Text, nullable=True)
    resolution_notes = Column(Text, nullable=True)
    resolved_at = Column(DateTime, nullable=True)
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    alerts = relationship('Alert', back_populates='incident')
    timeline_entries = relationship('IncidentTimelineEntry', back_populates='incident', cascade='all, delete-orphan', order_by='IncidentTimelineEntry.timestamp.asc()')
    evidence_items = relationship('IncidentEvidence', back_populates='incident', cascade='all, delete-orphan')

    def to_dict(self, exclude=None):
        data = super().to_dict(exclude=exclude)
        data['alert_count'] = len(self.alerts)
        data['timeline_count'] = len(self.timeline_entries)
        return data

class IncidentTimelineEntry(BaseModel):
    """Chronological log of activities, investigation notes, and status changes in an incident."""
    __tablename__ = 'nw_incident_timeline'

    incident_id = Column(String(36), ForeignKey('nw_incidents.id', ondelete='CASCADE'), nullable=False, index=True)
    author = Column(String(64), nullable=False)
    entry_type = Column(String(32), default='NOTE', nullable=False) # NOTE, STATUS_CHANGE, EVIDENCE_ADDED, ROOT_CAUSE_IDENTIFIED
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    incident = relationship('Incident', back_populates='timeline_entries')

class IncidentEvidence(BaseModel):
    """Attached telemetry evidence, flow dumps, or anomaly snapshots."""
    __tablename__ = 'nw_incident_evidence'

    incident_id = Column(String(36), ForeignKey('nw_incidents.id', ondelete='CASCADE'), nullable=False, index=True)
    evidence_type = Column(String(32), default='FLOW_METRIC', nullable=False)
    title = Column(String(128), nullable=False)
    payload_json = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    incident = relationship('Incident', back_populates='evidence_items')
