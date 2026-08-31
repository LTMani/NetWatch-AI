from flask import Blueprint, request, jsonify
from app.repositories.alert_repository import AlertRepository
from app.middleware.auth_middleware import login_required
from app.models.alert import Alert
from app.models.base import db
from app.utils.datetime_utils import utc_now

alerts_api_bp = Blueprint('alerts_api', __name__, url_prefix='/api/v1/alerts')
alert_repo = AlertRepository()

@alerts_api_bp.route('', methods=['GET'])
@login_required
def list_alerts():
    sev = request.args.get('severity')
    cat = request.args.get('category')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 25))
    result = alert_repo.list_alerts(severity=sev, category=cat, page=page, per_page=per_page)
    return jsonify({
        'status': 'success',
        'data': {
            'items': [a.to_dict() for a in result['items']],
            'total': result['total'],
            'page': result['page'],
            'pages': result['pages']
        }
    }), 200

@alerts_api_bp.route('/correlated', methods=['GET'])
@login_required
def list_correlated_groups():
    groups = alert_repo.get_active_correlation_groups()
    return jsonify({'status': 'success', 'data': [g.to_dict() for g in groups]}), 200

@alerts_api_bp.route('/<alert_id>/acknowledge', methods=['POST'])
@login_required
def acknowledge_alert(alert_id):
    a = alert_repo.get_by_id(alert_id)
    if not a:
        return jsonify({'status': 'error', 'message': 'Alert not found.'}), 404
    a.is_acknowledged = True
    a.acknowledged_at = utc_now()
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Alert acknowledged.'}), 200
