import sys
sys.path.insert(0, '.')
from scripts.writer import write

domain_engine = '''import re
from typing import Dict, Any, Tuple, Optional
from app.models.domain import DomainCategory, DomainReputation, DomainFilterRule
from app.repositories.domain_repository import DomainRepository
from app.constants import DomainCategoryEnum
from app.utils.validators import validate_domain_name

# Comprehensive Enterprise Known Domain Categorization Database
KNOWN_DOMAIN_DATABASE = {
    # Development & Engineering
    'github.com': ('Development', 95, False),
    'gitlab.com': ('Development', 95, False),
    'bitbucket.org': ('Development', 90, False),
    'stackoverflow.com': ('Development', 95, False),
    'stackexchange.com': ('Development', 90, False),
    'npmjs.com': ('Development', 90, False),
    'pypi.org': ('Development', 90, False),
    'docker.com': ('Development', 90, False),
    'hub.docker.com': ('Development', 90, False),
    'postman.com': ('Development', 90, False),
    'sentry.io': ('Development', 90, False),
    'datadoghq.com': ('Development', 90, False),
    'grafana.com': ('Development', 90, False),
    'jetbrains.com': ('Development', 95, False),
    
    # Documentation & Learning
    'docs.python.org': ('Documentation', 95, False),
    'developer.mozilla.org': ('Documentation', 95, False),
    'react.dev': ('Documentation', 95, False),
    'flask.palletsprojects.com': ('Documentation', 95, False),
    'docs.microsoft.com': ('Documentation', 95, False),
    'cloud.google.com': ('Documentation', 95, False),
    'docs.aws.amazon.com': ('Documentation', 95, False),
    'wikipedia.org': ('Documentation', 90, False),
    
    # Cloud Services & Infrastructure
    'aws.amazon.com': ('Cloud Services', 95, False),
    'amazonaws.com': ('Cloud Services', 95, False),
    'azure.microsoft.com': ('Cloud Services', 95, False),
    'cloudflare.com': ('Cloud Services', 95, False),
    'digitalocean.com': ('Cloud Services', 90, False),
    'gcp.google.com': ('Cloud Services', 95, False),
    'vercel.com': ('Cloud Services', 90, False),
    
    # Business & Productivity
    'microsoft.com': ('Business', 95, False),
    'office.com': ('Business', 95, False),
    'google.com': ('Business', 95, False),
    'atlassian.com': ('Business', 95, False),
    'jira.com': ('Business', 95, False),
    'notion.so': ('Business', 90, False),
    'salesforce.com': ('Business', 95, False),
    'workday.com': ('Business', 95, False),
    'servicenow.com': ('Business', 95, False),
    'docusign.com': ('Business', 95, False),
    
    # Communication
    'slack.com': ('Communication', 95, False),
    'zoom.us': ('Communication', 90, False),
    'teams.microsoft.com': ('Communication', 95, False),
    'discord.com': ('Communication', 75, False),
    'webex.com': ('Communication', 90, False),
    
    # Social Media
    'twitter.com': ('Social Media', 60, False),
    'x.com': ('Social Media', 60, False),
    'facebook.com': ('Social Media', 50, False),
    'instagram.com': ('Social Media', 50, False),
    'linkedin.com': ('Social Media', 85, False),
    'reddit.com': ('Social Media', 55, False),
    'tiktok.com': ('Social Media', 40, False),
    
    # Streaming & Entertainment
    'youtube.com': ('Streaming', 65, False),
    'netflix.com': ('Streaming', 50, False),
    'spotify.com': ('Streaming', 60, False),
    'twitch.tv': ('Streaming', 45, False),
    'hulu.com': ('Streaming', 45, False),
    'disneyplus.com': ('Streaming', 45, False),
    
    # Shopping
    'amazon.com': ('Shopping', 70, False),
    'ebay.com': ('Shopping', 65, False),
    'walmart.com': ('Shopping', 70, False),
    
    # Cryptocurrency
    'binance.com': ('Cryptocurrency', 50, False),
    'coinbase.com': ('Cryptocurrency', 60, False),
    'kraken.com': ('Cryptocurrency', 50, False),
    
    # Known Suspicious / Malicious patterns
    'evil-c2-server.net': ('Malicious', 5, True),
    'malware-drop-zone.cc': ('Malicious', 2, True),
    'phishing-verify-auth.xyz': ('Suspicious', 10, True),
    'crypto-miner-pool.top': ('Suspicious', 15, True),
    'dns-tunneling-probe.biz': ('Suspicious', 20, True)
}

class DomainClassificationEngine:
    def __init__(self, domain_repo: DomainRepository = None):
        self.domain_repo = domain_repo or DomainRepository()

    def classify_domain(self, domain_raw: str) -> Tuple[str, int, bool, str]:
        \"\"\"
        Classifies domain into category, reputation score, malicious flag, and description.
        Uses exact match -> Suffix match -> Heuristic regex match -> Default Unknown.
        \"\"\"
        try:
            clean_domain = validate_domain_name(domain_raw)
        except Exception:
            return DomainCategoryEnum.UNKNOWN.value, 50, False, 'Invalid Domain Syntax'

        # 1. Check direct database overrides
        rep = self.domain_repo.get_domain_reputation(clean_domain)
        if rep and rep.is_custom_override:
            return rep.category, rep.reputation_score, rep.is_malicious, 'Custom Override'

        # 2. Check Static Knowledgebase
        if clean_domain in KNOWN_DOMAIN_DATABASE:
            cat, score, mal = KNOWN_DOMAIN_DATABASE[clean_domain]
            return cat, score, mal, 'Static Knowledge Base'

        # 3. Suffix / Subdomain Matching (e.g. api.github.com -> github.com)
        parts = clean_domain.split('.')
        for i in range(1, len(parts) - 1):
            parent = '.'.join(parts[i:])
            if parent in KNOWN_DOMAIN_DATABASE:
                cat, score, mal = KNOWN_DOMAIN_DATABASE[parent]
                return cat, score, mal, f'Inherited from {parent}'

        # 4. Heuristic TLD & Keyword Classifiers
        if any(clean_domain.endswith(tld) for tld in ('.top', '.xyz', '.cc', '.buzz', '.work', '.gq', '.tk')):
            return DomainCategoryEnum.SUSPICIOUS.value, 35, False, 'High-Risk Generic TLD'

        if any(k in clean_domain for k in ('c2', 'botnet', 'payload', 'exploit', 'ransom')):
            return DomainCategoryEnum.SUSPICIOUS.value, 20, True, 'Suspicious Keyword Pattern'

        if any(k in clean_domain for k in ('git', 'code', 'dev', 'api', 'repo', 'build', 'ci')):
            return DomainCategoryEnum.DEVELOPMENT.value, 80, False, 'Developer Keyword Heuristic'

        if any(k in clean_domain for k in ('doc', 'learn', 'tutorial', 'wiki', 'guide')):
            return DomainCategoryEnum.DOCUMENTATION.value, 85, False, 'Documentation Keyword Heuristic'

        return DomainCategoryEnum.UNKNOWN.value, 70, False, 'Uncategorized Enterprise Traffic'

    def evaluate_filter_rules(self, domain: str) -> Optional[Dict[str, Any]]:
        \"\"\"Evaluates administrator domain filtering and blocking rules.\"\"\"
        rules = self.domain_repo.list_filter_rules()
        clean = domain.lower().strip()
        for rule in rules:
            if not rule.is_enabled:
                continue
            pattern = rule.domain_pattern.lower()
            if pattern == clean or (pattern.startswith('*.') and clean.endswith(pattern[1:])):
                return {
                    'blocked': rule.action == 'BLOCK',
                    'action': rule.action,
                    'reason': rule.reason,
                    'rule_id': rule.id
                }
        return None
'''
write('app/services/domain_engine.py', domain_engine)

device_service = '''from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from app.repositories.device_repository import DeviceRepository
from app.repositories.audit_repository import AuditRepository
from app.models.device import Device, DeviceInterface, DeviceHistory, DeviceTag
from app.models.organization import Subnet
from app.utils.ip_utils import normalize_mac_address, lookup_mac_vendor, ip_in_subnet
from app.utils.datetime_utils import utc_now
from app.constants import DeviceStatus, DeviceType, RiskLevel, AuditAction
from app.errors.exceptions import NotFoundError, ConflictError, ValidationError

class DeviceService:
    def __init__(self, device_repo: DeviceRepository = None, audit_repo: AuditRepository = None):
        self.device_repo = device_repo or DeviceRepository()
        self.audit_repo = audit_repo or AuditRepository()

    def register_device(self, data: Dict[str, Any], creator_id: str = None) -> Device:
        mac = normalize_mac_address(data.get('mac_address', ''))
        if not mac:
            raise ValidationError('Valid MAC address is required.')
        if self.device_repo.get_by_mac(mac):
            raise ConflictError(f'Device with MAC {mac} is already registered.')

        ip = data.get('ip_address', '').strip()
        vendor = lookup_mac_vendor(mac)
        
        device = Device(
            name=data.get('name', f'Endpoint-{mac[-5:].replace(\":\", \"\")}'),
            hostname=data.get('hostname'),
            ip_address=ip,
            mac_address=mac,
            device_type=data.get('device_type', DeviceType.WORKSTATION.value),
            operating_system=data.get('operating_system', 'Unknown OS'),
            os_version=data.get('os_version'),
            vendor=vendor,
            status=data.get('status', DeviceStatus.ONLINE.value),
            department_id=data.get('department_id'),
            site_id=data.get('site_id'),
            subnet_id=data.get('subnet_id'),
            assigned_user=data.get('assigned_user'),
            assigned_email=data.get('assigned_email'),
            is_authorized=bool(data.get('is_authorized', True))
        )
        created = self.device_repo.create(device)
        
        # Log history
        history = DeviceHistory(
            device_id=created.id,
            event_type='DEVICE_REGISTERED',
            new_value=f'IP: {ip}, MAC: {mac}',
            reason='Initial hardware inventory discovery'
        )
        from app.models.base import db
        db.session.add(history)
        db.session.commit()

        self.audit_repo.log_event(
            action=AuditAction.DEVICE_CREATED,
            resource_type='Device',
            username='system' if not creator_id else creator_id,
            resource_id=created.id,
            status='SUCCESS',
            details={'mac': mac, 'ip': ip, 'name': created.name}
        )
        return created

    def update_device(self, device_id: str, data: Dict[str, Any], user_id: str = None) -> Device:
        device = self.device_repo.get_by_id(device_id)
        if not device:
            raise NotFoundError('Device not found.')

        old_status = device.status
        old_ip = device.ip_address

        self.device_repo.update(device, data)

        if 'ip_address' in data and data['ip_address'] != old_ip:
            h = DeviceHistory(device_id=device.id, event_type='IP_CHANGED', old_value=old_ip, new_value=data['ip_address'], reason='DHCP lease renewal')
            from app.models.base import db
            db.session.add(h)
            db.session.commit()

        self.audit_repo.log_event(
            action=AuditAction.DEVICE_UPDATED,
            resource_type='Device',
            username=user_id or 'admin',
            resource_id=device.id,
            status='SUCCESS',
            details={'updated_fields': list(data.keys())}
        )
        return device

    def toggle_quarantine(self, device_id: str, quarantined: bool, reason: str = 'Policy violation', user_id: str = None) -> Device:
        device = self.device_repo.get_by_id(device_id)
        if not device:
            raise NotFoundError('Device not found.')
        
        device.is_quarantined = quarantined
        device.status = DeviceStatus.UNAUTHORIZED.value if quarantined else DeviceStatus.ONLINE.value
        from app.models.base import db
        db.session.commit()

        self.audit_repo.log_event(
            action='device_quarantine_toggled',
            resource_type='Device',
            username=user_id or 'admin',
            resource_id=device.id,
            status='SUCCESS',
            details={'quarantined': quarantined, 'reason': reason}
        )
        return device
'''
write('app/services/device_service.py', device_service)

telemetry_service = '''from typing import List, Dict, Any
from datetime import datetime, timezone
from app.repositories.telemetry_repository import TelemetryRepository
from app.repositories.device_repository import DeviceRepository
from app.services.domain_engine import DomainClassificationEngine
from app.models.telemetry import NetworkFlowMetric, DNSQueryLog
from app.utils.datetime_utils import utc_now, is_within_office_hours
from app.errors.exceptions import PrivacyViolationError, TelemetryIngestionError

class TelemetryIngestionService:
    def __init__(self, telemetry_repo: TelemetryRepository = None, device_repo: DeviceRepository = None):
        self.telemetry_repo = telemetry_repo or TelemetryRepository()
        self.device_repo = device_repo or DeviceRepository()
        self.domain_engine = DomainClassificationEngine()

    def ingest_flow_batch(self, flows: List[Dict[str, Any]]) -> Dict[str, Any]:
        \"\"\"Ingests a batch of NetFlow / IPFIX flow records strictly enforcing enterprise privacy boundaries.\"\"\"
        flow_objects = []
        now = utc_now()
        
        for item in flows:
            # Privacy boundary: ensure no packet payloads or private messages are present
            if any(forbidden in item for forbidden in ('payload', 'keystrokes', 'message_body', 'raw_packet')):
                raise PrivacyViolationError('Packet payload or private message capture violates enterprise privacy policy.')

            src_ip = item.get('source_ip')
            dst_ip = item.get('destination_ip')
            if not src_ip or not dst_ip:
                continue

            device = self.device_repo.get_by_ip(src_ip)
            device_id = device.id if device else None
            subnet_id = device.subnet_id if device else None

            # Calculate office hours status
            ts = now
            in_office = is_within_office_hours(ts)

            flow_obj = NetworkFlowMetric(
                device_id=device_id,
                subnet_id=subnet_id,
                source_ip=src_ip,
                source_port=int(item.get('source_port', 0)),
                destination_ip=dst_ip,
                destination_port=int(item.get('destination_port', 0)),
                protocol=item.get('protocol', 'TCP').upper(),
                bytes_in=int(item.get('bytes_in', 0)),
                bytes_out=int(item.get('bytes_out', 0)),
                packets_in=int(item.get('packets_in', 0)),
                packets_out=int(item.get('packets_out', 0)),
                duration_ms=int(item.get('duration_ms', 0)),
                latency_ms=float(item.get('latency_ms', 10.0)),
                jitter_ms=float(item.get('jitter_ms', 1.0)),
                packet_loss_percent=float(item.get('packet_loss_percent', 0.0)),
                tcp_flags=item.get('tcp_flags', 'ACK'),
                is_office_hours=in_office,
                timestamp=ts
            )
            flow_objects.append(flow_obj)

        if flow_objects:
            self.telemetry_repo.insert_flow_batch(flow_objects)

        return {
            'status': 'success',
            'ingested_count': len(flow_objects),
            'timestamp': now.isoformat()
        }

    def ingest_dns_query(self, device_ip: str, domain_name: str, query_type: str = 'A', response_code: str = 'NOERROR', response_time_ms: float = 12.0) -> DNSQueryLog:
        device = self.device_repo.get_by_ip(device_ip)
        device_id = device.id if device else None
        
        cat, score, is_mal, _ = self.domain_engine.classify_domain(domain_name)
        filter_res = self.domain_engine.evaluate_filter_rules(domain_name)
        is_blocked = filter_res['blocked'] if filter_res else is_mal
        block_reason = filter_res['reason'] if filter_res else ('Known malicious domain' if is_mal else None)

        now = utc_now()
        in_office = is_within_office_hours(now)

        dns_log = DNSQueryLog(
            device_id=device_id,
            domain_name=domain_name.lower().strip(),
            query_type=query_type,
            response_code=response_code,
            response_time_ms=response_time_ms,
            category=cat,
            is_blocked=is_blocked,
            block_reason=block_reason,
            is_office_hours=in_office,
            timestamp=now
        )
        from app.models.base import db
        db.session.add(dns_log)
        db.session.commit()
        return dns_log
'''
write('app/services/telemetry_service.py', telemetry_service)

write('app/services/__init__.py', '''from app.services.auth_service import AuthService
from app.services.audit_service import AuditService
from app.services.notification_service import NotificationService
from app.services.domain_engine import DomainClassificationEngine
from app.services.device_service import DeviceService
from app.services.telemetry_service import TelemetryIngestionService
''')

print('Milestone 2 Services generated.')
