from typing import Dict, Any
from datetime import datetime, timezone, timedelta
from app.repositories.device_repository import DeviceRepository
from app.repositories.telemetry_repository import TelemetryRepository
from app.services.health_engine import NetworkHealthEngine
from app.models.device import Device
from app.models.telemetry import NetworkFlowMetric
from app.models.base import db
from sqlalchemy import func

class DashboardService:
    def __init__(self):
        self.device_repo = DeviceRepository()
        self.telemetry_repo = TelemetryRepository()
        self.health_engine = NetworkHealthEngine()

    def get_executive_summary(self) -> Dict[str, Any]:
        health = self.health_engine.calculate_health()
        dev_stats = self.device_repo.get_device_summary_stats()
        categories = self.telemetry_repo.get_category_traffic_distribution(hours=24)
        
        # High-risk devices leaderboard
        high_risk_devs = Device.query.filter(Device.risk_score >= 50.0, Device.is_deleted == False).order_by(
            Device.risk_score.desc()
        ).limit(5).all()

        return {
            'health_score': health.overall_score,
            'health_status': health.health_status,
            'health_change_24h': health.score_change_24h,
            'health_explanation': health.explanation,
            'active_devices': dev_stats['online_count'],
            'total_devices': dev_stats['total_devices'],
            'high_risk_device_count': dev_stats['high_risk_count'],
            'bandwidth_mbps': health.total_bandwidth_mbps,
            'avg_latency_ms': health.avg_latency_ms,
            'packet_loss_pct': health.avg_packet_loss_pct,
            'category_distribution': categories,
            'high_risk_leaderboard': [d.to_dict() for d in high_risk_devs]
        }
