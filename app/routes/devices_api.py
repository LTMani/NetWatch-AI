from flask import Blueprint, request, jsonify
from app.repositories.device_repository import DeviceRepository
from app.services.device_service import DeviceService
from app.schemas.device_schemas import DeviceCreateSchema
from app.middleware.auth_middleware import login_required, roles_required, get_current_user
from app.errors.exceptions import NotFoundError
from app.utils.exporters import export_to_csv_response

devices_api_bp = Blueprint('devices_api', __name__, url_prefix='/api/v1/devices')
device_repo = DeviceRepository()
device_service = DeviceService()

@devices_api_bp.route('', methods=['GET'])
@login_required
def list_devices():
    search = request.args.get('search')
    status = request.args.get('status')
    device_type = request.args.get('type')
    dept_id = request.args.get('department_id')
    min_risk = float(request.args.get('min_risk')) if request.args.get('min_risk') else None
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 25))
    
    result = device_repo.list_devices(
        search=search, status=status, device_type=device_type,
        department_id=dept_id, min_risk=min_risk, page=page, per_page=per_page
    )
    return jsonify({
        'status': 'success',
        'data': {
            'items': [d.to_dict() for d in result['items']],
            'total': result['total'],
            'page': result['page'],
            'pages': result['pages']
        }
    }), 200

@devices_api_bp.route('/summary', methods=['GET'])
@login_required
def get_device_summary():
    stats = device_repo.get_device_summary_stats()
    return jsonify({'status': 'success', 'data': stats}), 200

@devices_api_bp.route('/<device_id>', methods=['GET'])
@login_required
def get_device(device_id):
    device = device_repo.get_by_id(device_id)
    if not device:
        raise NotFoundError('Device not found.')
    return jsonify({'status': 'success', 'data': device.to_dict()}), 200

@devices_api_bp.route('/ip/<path:ip_address>', methods=['GET'])
@login_required
def analyze_ip_endpoint(ip_address):
    analysis = device_service.analyze_ip_address(ip_address)
    return jsonify({'status': 'success', 'data': analysis}), 200

@devices_api_bp.route('', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin')
def create_device():
    data = DeviceCreateSchema.validate(request.get_json() or {})
    user = get_current_user()
    device = device_service.register_device(data, creator_id=user.username if user else 'admin')
    return jsonify({'status': 'success', 'message': 'Device registered successfully.', 'data': device.to_dict()}), 201

@devices_api_bp.route('/<device_id>', methods=['PUT', 'PATCH'])
@login_required
@roles_required('super_admin', 'network_admin')
def update_device(device_id):
    data = request.get_json() or {}
    user = get_current_user()
    device = device_service.update_device(device_id, data, user_id=user.username if user else 'admin')
    return jsonify({'status': 'success', 'message': 'Device updated.', 'data': device.to_dict()}), 200

@devices_api_bp.route('/<device_id>/quarantine', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin', 'security_analyst')
def toggle_device_quarantine(device_id):
    data = request.get_json() or {}
    quarantined = bool(data.get('quarantine', True))
    reason = data.get('reason', 'Administrative quarantine action')
    user = get_current_user()
    device = device_service.toggle_quarantine(device_id, quarantined, reason, user_id=user.username if user else 'admin')
    return jsonify({'status': 'success', 'message': f'Device quarantine state set to {quarantined}.', 'data': device.to_dict()}), 200

@devices_api_bp.route('/export', methods=['GET'])
@login_required
def export_devices():
    result = device_repo.list_devices(page=1, per_page=1000)
    rows = [d.to_dict() for d in result['items']]
    fields = ['id', 'name', 'hostname', 'ip_address', 'mac_address', 'device_type', 'operating_system', 'vendor', 'status', 'risk_score', 'risk_level', 'assigned_user']
    return export_to_csv_response(rows, fields, filename='device_inventory.csv')
