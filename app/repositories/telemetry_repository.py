from typing import List, Dict, Any, Optional
from datetime import datetime, timezone, timedelta
from sqlalchemy import desc, func, and_
from app.models.telemetry import NetworkFlowMetric, DNSQueryLog, BandwidthTimeseries, PacketMetric
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class TelemetryRepository(BaseRepository):
    def __init__(self):
        super().__init__(NetworkFlowMetric)

    def insert_flow_batch(self, flow_records: List[NetworkFlowMetric]):
        db.session.bulk_save_objects(flow_records)
        db.session.commit()

    def insert_dns_batch(self, dns_records: List[DNSQueryLog]):
        db.session.bulk_save_objects(dns_records)
        db.session.commit()

    def get_bandwidth_history(self, hours: int = 24, device_id: str = None, subnet_id: str = None) -> List[Dict[str, Any]]:
        cutoff = utc_now() - timedelta(hours=hours)
        query = NetworkFlowMetric.query.filter(NetworkFlowMetric.timestamp >= cutoff)
        if device_id:
            query = query.filter_by(device_id=device_id)
        if subnet_id:
            query = query.filter_by(subnet_id=subnet_id)
        
        # Aggregated hourly flows
        metrics = query.order_by(NetworkFlowMetric.timestamp.asc()).all()
        return metrics

    def get_recent_dns_queries(self, limit: int = 50, device_id: str = None, category: str = None, search: str = None):
        query = DNSQueryLog.query
        if device_id:
            query = query.filter_by(device_id=device_id)
        if category:
            query = query.filter_by(category=category)
        if search:
            query = query.filter(DNSQueryLog.domain_name.ilike(f'%{search.strip()}%'))
        return query.order_by(desc(DNSQueryLog.timestamp)).limit(limit).all()

    def get_top_domains(self, hours: int = 24, limit: int = 10):
        cutoff = utc_now() - timedelta(hours=hours)
        results = db.session.query(
            DNSQueryLog.domain_name,
            DNSQueryLog.category,
            func.count(DNSQueryLog.id).label('query_count'),
            func.sum(func.case((DNSQueryLog.is_blocked == True, 1), else_=0)).label('blocked_count')
        ).filter(DNSQueryLog.timestamp >= cutoff).group_by(
            DNSQueryLog.domain_name, DNSQueryLog.category
        ).order_by(desc('query_count')).limit(limit).all()

        return [{
            'domain': r[0],
            'category': r[1],
            'queries': r[2],
            'blocked': r[3]
        } for r in results]

    def get_category_traffic_distribution(self, hours: int = 24):
        cutoff = utc_now() - timedelta(hours=hours)
        results = db.session.query(
            DNSQueryLog.category,
            func.count(DNSQueryLog.id).label('query_count')
        ).filter(DNSQueryLog.timestamp >= cutoff).group_by(
            DNSQueryLog.category
        ).order_by(desc('query_count')).all()
        
        return {r[0]: r[1] for r in results}
