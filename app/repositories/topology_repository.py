from typing import List, Dict, Any
from app.models.topology import TopologyNode, TopologyLink
from app.models.base import db

class TopologyRepository:
    def get_topology_graph(self) -> Dict[str, Any]:
        nodes = TopologyNode.query.filter_by(is_deleted=False).all()
        links = TopologyLink.query.filter_by(is_deleted=False).all()
        return {
            'nodes': [n.to_dict() for n in nodes],
            'links': [l.to_dict() for l in links]
        }

    def save_node(self, node: TopologyNode) -> TopologyNode:
        db.session.add(node)
        db.session.commit()
        return node

    def save_link(self, link: TopologyLink) -> TopologyLink:
        db.session.add(link)
        db.session.commit()
        return link
