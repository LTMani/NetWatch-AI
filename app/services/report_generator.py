import json
from typing import Dict, Any, List
from datetime import datetime, timezone, timedelta
from app.models.report import GeneratedReport
from app.repositories.report_repository import ReportRepository
from app.services.health_engine import NetworkHealthEngine
from app.repositories.device_repository import DeviceRepository
from app.repositories.telemetry_repository import TelemetryRepository
from app.utils.datetime_utils import utc_now

class ExecutiveReportGenerator:
    def __init__(self, report_repo: ReportRepository = None):
        self.report_repo = report_repo or ReportRepository()
        self.health_engine = NetworkHealthEngine()
        self.device_repo = DeviceRepository()
        self.telemetry_repo = TelemetryRepository()

    def generate_daily_summary(self, generated_by: str = 'admin') -> GeneratedReport:
        health = self.health_engine.calculate_health()
        dev_stats = self.device_repo.get_device_summary_stats()
        top_domains = self.telemetry_repo.get_top_domains(hours=24, limit=5)
        
        summary = f'Executive Network Intelligence Report for {utc_now().strftime("%Y-%m-%d")}. '
        summary += f'Composite Health Score: {health.overall_score}/100. Total Active Endpoints: {dev_stats["online_count"]}. '
        summary += f'High-Risk Assets: {dev_stats["high_risk_count"]}. Total Bandwidth: {health.total_bandwidth_mbps:.1f} Mbps.'

        report = GeneratedReport(
            title=f'Daily Network Summary -- {utc_now().strftime("%B %d, %Y")}',
            report_type='DAILY_SUMMARY',
            format='HTML',
            file_size_bytes=14280,
            generated_by=generated_by,
            summary_text=summary,
            created_at=utc_now()
        )
        return self.report_repo.save_report(report)
