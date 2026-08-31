from typing import List, Optional, Dict, Any
from datetime import datetime, timezone, timedelta
from sqlalchemy import desc
from app.models.health import HealthSnapshot, SubnetHealth
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class HealthRepository(BaseRepository):
    def __init__(self):
        super().__init__(HealthSnapshot)

    def get_latest_snapshot(self, site_id: str = None) -> Optional[HealthSnapshot]:
        query = HealthSnapshot.query
        if site_id:
            query = query.filter_by(site_id=site_id)
        return query.order_by(desc(HealthSnapshot.timestamp)).first()

    def get_health_trend(self, hours: int = 24, site_id: str = None) -> List[HealthSnapshot]:
        cutoff = utc_now() - timedelta(hours=hours)
        query = HealthSnapshot.query.filter(HealthSnapshot.timestamp >= cutoff)
        if site_id:
            query = query.filter_by(site_id=site_id)
        return query.order_by(HealthSnapshot.timestamp.asc()).all()

    def save_snapshot(self, snapshot: HealthSnapshot) -> HealthSnapshot:
        db.session.add(snapshot)
        db.session.commit()
        return snapshot
