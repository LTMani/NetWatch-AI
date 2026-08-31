from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from sqlalchemy import desc
from app.models.incident import Incident, IncidentTimelineEntry, IncidentEvidence
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class IncidentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Incident)

    def get_next_incident_number(self) -> str:
        year = utc_now().year
        count = Incident.query.count() + 1
        return f'INC-{year}-{count:04d}'

    def list_incidents(self, status: str = None, severity: str = None, page: int = 1, per_page: int = 20):
        query = Incident.query.filter_by(is_deleted=False)
        if status:
            query = query.filter_by(status=status)
        if severity:
            query = query.filter_by(severity=severity)
        pagination = query.order_by(desc(Incident.created_at)).paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': pagination.items,
            'total': pagination.total,
            'page': pagination.page,
            'per_page': pagination.per_page,
            'pages': pagination.pages
        }

    def add_timeline_entry(self, incident_id: str, author: str, entry_type: str, message: str) -> IncidentTimelineEntry:
        entry = IncidentTimelineEntry(
            incident_id=incident_id,
            author=author,
            entry_type=entry_type,
            message=message,
            timestamp=utc_now()
        )
        db.session.add(entry)
        db.session.commit()
        return entry
