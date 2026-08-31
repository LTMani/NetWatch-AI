import sys
sys.path.insert(0, '.')
from scripts.writer import write

# Device Schemas
dev_schemas = '''from typing import Dict, Any
from app.errors.exceptions import ValidationError
from app.utils.ip_utils import is_valid_ipv4, normalize_mac_address

class DeviceCreateSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValidationError('Invalid JSON body.')
        name = data.get('name', '').strip()
        mac = normalize_mac_address(data.get('mac_address', ''))
        ip = data.get('ip_address', '').strip()
        
        if not name:
            raise ValidationError('Device name is required.')
        if not mac:
            raise ValidationError('Valid MAC address is required.')
        if ip and not is_valid_ipv4(ip):
            raise ValidationError('Invalid IPv4 address.')
            
        return {
            'name': name,
            'hostname': data.get('hostname'),
            'mac_address': mac,
            'ip_address': ip,
            'device_type': data.get('device_type', 'workstation'),
            'operating_system': data.get('operating_system', 'Unknown OS'),
            'department_id': data.get('department_id'),
            'site_id': data.get('site_id'),
            'subnet_id': data.get('subnet_id'),
            'assigned_user': data.get('assigned_user'),
            'assigned_email': data.get('assigned_email'),
            'is_authorized': bool(data.get('is_authorized', True))
        }
'''
write('app/schemas/device_schemas.py', dev_schemas)

# Telemetry Schemas
tel_schemas = '''from typing import Dict, Any, List
from app.errors.exceptions import ValidationError

class TelemetryBatchSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> List[Dict[str, Any]]:
        if not isinstance(data, dict):
            raise ValidationError('Invalid JSON body.')
        flows = data.get('flows', [])
        if not isinstance(flows, list):
            raise ValidationError('Flows parameter must be a list.')
        if len(flows) > 5000:
            raise ValidationError('Flow batch exceeds maximum size of 5,000 frames.')
        return flows
'''
write('app/schemas/telemetry_schemas.py', tel_schemas)

# Domain Schemas
dom_schemas = '''from typing import Dict, Any
from app.errors.exceptions import ValidationError
from app.utils.validators import validate_domain_name

class DomainFilterRuleSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, Any]:
        pattern = data.get('domain_pattern', '').strip()
        if not pattern:
            raise ValidationError('Domain pattern is required.')
        return {
            'domain_pattern': pattern.lower(),
            'category': data.get('category'),
            'action': data.get('action', 'BLOCK').upper(),
            'reason': data.get('reason', 'Administrative network policy'),
            'is_enabled': bool(data.get('is_enabled', True))
        }
'''
write('app/schemas/domain_schemas.py', dom_schemas)

# Devices API
dev_api = '''from flask import Blueprint, request, jsonify
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
'''
write('app/routes/devices_api.py', dev_api)

# Telemetry API
tel_api = '''from flask import Blueprint, request, jsonify
from app.services.telemetry_service import TelemetryIngestionService
from app.repositories.telemetry_repository import TelemetryRepository
from app.schemas.telemetry_schemas import TelemetryBatchSchema
from app.middleware.auth_middleware import login_required
from app.middleware.rate_limiter import rate_limit

telemetry_api_bp = Blueprint('telemetry_api', __name__, url_prefix='/api/v1/telemetry')
telemetry_service = TelemetryIngestionService()
telemetry_repo = TelemetryRepository()

@telemetry_api_bp.route('/flows/ingest', methods=['POST'])
@rate_limit(max_requests=500, window_seconds=60)
def ingest_flows():
    flows = TelemetryBatchSchema.validate(request.get_json() or {})
    result = telemetry_service.ingest_flow_batch(flows)
    return jsonify(result), 202

@telemetry_api_bp.route('/dns/ingest', methods=['POST'])
@rate_limit(max_requests=500, window_seconds=60)
def ingest_dns():
    data = request.get_json() or {}
    record = telemetry_service.ingest_dns_query(
        device_ip=data.get('device_ip', '127.0.0.1'),
        domain_name=data.get('domain_name', ''),
        query_type=data.get('query_type', 'A'),
        response_code=data.get('response_code', 'NOERROR'),
        response_time_ms=float(data.get('response_time_ms', 10.0))
    )
    return jsonify({'status': 'success', 'data': record.to_dict()}), 201

@telemetry_api_bp.route('/bandwidth', methods=['GET'])
@login_required
def get_bandwidth_telemetry():
    hours = int(request.args.get('hours', 24))
    dev_id = request.args.get('device_id')
    subnet_id = request.args.get('subnet_id')
    metrics = telemetry_repo.get_bandwidth_history(hours=hours, device_id=dev_id, subnet_id=subnet_id)
    return jsonify({
        'status': 'success',
        'count': len(metrics),
        'data': [m.to_dict() for m in metrics]
    }), 200
'''
write('app/routes/telemetry_api.py', tel_api)

# Domains API
dom_api = '''from flask import Blueprint, request, jsonify
from app.services.domain_engine import DomainClassificationEngine
from app.repositories.domain_repository import DomainRepository
from app.repositories.telemetry_repository import TelemetryRepository
from app.schemas.domain_schemas import DomainFilterRuleSchema
from app.middleware.auth_middleware import login_required, roles_required
from app.models.domain import DomainFilterRule
from app.models.base import db

domains_api_bp = Blueprint('domains_api', __name__, url_prefix='/api/v1/domains')
domain_engine = DomainClassificationEngine()
domain_repo = DomainRepository()
telemetry_repo = TelemetryRepository()

@domains_api_bp.route('/activity', methods=['GET'])
@login_required
def get_domain_activity():
    limit = int(request.args.get('limit', 50))
    dev_id = request.args.get('device_id')
    category = request.args.get('category')
    search = request.args.get('search')
    queries = telemetry_repo.get_recent_dns_queries(limit=limit, device_id=dev_id, category=category, search=search)
    return jsonify({
        'status': 'success',
        'data': [q.to_dict() for q in queries]
    }), 200

@domains_api_bp.route('/top', methods=['GET'])
@login_required
def get_top_domains():
    hours = int(request.args.get('hours', 24))
    limit = int(request.args.get('limit', 10))
    top = telemetry_repo.get_top_domains(hours=hours, limit=limit)
    return jsonify({'status': 'success', 'data': top}), 200

@domains_api_bp.route('/categories', methods=['GET'])
@login_required
def get_categories():
    cats = domain_repo.list_categories()
    distribution = telemetry_repo.get_category_traffic_distribution(hours=24)
    return jsonify({
        'status': 'success',
        'data': {
            'categories': [c.to_dict() for c in cats],
            'distribution': distribution
        }
    }), 200

@domains_api_bp.route('/classify', methods=['POST'])
@login_required
def classify_domain_endpoint():
    data = request.get_json() or {}
    domain = data.get('domain', '')
    cat, score, is_mal, desc = domain_engine.classify_domain(domain)
    return jsonify({
        'status': 'success',
        'data': {
            'domain': domain,
            'category': cat,
            'reputation_score': score,
            'is_malicious': is_mal,
            'source': desc
        }
    }), 200

@domains_api_bp.route('/filter-rules', methods=['GET', 'POST'])
@login_required
@roles_required('super_admin', 'network_admin', 'security_analyst')
def handle_filter_rules():
    if request.method == 'POST':
        data = DomainFilterRuleSchema.validate(request.get_json() or {})
        rule = DomainFilterRule(
            domain_pattern=data['domain_pattern'],
            category=data.get('category'),
            action=data['action'],
            reason=data['reason'],
            is_enabled=data['is_enabled']
        )
        db.session.add(rule)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Domain rule created.', 'data': rule.to_dict()}), 201
    
    rules = domain_repo.list_filter_rules()
    return jsonify({'status': 'success', 'data': [r.to_dict() for r in rules]}), 200
'''
write('app/routes/domains_api.py', dom_api)

# Network Overview API
net_api = '''from flask import Blueprint, request, jsonify
from app.models.organization import Organization, NetworkSite, Subnet, Department
from app.models.device import Device
from app.repositories.device_repository import DeviceRepository
from app.middleware.auth_middleware import login_required
from app.models.base import db
from sqlalchemy import func

network_api_bp = Blueprint('network_api', __name__, url_prefix='/api/v1/network')
device_repo = DeviceRepository()

@network_api_bp.route('/overview', methods=['GET'])
@login_required
def get_network_overview():
    sites = NetworkSite.query.filter_by(is_deleted=False).all()
    subnets = Subnet.query.filter_by(is_deleted=False).all()
    departments = Department.query.filter_by(is_deleted=False).all()
    stats = device_repo.get_device_summary_stats()
    
    subnet_utilization = []
    for sn in subnets:
        dev_count = Device.query.filter_by(subnet_id=sn.id, is_deleted=False).count()
        subnet_utilization.append({
            'id': sn.id,
            'name': sn.name,
            'cidr': sn.cidr,
            'gateway_ip': sn.gateway_ip,
            'vlan_id': sn.vlan_id,
            'device_count': dev_count,
            'is_dmz': sn.is_dmz,
            'is_guest': sn.is_guest_network
        })

    return jsonify({
        'status': 'success',
        'data': {
            'sites_count': len(sites),
            'subnets_count': len(subnets),
            'departments_count': len(departments),
            'device_summary': stats,
            'subnets': subnet_utilization
        }
    }), 200

@network_api_bp.route('/subnets', methods=['GET'])
@login_required
def list_subnets():
    subnets = Subnet.query.filter_by(is_deleted=False).all()
    return jsonify({'status': 'success', 'data': [s.to_dict() for s in subnets]}), 200
'''
write('app/routes/network_api.py', net_api)

print('Milestone 2 APIs & Schemas created.')
