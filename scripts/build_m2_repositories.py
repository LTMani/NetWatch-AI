import sys
sys.path.insert(0, '.')
from scripts.writer import write

device_repo = '''from typing import List, Optional, Dict, Any
from sqlalchemy import or_, desc, func
from app.models.device import Device, DeviceInterface, DeviceHistory, DeviceTag
from app.models.organization import Subnet, Department
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class DeviceRepository(BaseRepository):
    def __init__(self):
        super().__init__(Device)

    def get_by_mac(self, mac_address: str) -> Optional[Device]:
        return self.model.query.filter_by(mac_address=mac_address.upper(), is_deleted=False).first()

    def get_by_ip(self, ip_address: str) -> Optional[Device]:
        return self.model.query.filter_by(ip_address=ip_address.strip(), is_deleted=False).first()

    def list_devices(self, search: str = None, status: str = None, device_type: str = None,
                     department_id: str = None, subnet_id: str = None, min_risk: float = None,
                     page: int = 1, per_page: int = 25):
        query = self.model.query.filter_by(is_deleted=False)
        if search:
            s = f'%{search.strip()}%'
            query = query.filter(or_(
                self.model.name.ilike(s),
                self.model.hostname.ilike(s),
                self.model.ip_address.ilike(s),
                self.model.mac_address.ilike(s),
                self.model.assigned_user.ilike(s)
            ))
        if status:
            query = query.filter_by(status=status)
        if device_type:
            query = query.filter_by(device_type=device_type)
        if department_id:
            query = query.filter_by(department_id=department_id)
        if subnet_id:
            query = query.filter_by(subnet_id=subnet_id)
        if min_risk is not None:
            query = query.filter(self.model.risk_score >= min_risk)
        
        pagination = query.order_by(desc(self.model.risk_score), desc(self.model.last_seen_at)).paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': pagination.items,
            'total': pagination.total,
            'page': pagination.page,
            'per_page': pagination.per_page,
            'pages': pagination.pages
        }

    def get_device_summary_stats(self) -> Dict[str, Any]:
        total = self.model.query.filter_by(is_deleted=False).count()
        online = self.model.query.filter_by(status='online', is_deleted=False).count()
        offline = self.model.query.filter_by(status='offline', is_deleted=False).count()
        degraded = self.model.query.filter_by(status='degraded', is_deleted=False).count()
        high_risk = self.model.query.filter(self.model.risk_score >= 70.0, self.model.is_deleted == False).count()
        unauthorized = self.model.query.filter_by(is_authorized=False, is_deleted=False).count()
        
        # Type breakdown
        type_counts = db.session.query(
            Device.device_type, func.count(Device.id)
        ).filter_by(is_deleted=False).group_by(Device.device_type).all()
        
        return {
            'total_devices': total,
            'online_count': online,
            'offline_count': offline,
            'degraded_count': degraded,
            'high_risk_count': high_risk,
            'unauthorized_count': unauthorized,
            'type_breakdown': {t: count for t, count in type_counts}
        }

    def update_last_seen(self, device_id: str):
        device = self.get_by_id(device_id)
        if device:
            device.last_seen_at = utc_now()
            db.session.commit()
'''
write('app/repositories/device_repository.py', device_repo)

telemetry_repo = '''from typing import List, Dict, Any, Optional
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
'''
write('app/repositories/telemetry_repository.py', telemetry_repo)

domain_repo = '''from typing import List, Optional, Dict, Any
from app.models.domain import DomainCategory, DomainReputation, DomainFilterRule
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class DomainRepository(BaseRepository):
    def __init__(self):
        super().__init__(DomainCategory)

    def get_category_by_name(self, name: str) -> Optional[DomainCategory]:
        return DomainCategory.query.filter_by(name=name, is_deleted=False).first()

    def list_categories(self) -> List[DomainCategory]:
        return DomainCategory.query.filter_by(is_deleted=False).all()

    def get_domain_reputation(self, domain: str) -> Optional[DomainReputation]:
        return DomainReputation.query.filter_by(domain=domain.lower(), is_deleted=False).first()

    def upsert_domain_reputation(self, domain: str, category: str, score: int = 80, is_malicious: bool = False, threat_tags: str = None) -> DomainReputation:
        rep = self.get_domain_reputation(domain)
        if rep:
            rep.query_count += 1
            rep.last_queried_at = utc_now()
            if not rep.is_custom_override:
                rep.category = category
                rep.reputation_score = score
                rep.is_malicious = is_malicious
                rep.threat_tags = threat_tags
        else:
            rep = DomainReputation(
                domain=domain.lower(),
                category=category,
                reputation_score=score,
                is_malicious=is_malicious,
                threat_tags=threat_tags,
                query_count=1
            )
            db.session.add(rep)
        db.session.commit()
        return rep

    def list_filter_rules(self) -> List[DomainFilterRule]:
        return DomainFilterRule.query.filter_by(is_deleted=False).all()
'''
write('app/repositories/domain_repository.py', domain_repo)

write('app/repositories/__init__.py', '''from app.repositories.base_repository import BaseRepository
from app.repositories.user_repository import UserRepository
from app.repositories.audit_repository import AuditRepository
from app.repositories.device_repository import DeviceRepository
from app.repositories.telemetry_repository import TelemetryRepository
from app.repositories.domain_repository import DomainRepository
''')

print('Milestone 2 Repositories written successfully.')
