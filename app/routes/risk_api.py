from flask import Blueprint, request, jsonify
from app.repositories.risk_repository import RiskRepository
from app.services.risk_engine import AssetRiskScoringEngine
from app.middleware.auth_middleware import login_required, roles_required

risk_api_bp = Blueprint('risk_api', __name__, url_prefix='/api/v1/risk')
risk_repo = RiskRepository()
risk_engine = AssetRiskScoringEngine()

@risk_api_bp.route('/leaderboard', methods=['GET'])
@risk_api_bp.route('/summary', methods=['GET'])
@login_required
def get_risk_leaderboard():
    limit = int(request.args.get('limit', 10))
    devs = risk_repo.get_highest_risk_devices(limit=limit)
    return jsonify({
        'status': 'success',
        'data': [d.to_dict() for d in devs]
    }), 200

@risk_api_bp.route('/device/<device_id>', methods=['GET'])
@login_required
def get_device_risk(device_id):
    factors = risk_repo.get_device_risk_factors(device_id)
    return jsonify({
        'status': 'success',
        'data': {
            'factors': [f.to_dict() for f in factors]
        }
    }), 200

@risk_api_bp.route('/recalculate', methods=['POST'])
@login_required
@roles_required('super_admin', 'security_analyst')
def trigger_recalculation():
    count = risk_engine.recalculate_all_devices()
    return jsonify({'status': 'success', 'message': f'Risk posture recalculated for {count} devices.'}), 200
