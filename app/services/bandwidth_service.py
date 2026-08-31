from typing import Dict, Any, List
from datetime import datetime, timezone, timedelta
from sqlalchemy import func, desc
from app.models.telemetry import NetworkFlowMetric
from app.models.device import Device
from app.models.base import db
from app.utils.datetime_utils import utc_now

class BandwidthAnalyticsService:
    def get_bandwidth_overview(self, hours: int = 24) -> Dict[str, Any]:
        cutoff = utc_now() - timedelta(hours=hours)
        
        # Total ingress and egress
        totals = db.session.query(
            func.sum(NetworkFlowMetric.bytes_in).label('total_in'),
            func.sum(NetworkFlowMetric.bytes_out).label('total_out')
        ).filter(NetworkFlowMetric.timestamp >= cutoff).first()

        bytes_in = totals[0] or 0
        bytes_out = totals[1] or 0

        # Protocol distribution
        proto_dist = db.session.query(
            NetworkFlowMetric.protocol,
            func.sum(NetworkFlowMetric.bytes_in + NetworkFlowMetric.bytes_out).label('volume')
        ).filter(NetworkFlowMetric.timestamp >= cutoff).group_by(NetworkFlowMetric.protocol).order_by(desc('volume')).all()

        # Top bandwidth consumers
        top_hogs = db.session.query(
            Device.name,
            Device.ip_address,
            Device.device_type,
            func.sum(NetworkFlowMetric.bytes_in + NetworkFlowMetric.bytes_out).label('total_bytes')
        ).join(Device, NetworkFlowMetric.device_id == Device.id).filter(
            NetworkFlowMetric.timestamp >= cutoff
        ).group_by(Device.id).order_by(desc('total_bytes')).limit(10).all()

        return {
            'hours': hours,
            'total_ingress_bytes': bytes_in,
            'total_egress_bytes': bytes_out,
            'total_volume_bytes': bytes_in + bytes_out,
            'protocol_distribution': {r[0]: r[1] for r in proto_dist},
            'top_consumers': [{
                'name': r[0],
                'ip': r[1],
                'type': r[2],
                'bytes': r[3]
            } for r in top_hogs]
        }
