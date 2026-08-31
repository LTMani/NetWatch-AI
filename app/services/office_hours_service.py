from typing import Dict, Any, List
from datetime import datetime, timezone, timedelta
from sqlalchemy import func, case
from app.models.telemetry import NetworkFlowMetric, DNSQueryLog
from app.models.organization import Department
from app.models.device import Device
from app.models.base import db
from app.utils.datetime_utils import utc_now

class OfficeHoursAnalyticsService:
    def get_activity_comparison(self, days: int = 7) -> Dict[str, Any]:
        cutoff = utc_now() - timedelta(days=days)
        
        # In-office vs Out-of-office flow aggregates
        flow_stats = db.session.query(
            NetworkFlowMetric.is_office_hours,
            func.sum(NetworkFlowMetric.bytes_in + NetworkFlowMetric.bytes_out).label('total_bytes'),
            func.count(NetworkFlowMetric.id).label('total_flows')
        ).filter(NetworkFlowMetric.timestamp >= cutoff).group_by(NetworkFlowMetric.is_office_hours).all()

        office_bytes = 0
        off_hours_bytes = 0
        for in_office, b, _ in flow_stats:
            if in_office:
                office_bytes = b or 0
            else:
                off_hours_bytes = b or 0

        total_bytes = office_bytes + off_hours_bytes
        office_pct = round((office_bytes / total_bytes * 100), 1) if total_bytes > 0 else 0
        off_hours_pct = round((off_hours_bytes / total_bytes * 100), 1) if total_bytes > 0 else 0

        # Off-hours top active devices
        off_hours_devices = db.session.query(
            Device.name,
            Device.ip_address,
            Device.assigned_user,
            func.sum(NetworkFlowMetric.bytes_in + NetworkFlowMetric.bytes_out).label('off_bytes')
        ).join(Device, NetworkFlowMetric.device_id == Device.id).filter(
            NetworkFlowMetric.timestamp >= cutoff,
            NetworkFlowMetric.is_office_hours == False
        ).group_by(Device.id).order_by(func.sum(NetworkFlowMetric.bytes_in + NetworkFlowMetric.bytes_out).desc()).limit(10).all()

        return {
            'period_days': days,
            'office_hours_bytes': office_bytes,
            'office_hours_percentage': office_pct,
            'off_hours_bytes': off_hours_bytes,
            'off_hours_percentage': off_hours_pct,
            'top_off_hours_devices': [{
                'name': r[0],
                'ip': r[1],
                'user': r[2] or 'Unassigned',
                'volume_bytes': r[3]
            } for r in off_hours_devices]
        }
