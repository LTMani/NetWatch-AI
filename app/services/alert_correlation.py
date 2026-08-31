from typing import List, Optional
from datetime import datetime, timezone, timedelta
from app.models.alert import Alert, AlertCorrelationGroup
from app.repositories.alert_repository import AlertRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class AlertCorrelationEngine:
    def __init__(self, alert_repo: AlertRepository = None):
        self.alert_repo = alert_repo or AlertRepository()

    def correlate_alert(self, alert: Alert) -> Optional[AlertCorrelationGroup]:
        """
        Correlates incoming atomic alert into existing temporal and topological correlation groups.
        Collapses alert floods (e.g. 50 simultaneous high-latency alerts on same subnet into 1 group).
        """
        time_window = utc_now() - timedelta(minutes=15)
        
        # Build correlation key (e.g., SUBNET:192.168.1.0/24:PERFORMANCE)
        key = f'{alert.category}:{alert.subnet_id or alert.device_id or "GLOBAL"}'
        
        group = AlertCorrelationGroup.query.filter(
            AlertCorrelationGroup.correlation_key == key,
            AlertCorrelationGroup.last_seen_at >= time_window,
            AlertCorrelationGroup.is_active == True
        ).first()

        if group:
            group.alert_count += 1
            group.last_seen_at = utc_now()
            alert.correlation_group_id = group.id
        else:
            group = AlertCorrelationGroup(
                correlation_key=key,
                title=f'Correlated {alert.category} Incident ({alert.title})',
                severity=alert.severity,
                alert_count=1,
                first_seen_at=utc_now(),
                last_seen_at=utc_now(),
                is_active=True
            )
            db.session.add(group)
            db.session.flush()
            alert.correlation_group_id = group.id

        db.session.commit()
        return group
