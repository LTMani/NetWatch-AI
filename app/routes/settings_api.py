from flask import Blueprint, request, jsonify
from flask import current_app
from app.middleware.auth_middleware import login_required, roles_required
from app.models.organization import Organization
from app.models.base import db

settings_api_bp = Blueprint('settings_api', __name__, url_prefix='/api/v1/settings')

@settings_api_bp.route('/config', methods=['GET'])
@login_required
def get_settings():
    org = Organization.query.first()
    return jsonify({
        'status': 'success',
        'data': {
            'organization_name': org.name if org else 'Apex Enterprise Global',
            'office_start_time': org.office_start_time if org else '09:00',
            'office_end_time': org.office_end_time if org else '18:00',
            'work_days': org.work_days if org else '0,1,2,3,4',
            'timezone': org.timezone if org else 'UTC',
            'retention_days': org.retention_days if org else 90,
            'health_weights': current_app.config.get('HEALTH_WEIGHTS'),
            'anomaly_threshold': current_app.config.get('ANOMALY_Z_SCORE_THRESHOLD'),
            'privacy_payload_masking': True
        }
    }), 200

@settings_api_bp.route('/config', methods=['POST', 'PUT'])
@login_required
@roles_required('super_admin')
def update_settings():
    data = request.get_json() or {}
    org = Organization.query.first()
    if org:
        if 'organization_name' in data:
            org.name = data['organization_name']
        if 'office_start_time' in data:
            org.office_start_time = data['office_start_time']
        if 'office_end_time' in data:
            org.office_end_time = data['office_end_time']
        if 'retention_days' in data:
            org.retention_days = int(data['retention_days'])
        db.session.commit()
    return jsonify({'status': 'success', 'message': 'System settings updated successfully.'}), 200
