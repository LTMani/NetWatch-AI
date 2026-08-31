from typing import List, Optional, Dict, Any
from datetime import datetime, timezone, timedelta
from sqlalchemy import desc, func
from app.models.alert import Alert, AlertCorrelationGroup
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class AlertRepository(BaseRepository):
    def __init__(self):
        super().__init__(Alert)

    def list_alerts(self, severity: str = None, category: str = None, unacknowledged_only: bool = False,
                    page: int = 1, per_page: int = 25):
        query = Alert.query.filter_by(is_deleted=False)
        if severity:
            query = query.filter_by(severity=severity)
        if category:
            query = query.filter_by(category=category)
        if unacknowledged_only:
            query = query.filter_by(is_acknowledged=False)
            
        pagination = query.order_by(desc(Alert.timestamp)).paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': pagination.items,
            'total': pagination.total,
            'page': pagination.page,
            'per_page': pagination.per_page,
            'pages': pagination.pages
        }

    def get_active_correlation_groups(self) -> List[AlertCorrelationGroup]:
        return AlertCorrelationGroup.query.filter_by(is_active=True, is_deleted=False).order_by(
            desc(AlertCorrelationGroup.last_seen_at)
        ).all()
