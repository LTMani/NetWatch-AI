from datetime import datetime, timezone
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
    """Authorized enterprise network endpoint, workstation, or infrastructure node."""
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
    """Network interface card (NIC) or virtual interface attached to a device."""
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
    """Historical state and connection log for compliance audit trails."""
    __tablename__ = 'nw_device_history'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=False, index=True)
    event_type = Column(String(64), nullable=False, index=True) # IP_CHANGE, STATUS_CHANGE, RISK_ELEVATION
    old_value = Column(String(128), nullable=True)
    new_value = Column(String(128), nullable=True)
    reason = Column(String(256), nullable=True)

    device = relationship('Device', back_populates='history')

class DeviceTag(BaseModel):
    """Administrative label/tag for device categorization (e.g., 'Production', 'Executive', 'POS')."""
    __tablename__ = 'nw_device_tags'

    name = Column(String(64), unique=True, nullable=False, index=True)
    color_hex = Column(String(7), default='#3B82F6')
    description = Column(String(128), nullable=True)

    devices = relationship('Device', secondary=device_tags, back_populates='tags')
