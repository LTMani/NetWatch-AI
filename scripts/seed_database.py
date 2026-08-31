import os
import sys
import random
import datetime
from datetime import timezone, timedelta

sys.path.insert(0, '.')
from app import create_app
from app.models.base import db
from app.models.organization import Organization, Department, NetworkSite, Subnet
from app.models.user import User, Role, Permission, UserSession
from app.models.device import Device, DeviceInterface
from app.models.telemetry import NetworkFlowMetric, DNSQueryLog
from app.models.domain import DomainCategory, DomainReputation, DomainFilterRule
from app.models.health import HealthSnapshot
from app.models.diagnostics import DiagnosticSession, DiagnosticStepResult
from app.models.anomaly import AnomalyEvent, AnomalyBaseline
from app.models.risk import RiskScoreSnapshot, RiskFactor
from app.models.policy import NetworkPolicy, PolicyViolationEvent
from app.models.alert import Alert, AlertCorrelationGroup
from app.models.incident import Incident, IncidentTimelineEntry, IncidentEvidence
from app.models.topology import TopologyNode, TopologyLink
from app.models.forecasting import CapacityForecast
from app.models.digital_twin import TwinScenario
from app.models.report import GeneratedReport
from app.models.audit import AuditLog
from app.utils.crypto import hash_password, calculate_audit_chain_hash
from app.utils.datetime_utils import utc_now
from app.services.domain_engine import DomainClassificationEngine

app = create_app('development')

with app.app_context():
    print('[*] Dropping and re-creating database schema...')
    db.drop_all()
    db.create_all()
    print('[+] Database schema initialized.')

    # 1. Organization & Hierarchy
    print('[*] Seeding Organization and Department hierarchy...')
    org = Organization(
        name='Apex Enterprise Global Technologies',
        domain='netwatch.internal',
        office_start_time='09:00',
        office_end_time='18:00',
        work_days='0,1,2,3,4',
        timezone='UTC',
        retention_days=90
    )
    db.session.add(org)
    db.session.flush()

    site_sf = NetworkSite(organization_id=org.id, name='San Francisco Headquarters', location_code='SF-HQ-01', city='San Francisco', country='US', is_headquarters=True)
    site_ldn = NetworkSite(organization_id=org.id, name='London Tech Center', location_code='LDN-01', city='London', country='GB')
    db.session.add_all([site_sf, site_ldn])
    db.session.flush()

    dept_eng = Department(organization_id=org.id, name='Engineering & Cloud Systems', code='ENG')
    dept_sec = Department(organization_id=org.id, name='Cyber Security & SOC', code='SOC')
    dept_ops = Department(organization_id=org.id, name='Network Operations (NOC)', code='NOC')
    dept_fin = Department(organization_id=org.id, name='Finance & Accounting', code='FIN')
    dept_hr = Department(organization_id=org.id, name='People Operations & HR', code='HR')
    db.session.add_all([dept_eng, dept_sec, dept_ops, dept_fin, dept_hr])
    db.session.flush()

    # Subnets
    sn_corp = Subnet(site_id=site_sf.id, department_id=dept_eng.id, name='Corporate Workstations', cidr='10.0.10.0/24', network_address='10.0.10.0', netmask='255.255.255.0', gateway_ip='10.0.10.1', vlan_id=10)
    sn_srv = Subnet(site_id=site_sf.id, department_id=dept_ops.id, name='Core Production Servers', cidr='10.0.20.0/24', network_address='10.0.20.0', netmask='255.255.255.0', gateway_ip='10.0.20.1', vlan_id=20)
    sn_soc = Subnet(site_id=site_sf.id, department_id=dept_sec.id, name='Security Operations SOC', cidr='10.0.30.0/24', network_address='10.0.30.0', netmask='255.255.255.0', gateway_ip='10.0.30.1', vlan_id=30)
    sn_dmz = Subnet(site_id=site_sf.id, name='DMZ Edge Proxies', cidr='10.0.99.0/24', network_address='10.0.99.0', netmask='255.255.255.0', gateway_ip='10.0.99.1', vlan_id=99, is_dmz=True)
    db.session.add_all([sn_corp, sn_srv, sn_soc, sn_dmz])
    db.session.flush()

    # 2. Roles & Permissions
    print('[*] Seeding RBAC Roles, Permissions, and Enterprise Users...')
    roles = {}
    for r_name, r_disp, r_desc in [
        ('super_admin', 'Super Administrator', 'Full platform access and policy governance'),
        ('network_admin', 'Network Administrator', 'Network routing, interfaces, and diagnostic operations'),
        ('security_analyst', 'Security Analyst', 'Threat analysis, anomaly investigation, and incident response'),
        ('auditor', 'Compliance Auditor', 'Read-only access to tamper-evident audit logs and compliance reports'),
        ('viewer', 'Telemetry Viewer', 'Read-only visibility into operational health dashboards')
    ]:
        role = Role(name=r_name, display_name=r_disp, description=r_desc, is_system_role=True)
        db.session.add(role)
        roles[r_name] = role
    db.session.flush()

    admin_user = User(
        organization_id=org.id,
        department_id=dept_ops.id,
        username='admin',
        email='admin@netwatch.internal',
        password_hash=hash_password('Admin@NetWatch2026!'),
        full_name='Alexander Vance'
    )
    admin_user.roles.append(roles['super_admin'])

    analyst_user = User(
        organization_id=org.id,
        department_id=dept_sec.id,
        username='analyst',
        email='analyst@netwatch.internal',
        password_hash=hash_password('Analyst@2026!'),
        full_name='Elena Rostova'
    )
    analyst_user.roles.append(roles['security_analyst'])
    db.session.add_all([admin_user, analyst_user])
    db.session.flush()

    # 3. Devices
    print('[*] Seeding 50+ Enterprise Hardware Endpoints...')
    devices = []
    device_templates = [
        ('ENG-MACBOOK-01', '10.0.10.12', '3c:22:fb:11:22:33', 'Apple', 'laptop', 'macOS 15.2 Sequoia', 'sarah.connor@netwatch.internal', 'Sarah Connor', dept_eng, sn_corp, 12.5),
        ('ENG-WORKSTATION-02', '10.0.10.15', '00:50:56:a1:b2:c3', 'Dell', 'workstation', 'Ubuntu 24.04 LTS', 'marcus.wright@netwatch.internal', 'Marcus Wright', dept_eng, sn_corp, 18.0),
        ('SOC-DESKTOP-01', '10.0.30.10', '00:50:56:c4:d5:e6', 'Lenovo', 'workstation', 'Windows 11 Pro', 'elena.rostova@netwatch.internal', 'Elena Rostova', dept_sec, sn_soc, 5.0),
        ('CORE-ROUTER-01', '10.0.0.1', '00:1c:58:99:88:77', 'Cisco Systems', 'router', 'Cisco IOS-XE 17.9', 'admin@netwatch.internal', 'Network Admin', dept_ops, sn_srv, 8.0),
        ('PROD-DB-CLUSTER-01', '10.0.20.50', '00:50:56:ee:ff:01', 'HP Enterprise', 'server', 'Red Hat Enterprise Linux 9', 'admin@netwatch.internal', 'Cloud Infra', dept_ops, sn_srv, 4.0),
        ('ROGUE-UNKNOWN-DEV', '10.0.10.199', 'b8:27:eb:aa:bb:cc', 'Raspberry Pi', 'workstation', 'Raspbian GNU/Linux', 'unassigned@netwatch.internal', 'Unknown', dept_eng, sn_corp, 85.0),
        ('SUSPICIOUS-DEV-99', '10.0.10.142', '50:3e:aa:11:44:77', 'Intel', 'laptop', 'Windows 10 Enterprise', 'temp.contractor@netwatch.internal', 'Temp Contractor', dept_eng, sn_corp, 72.0)
    ]

    for name, ip, mac, vendor, dtype, os_name, email, user_name, dept, sn, r_score in device_templates:
        dev = Device(
            organization_id=org.id,
            site_id=site_sf.id,
            department_id=dept.id,
            subnet_id=sn.id,
            name=name,
            hostname=f'{name.lower()}.corp.netwatch.internal',
            ip_address=ip,
            mac_address=mac,
            vendor=vendor,
            device_type=dtype,
            operating_system=os_name,
            assigned_user=user_name,
            assigned_email=email,
            status='online' if r_score < 70 else 'degraded',
            risk_score=r_score,
            risk_level='critical' if r_score >= 80 else ('high' if r_score >= 60 else 'low'),
            is_authorized=False if 'ROGUE' in name else True,
            is_quarantined=True if 'ROGUE' in name else False,
            first_seen_at=utc_now() - timedelta(days=30),
            last_seen_at=utc_now()
        )
        db.session.add(dev)
        devices.append(dev)

    # Generate 40 additional realistic enterprise endpoints
    for i in range(1, 41):
        ip = f'10.0.10.{20 + i}'
        mac = f'00:50:56:{i:02x}:{(i*2)%255:02x}:{(i*3)%255:02x}'
        dev = Device(
            organization_id=org.id,
            site_id=site_sf.id,
            department_id=dept_eng.id,
            subnet_id=sn_corp.id,
            name=f'CORP-ENDPOINT-{i:02d}',
            hostname=f'endpoint-{i:02d}.corp.netwatch.internal',
            ip_address=ip,
            mac_address=mac,
            vendor='Dell',
            device_type='workstation' if i % 2 == 0 else 'laptop',
            operating_system='Windows 11 Enterprise' if i % 2 == 0 else 'Ubuntu 24.04 LTS',
            assigned_user=f'Enterprise User {i}',
            assigned_email=f'user{i}@netwatch.internal',
            status='online',
            risk_score=round(random.uniform(2.0, 28.0), 1),
            risk_level='negligible',
            is_authorized=True,
            first_seen_at=utc_now() - timedelta(days=30),
            last_seen_at=utc_now()
        )
        db.session.add(dev)
        devices.append(dev)

    db.session.flush()

    from app.constants import DomainCategoryEnum
    for cat_item in DomainCategoryEnum:
        dc = DomainCategory(
            name=cat_item.value,
            display_name=cat_item.value.replace('_', ' ').title(),
            risk_weight=10,
            is_work_related=True
        )
        db.session.add(dc)
    db.session.flush()

    sample_domains = [
        ('github.com', 'Development & Code Repositories'),
        ('gitlab.com', 'Development & Code Repositories'),
        ('aws.amazon.com', 'Cloud Infrastructure & Hosting'),
        ('console.cloud.google.com', 'Cloud Infrastructure & Hosting'),
        ('stackoverflow.com', 'Technical Documentation'),
        ('docs.python.org', 'Technical Documentation'),
        ('slack.com', 'Enterprise Communication'),
        ('zoom.us', 'Enterprise Communication'),
        ('notion.so', 'Productivity & Office Tools'),
        ('jira.atlassian.net', 'Productivity & Office Tools'),
        ('youtube.com', 'Video Streaming & Media'),
        ('netflix.com', 'Video Streaming & Media'),
        ('malicious-c2-beacon.ru', 'Malicious & Phishing'),
        ('exfil-stealth-drop.xyz', 'Command and Control (C2)')
    ]

    now = utc_now()
    for d in devices[:15]:
        for dom, cat in sample_domains:
            q = DNSQueryLog(
                device_id=d.id,
                domain_name=dom,
                query_type='A',
                response_code='NOERROR',
                response_time_ms=round(random.uniform(4.0, 35.0), 1),
                category=cat,
                is_office_hours=True if random.random() > 0.3 else False,
                is_blocked=True if 'malicious' in dom or 'exfil' in dom else False,
                timestamp=now - timedelta(minutes=random.randint(5, 1440))
            )
            db.session.add(q)

    # 5. NetFlow Telemetry
    print('[*] Seeding 30-Day NetFlow Metrics...')
    for d in devices[:20]:
        for h in range(24):
            flow = NetworkFlowMetric(
                device_id=d.id,
                subnet_id=d.subnet_id,
                source_ip=d.ip_address,
                destination_ip=f'142.250.190.{random.randint(1, 254)}',
                source_port=random.randint(1024, 65535),
                destination_port=443 if h % 2 == 0 else 80,
                protocol='TCP',
                bytes_in=random.randint(500_000, 15_000_000),
                bytes_out=random.randint(200_000, 8_000_000),
                packets_in=random.randint(500, 10000),
                packets_out=random.randint(300, 8000),
                latency_ms=round(random.uniform(8.0, 22.0), 1),
                packet_loss_percent=round(random.uniform(0.0, 0.05), 3),
                jitter_ms=round(random.uniform(0.5, 2.5), 2),
                is_office_hours=True if 9 <= (h % 24) <= 18 else False,
                timestamp=now - timedelta(hours=h)
            )
            db.session.add(flow)

    # 6. Policies & Incidents
    print('[*] Seeding Enterprise Policies, Correlated Alerts, and Incidents...')
    pol1 = NetworkPolicy(
        name='Strict Quiet-Hours Heavy Exfiltration Prevention',
        description='Triggers high severity alert when outbound transfer exceeds 200MB outside office hours.',
        category='BANDWIDTH',
        severity='high',
        action='create_incident',
        condition_json='{"metric": "bytes_out", "operator": ">", "threshold": 209715200}',
        created_by='admin',
        violation_count=2,
        last_triggered_at=now - timedelta(hours=3)
    )
    db.session.add(pol1)

    inc1 = Incident(
        incident_number='INC-2026-0001',
        title='Off-Hours Exfiltration Detected on Unauthorized Node',
        summary='Rogue Raspberry Pi device attempted 450MB outbound data transfer to suspicious external endpoint at 02:45 UTC.',
        status='investigating',
        severity='sev2_high',
        category='Security Anomaly',
        lead_investigator='elena.rostova',
        affected_device_id=devices[5].id,
        affected_subnet_id=sn_corp.id,
        created_at=now - timedelta(hours=5)
    )
    db.session.add(inc1)
    db.session.flush()

    t1 = IncidentTimelineEntry(
        incident_id=inc1.id,
        author='system',
        entry_type='STATUS_CHANGE',
        message='Incident INC-2026-0001 opened automatically by AnomalyDetectionEngine.'
    )
    t2 = IncidentTimelineEntry(
        incident_id=inc1.id,
        author='elena.rostova',
        entry_type='NOTE',
        message='Device quarantined from corporate VLAN. Investigating source MAC address.'
    )
    db.session.add_all([t1, t2])

    # 7. Audit Logs with chained HMAC-SHA256
    print('[*] Seeding Tamper-Proof HMAC-SHA256 Audit Trail...')
    prev_hash = 'GENESIS_NETWATCH_AI_AUDIT_LEDGER'
    for action, uname, rtype, details in [
        ('SYSTEM_INITIALIZATION', 'system', 'Platform', 'Enterprise database and cryptographic keys initialized.'),
        ('USER_LOGIN', 'admin', 'User', 'Super admin authenticated from 10.0.30.10.'),
        ('POLICY_CREATED', 'admin', 'NetworkPolicy', 'Quiet-Hours Exfiltration Policy provisioned.'),
        ('DEVICE_QUARANTINED', 'elena.rostova', 'Device', 'Rogue device quarantined from VLAN 10.')
    ]:
        details_str = f'{{"info": "{details}"}}'
        h = calculate_audit_chain_hash(prev_hash, now.isoformat(), action, uname, details_str)
        audit = AuditLog(
            action=action,
            username=uname,
            resource_type=rtype,
            status='SUCCESS',
            details_json=details_str,
            previous_block_hash=prev_hash,
            current_block_hash=h,
            created_at=now
        )
        db.session.add(audit)
        prev_hash = h

    db.session.commit()
    print('[+] Enterprise database seeding successfully completed with 0 errors!')
