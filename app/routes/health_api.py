from flask import Blueprint, request, jsonify
from app.services.health_engine import NetworkHealthEngine
from app.repositories.health_repository import HealthRepository
from app.middleware.auth_middleware import login_required

health_api_bp = Blueprint('health_api', __name__, url_prefix='/api/v1/health')
health_engine = NetworkHealthEngine()
health_repo = HealthRepository()

@health_api_bp.route('/current', methods=['GET'])
@health_api_bp.route('/summary', methods=['GET'])
@login_required
def get_current_health():
    snapshot = health_engine.calculate_health()
    return jsonify({'status': 'success', 'data': snapshot.to_dict()}), 200

@health_api_bp.route('/trend', methods=['GET'])
@login_required
def get_health_trend():
    hours = int(request.args.get('hours', 24))
    trend = health_repo.get_health_trend(hours=hours)
    return jsonify({
        'status': 'success',
        'data': [s.to_dict() for s in trend]
    }), 200
