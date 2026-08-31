from flask import Blueprint, request, jsonify
from app.services.audit_service import AuditService
from app.middleware.auth_middleware import login_required, roles_required
from app.utils.exporters import export_to_csv_response

audit_api_bp = Blueprint('audit_api', __name__, url_prefix='/api/v1/audit-logs')
audit_service = AuditService()

@audit_api_bp.route('', methods=['GET'])
@login_required
@roles_required('super_admin', 'security_analyst', 'auditor')
def list_audit_logs():
    action = request.args.get('action')
    username = request.args.get('username')
    status = request.args.get('status')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 25))
    result = audit_service.get_logs(action=action, username=username, status=status, page=page, per_page=per_page)
    return jsonify({
        'status': 'success',
        'data': {
            'items': [log.to_dict() for log in result['items']],
            'total': result['total'],
            'page': result['page'],
            'pages': result['pages']
        }
    }), 200

@audit_api_bp.route('/verify-integrity', methods=['GET'])
@audit_api_bp.route('/verify', methods=['GET'])
@login_required
@roles_required('super_admin', 'auditor')
def verify_audit_integrity():
    result = audit_service.verify_chain_integrity()
    return jsonify({
        'status': 'success',
        'message': 'Cryptographic chain verification complete.',
        'data': result
    }), 200

@audit_api_bp.route('/export', methods=['GET'])
@login_required
@roles_required('super_admin', 'auditor')
def export_audit_logs():
    result = audit_service.get_logs(page=1, per_page=1000)
    rows = [l.to_dict() for l in result['items']]
    fields = ['id', 'created_at', 'username', 'action', 'resource_type', 'resource_id', 'status', 'ip_address', 'current_block_hash']
    return export_to_csv_response(rows, fields, filename='audit_log_export.csv')
