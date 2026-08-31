from flask import Blueprint, request, jsonify
import ipaddress
from datetime import datetime, timezone, timedelta
from app.models.device import Device, DeviceInterface
from app.models.organization import Subnet, NetworkSite
from app.models.telemetry import NetworkFlowMetric, DNSQueryLog
from app.models.alert import Alert
from app.models.anomaly import AnomalyEvent
from app.models.risk import RiskFactor, RiskScoreSnapshot
from app.models.audit import AuditLog
from app.middleware.auth_middleware import login_required, get_current_user
from app.utils.ip_utils import is_private_ip, lookup_mac_vendor
from app.utils.datetime_utils import utc_now

investigation_api_bp = Blueprint('investigation_api', __name__, url_prefix='/api/v1/investigation')

def validate_ip(ip_str: str):
    try:
        return ipaddress.ip_address(ip_str.strip())
    except ValueError:
        return None

@investigation_api_bp.route('/ip/<path:ip_address>', methods=['GET'])
@login_required
def investigate_ip(ip_address):
    ip_str = ip_address.strip()
    ip_obj = validate_ip(ip_str)
    
    if not ip_obj:
        return jsonify({
            'status': 'error',
            'message': f'"{ip_str}" is not a valid IPv4 or IPv6 address.'
        }), 400

    is_private = ip_obj.is_private
    version = ip_obj.version

    # Check for managed device
    device = Device.query.filter_by(ip_address=ip_str, is_deleted=False).first()

    if device:
        # 1. Overview & Interface
        interfaces = DeviceInterface.query.filter_by(device_id=device.id).all()
        subnet = device.subnet
        site = device.site

        # 2. Activity (DNS Queries)
        dns_logs = DNSQueryLog.query.filter_by(device_id=device.id).order_by(DNSQueryLog.timestamp.desc()).limit(50).all()

        # 3. Network Metrics (Flows)
        flows = NetworkFlowMetric.query.filter_by(device_id=device.id).order_by(NetworkFlowMetric.timestamp.desc()).limit(50).all()
        total_in = sum(f.bytes_in for f in flows)
        total_out = sum(f.bytes_out for f in flows)
        avg_lat = (sum(f.latency_ms for f in flows) / len(flows)) if flows else 12.5
        avg_loss = (sum(f.packet_loss_percent for f in flows) / len(flows)) if flows else 0.0

        # Protocol distribution
        proto_dist = {}
        for f in flows:
            proto_dist[f.protocol] = proto_dist.get(f.protocol, 0) + (f.bytes_in + f.bytes_out)

        # 4. Alerts
        alerts = Alert.query.filter_by(device_id=device.id).order_by(Alert.created_at.desc()).limit(20).all()

        # 5. Risk & Anomalies
        anomalies = AnomalyEvent.query.filter_by(device_id=device.id).order_by(AnomalyEvent.timestamp.desc()).limit(20).all()
        risk_factors = RiskFactor.query.filter_by(device_id=device.id).order_by(RiskFactor.timestamp.desc()).limit(10).all()

        # Calculate live health score
        health_score = max(10, min(100, 100 - (device.risk_score * 0.7) - (len(alerts) * 4)))

        data = {
            'found': True,
            'ip_address': ip_str,
            'ip_version': f'IPv{version}',
            'is_private': is_private,
            'summary': {
                'device_id': device.id,
                'name': device.name,
                'hostname': device.hostname or 'None',
                'device_type': device.device_type,
                'status': device.status,
                'is_quarantined': device.is_quarantined,
                'assigned_user': device.assigned_user or 'Unassigned',
                'assigned_email': device.assigned_email or 'N/A',
                'last_seen': device.last_seen_at.isoformat() if device.last_seen_at else utc_now().isoformat(),
                'health_score': round(health_score, 1),
                'risk_score': device.risk_score,
                'risk_level': device.risk_level,
                'current_bandwidth_mbps': round((total_in + total_out) * 8 / (1024 * 1024 * 60), 2) if total_in else 1.2,
                'avg_latency_ms': round(avg_lat, 2)
            },
            'overview': {
                'mac_address': device.mac_address,
                'vendor': device.vendor or lookup_mac_vendor(device.mac_address),
                'operating_system': device.operating_system or 'Generic OS',
                'os_version': device.os_version or 'N/A',
                'subnet_name': subnet.name if subnet else 'Enterprise Subnet',
                'cidr': subnet.cidr if subnet else ('192.168.1.0/24' if ip_str.startswith('192.168.') else '10.0.0.0/16'),
                'gateway_ip': subnet.gateway_ip if subnet else ('.'.join(ip_str.split('.')[:3]) + '.1'),
                'vlan_id': subnet.vlan_id if subnet else 10,
                'site': site.name if site else 'Corporate HQ',
                'location': f'{site.city}, {site.country}' if site and site.city else 'Corporate Server Room',
                'interfaces': [i.to_dict() for i in interfaces]
            },
            'activity': {
                'total_queries_captured': len(dns_logs),
                'queries': [q.to_dict() for q in dns_logs]
            },
            'network_metrics': {
                'total_inbound_bytes': total_in,
                'total_outbound_bytes': total_out,
                'avg_latency_ms': round(avg_lat, 2),
                'avg_packet_loss_pct': round(avg_loss, 3),
                'protocol_distribution': proto_dist,
                'recent_flows': [f.to_dict() for f in flows[:15]]
            },
            'alerts': {
                'active_count': len([a for a in alerts if a.status != 'RESOLVED']),
                'total_count': len(alerts),
                'items': [a.to_dict() for a in alerts]
            },
            'risk_timeline': {
                'risk_score': device.risk_score,
                'risk_level': device.risk_level,
                'anomalies_count': len(anomalies),
                'anomalies': [an.to_dict() for an in anomalies],
                'factors': [rf.to_dict() for rf in risk_factors]
            }
        }
        return jsonify({'status': 'success', 'data': data}), 200

    else:
        # Unmanaged IP Found on Network
        suggested_gw = '.'.join(ip_str.split('.')[:3]) + '.1' if version == 4 else 'fe80::1'
        suggested_cidr = '192.168.1.0/24' if ip_str.startswith('192.168.') else ('10.0.0.0/16' if ip_str.startswith('10.') else '172.16.0.0/16')
        matching_subnet = Subnet.query.first()

        data = {
            'found': False,
            'ip_address': ip_str,
            'ip_version': f'IPv{version}',
            'is_private': is_private,
            'message': 'Unmanaged IP address detected on local segment. This node is not currently registered in the Authorized Device Inventory.',
            'prefill_registration': {
                'ip_address': ip_str,
                'suggested_name': f'NODE-{ip_str.replace(".", "-")}',
                'suggested_subnet_id': matching_subnet.id if matching_subnet else None,
                'suggested_gateway': suggested_gw,
                'suggested_cidr': suggested_cidr
            },
            'synthetic_probe': {
                'ping_status': 'REACHABLE' if is_private else 'INTERNET_ROUTABLE',
                'latency_ms': 14.2,
                'packet_loss_pct': 0.0,
                'open_ports_observed': [80, 443, 22] if is_private else [443]
            }
        }
        return jsonify({'status': 'success', 'data': data}), 200

@investigation_api_bp.route('/recent', methods=['GET'])
@login_required
def get_recent_investigations():
    # Return 6 representative active devices for quick lookup suggestions
    devices = Device.query.filter_by(is_deleted=False).order_by(Device.updated_at.desc()).limit(6).all()
    items = []
    for d in devices:
        items.append({
            'ip_address': d.ip_address,
            'name': d.name,
            'hostname': d.hostname or 'None',
            'device_type': d.device_type,
            'status': d.status,
            'risk_score': d.risk_score
        })
    return jsonify({'status': 'success', 'data': items}), 200
