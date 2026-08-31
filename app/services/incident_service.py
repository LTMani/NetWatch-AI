from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from app.repositories.incident_repository import IncidentRepository
from app.repositories.audit_repository import AuditRepository
from app.models.incident import Incident, IncidentTimelineEntry, IncidentEvidence
from app.constants import IncidentStatus, IncidentSeverity, AuditAction
from app.utils.datetime_utils import utc_now
from app.errors.exceptions import NotFoundError, ValidationError

class IncidentManagementService:
    def __init__(self, incident_repo: IncidentRepository = None, audit_repo: AuditRepository = None):
        self.incident_repo = incident_repo or IncidentRepository()
        self.audit_repo = audit_repo or AuditRepository()

    def create_incident(self, data: Dict[str, Any], creator: str = 'admin') -> Incident:
        inc_num = self.incident_repo.get_next_incident_number()
        title = data.get('title', '').strip()
        if not title:
            raise ValidationError('Incident title is required.')

        incident = Incident(
            incident_number=inc_num,
            title=title,
            summary=data.get('summary', 'Enterprise network incident created for investigation.'),
            status=data.get('status', IncidentStatus.OPEN.value),
            severity=data.get('severity', IncidentSeverity.SEV2_HIGH.value),
            category=data.get('category', 'Network Performance'),
            assigned_to=data.get('assigned_to'),
            lead_investigator=creator,
            affected_device_id=data.get('affected_device_id'),
            affected_subnet_id=data.get('affected_subnet_id'),
            root_cause=data.get('root_cause'),
            created_at=utc_now()
        )
        created = self.incident_repo.create(incident)
        
        # Initial timeline entry
        self.incident_repo.add_timeline_entry(
            incident_id=created.id,
            author=creator,
            entry_type='STATUS_CHANGE',
            message=f'Incident {inc_num} opened with severity {created.severity}.'
        )

        self.audit_repo.log_event(
            action=AuditAction.INCIDENT_CREATED,
            resource_type='Incident',
            username=creator,
            resource_id=created.id,
            status='SUCCESS',
            details={'incident_number': inc_num, 'severity': created.severity}
        )
        return created

    def update_incident_status(self, incident_id: str, new_status: str, author: str = 'admin', notes: str = None) -> Incident:
        incident = self.incident_repo.get_by_id(incident_id)
        if not incident:
            raise NotFoundError('Incident not found.')

        old_status = incident.status
        incident.status = new_status
        if new_status in ('resolved', 'closed'):
            incident.resolved_at = utc_now()
            if notes:
                incident.resolution_notes = notes

        from app.models.base import db
        db.session.commit()

        self.incident_repo.add_timeline_entry(
            incident_id=incident.id,
            author=author,
            entry_type='STATUS_CHANGE',
            message=f'Status transitioned from {old_status.upper()} to {new_status.upper()}. {notes or ""}'
        )

        self.audit_repo.log_event(
            action=AuditAction.INCIDENT_STATUS_CHANGED,
            resource_type='Incident',
            username=author,
            resource_id=incident.id,
            status='SUCCESS',
            details={'from': old_status, 'to': new_status}
        )
        return incident
