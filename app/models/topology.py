from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db
from app.constants import TopologyNodeType

class TopologyNode(BaseModel):
    """Graph node representing a physical or virtual network asset in the topology."""
    __tablename__ = 'nw_topology_nodes'

    node_key = Column(String(64), unique=True, nullable=False, index=True)
    label = Column(String(128), nullable=False)
    node_type = Column(String(32), default=TopologyNodeType.WORKSTATION.value, nullable=False, index=True)
    ip_address = Column(String(45), nullable=True)
    mac_address = Column(String(17), nullable=True)
    
    device_id = Column(String(36), ForeignKey('nw_devices.id'), nullable=True, index=True)
    site_id = Column(String(36), ForeignKey('nw_network_sites.id'), nullable=True, index=True)
    subnet_id = Column(String(36), ForeignKey('nw_subnets.id'), nullable=True, index=True)
    
    pos_x = Column(Float, default=0.0, nullable=False)
    pos_y = Column(Float, default=0.0, nullable=False)
    tier_level = Column(Integer, default=3, nullable=False) # 0=Internet, 1=Firewall, 2=Core, 3=Access, 4=Endpoints
    status = Column(String(16), default='online', nullable=False)
    health_score = Column(Float, default=100.0, nullable=False)
    risk_score = Column(Float, default=0.0, nullable=False)
    
    device = relationship('Device')

class TopologyLink(BaseModel):
    """Directed or bidirectional network edge connecting two topology nodes."""
    __tablename__ = 'nw_topology_links'

    source_node_key = Column(String(64), ForeignKey('nw_topology_nodes.node_key'), nullable=False, index=True)
    target_node_key = Column(String(64), ForeignKey('nw_topology_nodes.node_key'), nullable=False, index=True)
    
    link_type = Column(String(32), default='ETHERNET', nullable=False) # ETHERNET, FIBER, WIRELESS, VPN
    bandwidth_capacity_mbps = Column(Integer, default=1000, nullable=False)
    current_traffic_mbps = Column(Float, default=0.0, nullable=False)
    latency_ms = Column(Float, default=1.0, nullable=False)
    packet_loss_pct = Column(Float, default=0.0, nullable=False)
    status = Column(String(16), default='UP', nullable=False) # UP, DEGRADED, DOWN
