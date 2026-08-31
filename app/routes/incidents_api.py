from flask import Blueprint, request, jsonify
from app.repositories.incident_repository import IncidentRepository
from app.services.incident_service import IncidentManagementService
from app.middleware.auth_middleware import login_required, roles_required, get_current_user

incidents_api_bp = Blueprint('incidents_api', __name__, url_prefix='/api/v1/incidents')
inc_repo = IncidentRepository()
inc_service = IncidentManagementService()

@incidents_api_bp.route('', methods=['GET'])
@login_required
def list_incidents():
    status = request.args.get('status')
    severity = request.args.get('severity')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    result = inc_repo.list_incidents(status=status, severity=severity, page=page, per_page=per_page)
    return jsonify({
        'status': 'success',
        'data': {
            'items': [i.to_dict() for i in result['items']],
            'total': result['total'],
            'page': result['page'],
            'pages': result['pages']
        }
    }), 200

@incidents_api_bp.route('/<incident_id>', methods=['GET'])
@login_required
def get_incident(incident_id):
    inc = inc_repo.get_by_id(incident_id)
    if not inc:
        return jsonify({'status': 'error', 'message': 'Incident not found.'}), 404
    data = inc.to_dict()
    data['timeline'] = [t.to_dict() for t in inc.timeline_entries]
    data['evidence'] = [e.to_dict() for e in inc.evidence_items]
    return jsonify({'status': 'success', 'data': data}), 200

@incidents_api_bp.route('', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin', 'security_analyst')
def create_incident():
    data = request.get_json() or {}
    user = get_current_user()
    inc = inc_service.create_incident(data, creator=user.username if user else 'admin')
    return jsonify({'status': 'success', 'message': 'Incident created.', 'data': inc.to_dict()}), 201

@incidents_api_bp.route('/<incident_id>/status', methods=['PATCH'])
@login_required
@roles_required('super_admin', 'security_analyst', 'network_admin')
def update_incident_status(incident_id):
    data = request.get_json() or {}
    user = get_current_user()
    inc = inc_service.update_incident_status(
        incident_id, data.get('status', 'investigating'),
        author=user.username if user else 'admin',
        notes=data.get('notes')
    )
    return jsonify({'status': 'success', 'message': 'Incident status updated.', 'data': inc.to_dict()}), 200

@incidents_api_bp.route('/<incident_id>/timeline', methods=['POST'])
@login_required
def add_timeline_entry(incident_id):
    data = request.get_json() or {}
    user = get_current_user()
    entry = inc_repo.add_timeline_entry(
        incident_id=incident_id,
        author=user.username if user else 'admin',
        entry_type=data.get('entry_type', 'NOTE'),
        message=data.get('message', '')
    )
    return jsonify({'status': 'success', 'message': 'Timeline note added.', 'data': entry.to_dict()}), 201
