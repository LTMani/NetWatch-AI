from flask import Blueprint, request, jsonify
from app.services.digital_twin_engine import NetworkDigitalTwinEngine
from app.repositories.digital_twin_repository import DigitalTwinRepository
from app.middleware.auth_middleware import login_required, roles_required, get_current_user

digital_twin_api_bp = Blueprint('digital_twin_api', __name__, url_prefix='/api/v1/digital-twin')
twin_engine = NetworkDigitalTwinEngine()
twin_repo = DigitalTwinRepository()

@digital_twin_api_bp.route('/scenarios', methods=['GET'])
@login_required
def list_scenarios():
    scenarios = twin_repo.list_scenarios()
    return jsonify({
        'status': 'success',
        'data': [s.to_dict() for s in scenarios]
    }), 200

@digital_twin_api_bp.route('/simulate', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin')
def run_simulation():
    data = request.get_json() or {}
    user = get_current_user()
    scenario = twin_engine.simulate_failure_scenario(
        scenario_name=data.get('name', ''),
        failed_node_key=data.get('node_key', 'NODE_ROUTER_CORE'),
        simulation_type=data.get('simulation_type', 'NODE_FAILURE'),
        executed_by=user.username if user else 'admin'
    )
    return jsonify({
        'status': 'success',
        'message': 'Digital Twin scenario simulation completed.',
        'data': scenario.to_dict()
    }), 201
