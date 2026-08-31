from flask import Blueprint, request, jsonify
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
