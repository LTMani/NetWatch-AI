from flask import Blueprint, request, jsonify
from app.repositories.anomaly_repository import AnomalyRepository
from app.services.anomaly_engine import AnomalyDetectionEngine
from app.middleware.auth_middleware import login_required, roles_required
from app.models.base import db

anomalies_api_bp = Blueprint('anomalies_api', __name__, url_prefix='/api/v1/anomalies')
anom_repo = AnomalyRepository()
anom_engine = AnomalyDetectionEngine()

@anomalies_api_bp.route('', methods=['GET'])
@anomalies_api_bp.route('/events', methods=['GET'])
@login_required
def list_anomalies():
    dev_id = request.args.get('device_id')
    anom_type = request.args.get('type')
    severity = request.args.get('severity')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 25))
    
    result = anom_repo.list_anomalies(device_id=dev_id, anomaly_type=anom_type, severity=severity, page=page, per_page=per_page)
    return jsonify({
        'status': 'success',
        'data': {
            'items': [a.to_dict() for a in result['items']],
            'total': result['total'],
            'page': result['page'],
            'pages': result['pages']
        }
    }), 200

@anomalies_api_bp.route('/detect', methods=['POST'])
@login_required
@roles_required('super_admin', 'security_analyst')
def trigger_detection():
    new_anomalies = anom_engine.detect_traffic_anomalies()
    return jsonify({
        'status': 'success',
        'message': f'Anomaly scan completed. {len(new_anomalies)} anomalies identified.',
        'count': len(new_anomalies),
        'data': [a.to_dict() for a in new_anomalies]
    }), 200

@anomalies_api_bp.route('/<anomaly_id>/acknowledge', methods=['POST'])
@login_required
def acknowledge_anomaly(anomaly_id):
    anom = anom_repo.get_by_id(anomaly_id)
    if not anom:
        return jsonify({'status': 'error', 'message': 'Anomaly not found.'}), 404
    anom.is_acknowledged = True
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Anomaly acknowledged.'}), 200
