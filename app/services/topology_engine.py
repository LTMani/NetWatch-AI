from typing import Dict, Any, List
from app.models.topology import TopologyNode, TopologyLink
from app.models.device import Device
from app.models.organization import Subnet, NetworkSite
from app.repositories.topology_repository import TopologyRepository
from app.utils.datetime_utils import utc_now
from app.models.base import db

class NetworkTopologyEngine:
    def __init__(self, topo_repo: TopologyRepository = None):
        self.topo_repo = topo_repo or TopologyRepository()

    def sync_topology_from_devices(self) -> Dict[str, Any]:
        """Builds hierarchical topology nodes and links from active devices, subnets, and sites."""
        nodes = []
        links = []

        # Layer 0: Internet Gateway
        inet_key = 'NODE_INTERNET'
        if not TopologyNode.query.filter_by(node_key=inet_key).first():
            db.session.add(TopologyNode(node_key=inet_key, label='External Internet', node_type='internet', tier_level=0, pos_x=400, pos_y=50, health_score=100.0))

        # Layer 1: Core Firewall
        fw_key = 'NODE_FIREWALL_CORE'
        if not TopologyNode.query.filter_by(node_key=fw_key).first():
            db.session.add(TopologyNode(node_key=fw_key, label='Edge Firewall 01', node_type='firewall', tier_level=1, pos_x=400, pos_y=160, ip_address='10.0.0.1', health_score=98.0))
            db.session.add(TopologyLink(source_node_key=inet_key, target_node_key=fw_key, bandwidth_capacity_mbps=10000, current_traffic_mbps=85.2, latency_ms=1.2))

        # Layer 2: Core Router
        cr_key = 'NODE_ROUTER_CORE'
        if not TopologyNode.query.filter_by(node_key=cr_key).first():
            db.session.add(TopologyNode(node_key=cr_key, label='Core Gateway Router', node_type='core_router', tier_level=2, pos_x=400, pos_y=280, ip_address='10.0.0.2', health_score=96.0))
            db.session.add(TopologyLink(source_node_key=fw_key, target_node_key=cr_key, bandwidth_capacity_mbps=10000, current_traffic_mbps=82.0, latency_ms=0.8))

        # Layer 3: Distribution Switches for Subnets
        subnets = Subnet.query.filter_by(is_deleted=False).all()
        for idx, sn in enumerate(subnets):
            sn_key = f'NODE_SWITCH_{sn.id[:8]}'
            if not TopologyNode.query.filter_by(node_key=sn_key).first():
                x = 150 + (idx * 250)
                db.session.add(TopologyNode(node_key=sn_key, label=f'Switch - {sn.name}', node_type='distribution_switch', tier_level=3, pos_x=x, pos_y=420, ip_address=sn.gateway_ip, health_score=95.0))
                db.session.add(TopologyLink(source_node_key=cr_key, target_node_key=sn_key, bandwidth_capacity_mbps=1000, current_traffic_mbps=32.4, latency_ms=0.5))

        db.session.commit()
        return self.topo_repo.get_topology_graph()
