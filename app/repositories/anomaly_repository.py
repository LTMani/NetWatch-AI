from typing import List, Optional, Dict, Any
from datetime import datetime, timezone, timedelta
from sqlalchemy import desc, and_
from app.models.anomaly import AnomalyEvent, AnomalyBaseline
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class AnomalyRepository(BaseRepository):
    def __init__(self):
        super().__init__(AnomalyEvent)

    def list_anomalies(self, device_id: str = None, anomaly_type: str = None, severity: str = None,
                       unacknowledged_only: bool = False, page: int = 1, per_page: int = 25):
        query = AnomalyEvent.query.filter_by(is_deleted=False)
        if device_id:
            query = query.filter_by(device_id=device_id)
        if anomaly_type:
            query = query.filter_by(anomaly_type=anomaly_type)
        if severity:
            query = query.filter_by(severity=severity)
        if unacknowledged_only:
            query = query.filter_by(is_acknowledged=False)
            
        pagination = query.order_by(desc(AnomalyEvent.timestamp)).paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': pagination.items,
            'total': pagination.total,
            'page': pagination.page,
            'per_page': pagination.per_page,
            'pages': pagination.pages
        }

    def get_baseline(self, target_type: str, target_id: str, metric_name: str) -> Optional[AnomalyBaseline]:
        return AnomalyBaseline.query.filter_by(
            target_type=target_type, target_id=target_id, metric_name=metric_name
        ).first()

    def update_baseline(self, baseline: AnomalyBaseline):
        db.session.add(baseline)
        db.session.commit()
        return baseline
