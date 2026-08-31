from flask import Blueprint, jsonify
from app.services.topology_engine import NetworkTopologyEngine
from app.repositories.topology_repository import TopologyRepository
from app.middleware.auth_middleware import login_required

topology_api_bp = Blueprint('topology_api', __name__, url_prefix='/api/v1/topology')
topo_engine = NetworkTopologyEngine()
topo_repo = TopologyRepository()

@topology_api_bp.route('/graph', methods=['GET'])
@login_required
def get_graph():
    graph = topo_engine.sync_topology_from_devices()
    return jsonify({'status': 'success', 'data': graph}), 200
