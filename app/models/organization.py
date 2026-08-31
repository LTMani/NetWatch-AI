from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class Organization(BaseModel):
    __tablename__ = 'nw_organizations'

    name = Column(String(128), unique=True, nullable=False, index=True)
    domain = Column(String(128), nullable=True)
    office_start_time = Column(String(5), default='09:00', nullable=False)
    office_end_time = Column(String(5), default='18:00', nullable=False)
    work_days = Column(String(32), default='0,1,2,3,4', nullable=False)
    timezone = Column(String(64), default='UTC', nullable=False)
    retention_days = Column(Integer, default=90, nullable=False)

    departments = relationship('Department', back_populates='organization', cascade='all, delete-orphan')
    sites = relationship('NetworkSite', back_populates='organization', cascade='all, delete-orphan')
    users = relationship('User', back_populates='organization')
    devices = relationship('Device', back_populates='organization')

class Department(BaseModel):
    __tablename__ = 'nw_departments'

    organization_id = Column(String(36), ForeignKey('nw_organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = Column(String(128), nullable=False, index=True)
    code = Column(String(32), nullable=True)
    manager_name = Column(String(128), nullable=True)
    manager_email = Column(String(128), nullable=True)
    risk_threshold = Column(Integer, default=70, nullable=False)

    organization = relationship('Organization', back_populates='departments')
    users = relationship('User', back_populates='department')
    subnets = relationship('Subnet', back_populates='department')
    devices = relationship('Device', back_populates='department')

class NetworkSite(BaseModel):
    __tablename__ = 'nw_network_sites'

    organization_id = Column(String(36), ForeignKey('nw_organizations.id', ondelete='CASCADE'), nullable=False, index=True)
    name = Column(String(128), nullable=False, index=True)
    location_code = Column(String(32), nullable=False)
    city = Column(String(64), nullable=True)
    country = Column(String(64), nullable=True)
    primary_gateway_ip = Column(String(45), nullable=True)
    is_headquarters = Column(Boolean, default=False, nullable=False)

    organization = relationship('Organization', back_populates='sites')
    subnets = relationship('Subnet', back_populates='site')
    devices = relationship('Device', back_populates='site')

class Subnet(BaseModel):
    __tablename__ = 'nw_subnets'

    site_id = Column(String(36), ForeignKey('nw_network_sites.id'), nullable=True, index=True)
    department_id = Column(String(36), ForeignKey('nw_departments.id'), nullable=True, index=True)
    name = Column(String(128), nullable=False)
    cidr = Column(String(45), unique=True, nullable=False, index=True)
    network_address = Column(String(45), nullable=False)
    netmask = Column(String(45), nullable=False)
    gateway_ip = Column(String(45), nullable=True)
    vlan_id = Column(Integer, nullable=True, index=True)
    is_guest_network = Column(Boolean, default=False, nullable=False)
    is_dmz = Column(Boolean, default=False, nullable=False)
    description = Column(String(256), nullable=True)

    site = relationship('NetworkSite', back_populates='subnets')
    department = relationship('Department', back_populates='subnets')
    devices = relationship('Device', back_populates='subnet')
