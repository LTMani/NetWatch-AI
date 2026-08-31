import sys
sys.path.insert(0, '.')
from scripts.writer import write

device_model = '''from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db
from app.constants import DeviceStatus, DeviceType, RiskLevel

# Association table for Device <-> Tag
device_tags = Table(
    'nw_device_tags_map',
    db.metadata,
    Column('device_id', String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), primary_key=True),
    Column('tag_id', String(36), ForeignKey('nw_device_tags.id', ondelete='CASCADE'), primary_key=True)
)

class Device(BaseModel):
    \"\"\"Authorized enterprise network endpoint, workstation, or infrastructure node.\"\"\"
    __tablename__ = 'nw_devices'

    name = Column(String(128), nullable=False, index=True)
    hostname = Column(String(128), nullable=True, index=True)
    ip_address = Column(String(45), nullable=False, index=True)
    mac_address = Column(String(17), unique=True, nullable=False, index=True)
    
    device_type = Column(String(32), default=DeviceType.WORKSTATION.value, nullable=False, index=True)
    operating_system = Column(String(64), nullable=True)
    os_version = Column(String(32), nullable=True)
    vendor = Column(String(64), nullable=True)
    
    status = Column(String(32), default=DeviceStatus.ONLINE.value, nullable=False, index=True)
    risk_score = Column(Float, default=0.0, nullable=False, index=True)
    risk_level = Column(String(16), default=RiskLevel.NEGLIGIBLE.value, nullable=False, index=True)
    
    organization_id = Column(String(36), ForeignKey('nw_organizations.id'), nullable=True, index=True)
    department_id = Column(String(36), ForeignKey('nw_departments.id'), nullable=True, index=True)
    site_id = Column(String(36), ForeignKey('nw_network_sites.id'), nullable=True, index=True)
    subnet_id = Column(String(36), ForeignKey('nw_subnets.id'), nullable=True, index=True)
    
    assigned_user = Column(String(128), nullable=True)
    assigned_email = Column(String(128), nullable=True)
    
    first_seen_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    last_seen_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)
    is_authorized = Column(Boolean, default=True, nullable=False, index=True)
    is_quarantined = Column(Boolean, default=False, nullable=False)
    
    # Relationships
    organization = relationship('Organization', back_populates='devices')
    department = relationship('Department', back_populates='devices')
    site = relationship('NetworkSite', back_populates='devices')
    subnet = relationship('Subnet', back_populates='devices')
    interfaces = relationship('DeviceInterface', back_populates='device', cascade='all, delete-orphan')
    history = relationship('DeviceHistory', back_populates='device', cascade='all, delete-orphan')
    tags = relationship('DeviceTag', secondary=device_tags, back_populates='devices', lazy='joined')
    flow_metrics = relationship('NetworkFlowMetric', back_populates='device', cascade='all, delete-orphan', lazy='dynamic')
    dns_queries = relationship('DNSQueryLog', back_populates='device', cascade='all, delete-orphan', lazy='dynamic')

    def to_dict(self, exclude=None):
        data = super().to_dict(exclude=exclude)
        data['tags'] = [t.name for t in self.tags]
        data['department_name'] = self.department.name if self.department else None
        data['subnet_cidr'] = self.subnet.cidr if self.subnet else None
        data['site_name'] = self.site.name if self.site else None
        return data

class DeviceInterface(BaseModel):
    \"\"\"Network interface card (NIC) or virtual interface attached to a device.\"\"\"
    __tablename__ = 'nw_device_interfaces'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=False, index=True)
    interface_name = Column(String(64), nullable=False) # eth0, wlan0, enp3s0
    mac_address = Column(String(17), nullable=False)
    ip_address = Column(String(45), nullable=True)
    speed_mbps = Column(Integer, default=1000, nullable=False)
    is_up = Column(Boolean, default=True, nullable=False)
    duplex = Column(String(16), default='full')
    mtu = Column(Integer, default=1500, nullable=False)

    device = relationship('Device', back_populates='interfaces')

class DeviceHistory(BaseModel):
    \"\"\"Historical state and connection log for compliance audit trails.\"\"\"
    __tablename__ = 'nw_device_history'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=False, index=True)
    event_type = Column(String(64), nullable=False, index=True) # IP_CHANGE, STATUS_CHANGE, RISK_ELEVATION
    old_value = Column(String(128), nullable=True)
    new_value = Column(String(128), nullable=True)
    reason = Column(String(256), nullable=True)

    device = relationship('Device', back_populates='history')

class DeviceTag(BaseModel):
    \"\"\"Administrative label/tag for device categorization (e.g., 'Production', 'Executive', 'POS').\"\"\"
    __tablename__ = 'nw_device_tags'

    name = Column(String(64), unique=True, nullable=False, index=True)
    color_hex = Column(String(7), default='#3B82F6')
    description = Column(String(128), nullable=True)

    devices = relationship('Device', secondary=device_tags, back_populates='tags')
'''
write('app/models/device.py', device_model)

telemetry_model = '''from datetime import datetime, timezone
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class NetworkFlowMetric(BaseModel):
    \"\"\"NetFlow / IPFIX metadata frame recording authorized connection statistics.\"\"\"
    __tablename__ = 'nw_flow_metrics'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=True, index=True)
    subnet_id = Column(String(36), ForeignKey('nw_subnets.id'), nullable=True, index=True)
    
    source_ip = Column(String(45), nullable=False, index=True)
    source_port = Column(Integer, nullable=False)
    destination_ip = Column(String(45), nullable=False, index=True)
    destination_port = Column(Integer, nullable=False, index=True)
    
    protocol = Column(String(16), default='TCP', nullable=False, index=True)
    bytes_in = Column(BigInteger, default=0, nullable=False)
    bytes_out = Column(BigInteger, default=0, nullable=False)
    packets_in = Column(Integer, default=0, nullable=False)
    packets_out = Column(Integer, default=0, nullable=False)
    
    duration_ms = Column(Integer, default=0, nullable=False)
    latency_ms = Column(Float, default=0.0, nullable=False)
    jitter_ms = Column(Float, default=0.0, nullable=False)
    packet_loss_percent = Column(Float, default=0.0, nullable=False)
    tcp_flags = Column(String(16), nullable=True)
    
    is_office_hours = Column(Boolean, default=True, nullable=False, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    device = relationship('Device', back_populates='flow_metrics')

class DNSQueryLog(BaseModel):
    \"\"\"Authorized domain-level resolution telemetry without payload inspection.\"\"\"
    __tablename__ = 'nw_dns_queries'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=True, index=True)
    domain_name = Column(String(256), nullable=False, index=True)
    query_type = Column(String(8), default='A', nullable=False) # A, AAAA, CNAME, MX, TXT, PTR
    response_code = Column(String(16), default='NOERROR', nullable=False) # NOERROR, NXDOMAIN, SERVFAIL
    response_ip = Column(String(45), nullable=True)
    response_time_ms = Column(Float, default=0.0, nullable=False)
    
    category = Column(String(64), default='Unknown', nullable=False, index=True)
    is_blocked = Column(Boolean, default=False, nullable=False, index=True)
    block_reason = Column(String(128), nullable=True)
    is_office_hours = Column(Boolean, default=True, nullable=False, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    device = relationship('Device', back_populates='dns_queries')

class BandwidthTimeseries(BaseModel):
    \"\"\"Aggregated hourly/5-min bandwidth time series for fast historical analytics.\"\"\"
    __tablename__ = 'nw_bandwidth_timeseries'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=True, index=True)
    subnet_id = Column(String(36), ForeignKey('nw_subnets.id'), nullable=True, index=True)
    site_id = Column(String(36), ForeignKey('nw_network_sites.id'), nullable=True, index=True)
    
    bytes_in = Column(BigInteger, default=0, nullable=False)
    bytes_out = Column(BigInteger, default=0, nullable=False)
    peak_bps_in = Column(Float, default=0.0, nullable=False)
    peak_bps_out = Column(Float, default=0.0, nullable=False)
    avg_latency_ms = Column(Float, default=0.0, nullable=False)
    avg_packet_loss = Column(Float, default=0.0, nullable=False)
    
    interval_start = Column(DateTime, nullable=False, index=True)
    interval_end = Column(DateTime, nullable=False)
    is_office_hours = Column(Boolean, default=True, nullable=False, index=True)

class PacketMetric(BaseModel):
    \"\"\"Raw network interface error counters and link performance metrics.\"\"\"
    __tablename__ = 'nw_packet_metrics'

    site_id = Column(String(36), ForeignKey('nw_network_sites.id'), nullable=True, index=True)
    interface_name = Column(String(64), nullable=False, index=True)
    rx_bytes = Column(BigInteger, default=0, nullable=False)
    tx_bytes = Column(BigInteger, default=0, nullable=False)
    rx_packets = Column(BigInteger, default=0, nullable=False)
    tx_packets = Column(BigInteger, default=0, nullable=False)
    rx_errors = Column(Integer, default=0, nullable=False)
    tx_errors = Column(Integer, default=0, nullable=False)
    rx_drops = Column(Integer, default=0, nullable=False)
    tx_drops = Column(Integer, default=0, nullable=False)
    link_flaps = Column(Integer, default=0, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)
'''
write('app/models/telemetry.py', telemetry_model)

domain_model = '''from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text
from app.models.base import BaseModel, db

class DomainCategory(BaseModel):
    \"\"\"Enterprise classification category for web traffic policy enforcement.\"\"\"
    __tablename__ = 'nw_domain_categories'

    name = Column(String(64), unique=True, nullable=False, index=True)
    display_name = Column(String(128), nullable=False)
    description = Column(String(256), nullable=True)
    is_work_related = Column(Boolean, default=True, nullable=False)
    is_restricted = Column(Boolean, default=False, nullable=False)
    risk_weight = Column(Integer, default=10, nullable=False) # 0-100
    color_hex = Column(String(7), default='#64748B')

class DomainReputation(BaseModel):
    \"\"\"Domain reputation cache and threat classification registry.\"\"\"
    __tablename__ = 'nw_domain_reputations'

    domain = Column(String(256), unique=True, nullable=False, index=True)
    category = Column(String(64), default='Unknown', nullable=False, index=True)
    reputation_score = Column(Integer, default=80, nullable=False) # 0 (Malicious) to 100 (Trusted)
    is_malicious = Column(Boolean, default=False, nullable=False, index=True)
    is_suspicious = Column(Boolean, default=False, nullable=False)
    is_custom_override = Column(Boolean, default=False, nullable=False)
    threat_tags = Column(String(256), nullable=True) # e.g. 'phishing,dga,c2'
    query_count = Column(Integer, default=1, nullable=False)
    last_queried_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

class DomainFilterRule(BaseModel):
    \"\"\"Administrative domain blocking or alerting policy rule.\"\"\"
    __tablename__ = 'nw_domain_filter_rules'

    domain_pattern = Column(String(256), nullable=False, index=True) # e.g. '*.torrent.org', 'tiktok.com'
    category = Column(String(64), nullable=True)
    action = Column(String(32), default='BLOCK', nullable=False) # BLOCK, ALERT, THROTTLE
    is_enabled = Column(Boolean, default=True, nullable=False, index=True)
    reason = Column(String(256), nullable=False)
'''
write('app/models/domain.py', domain_model)

print('Milestone 2 Models (Device, Telemetry, Domain) created successfully.')
