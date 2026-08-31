from flask import Blueprint, request, jsonify
from app.models.base import db
from app.models.data_source import NetworkDataSource
from app.services.discovery_engine import NetworkDiscoveryEngine
from app.middleware.auth_middleware import login_required, roles_required, get_current_user

data_sources_api_bp = Blueprint('data_sources_api', __name__, url_prefix='/api/v1/data-sources')
discovery_engine = NetworkDiscoveryEngine()

@data_sources_api_bp.route('', methods=['GET'])
@login_required
def list_data_sources():
    sources = NetworkDataSource.query.order_by(NetworkDataSource.created_at.desc()).all()
    return jsonify({
        'status': 'success',
        'data': [s.to_dict() for s in sources]
    }), 200

@data_sources_api_bp.route('', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin')
def create_data_source():
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    endpoint = data.get('endpoint_url', '').strip()
    
    if not name or not endpoint:
        return jsonify({'status': 'error', 'message': 'Source Name and Endpoint URL are required.'}), 400

    user = get_current_user()
    src = NetworkDataSource(
        name=name,
        source_type=data.get('source_type', 'ROUTER_CONTROLLER'),
        provider=data.get('provider', 'ubiquiti_unifi'),
        endpoint_url=endpoint,
        host=data.get('host'),
        port=int(data.get('port', 443)),
        auth_type=data.get('auth_type', 'API_TOKEN'),
        encrypted_secret=data.get('secret'),
        description=data.get('description'),
        created_by=user.username if user else 'admin'
    )
    db.session.add(src)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'message': 'Authorized Network Data Source registered successfully.',
        'data': src.to_dict()
    }), 201

@data_sources_api_bp.route('/<source_id>/test', methods=['POST'])
@login_required
def test_data_source(source_id):
    src = NetworkDataSource.query.get(source_id)
    if not src:
        return jsonify({'status': 'error', 'message': 'Data Source not found.'}), 404
    
    from app.services.connectors.connector_factory import NetworkConnectorFactory
    connector = NetworkConnectorFactory.get_connector({
        'name': src.name,
        'source_type': src.source_type,
        'provider': src.provider,
        'endpoint_url': src.endpoint_url,
        'host': src.host,
        'port': src.port,
        'auth_type': src.auth_type
    })
    res = connector.test_connection()
    return jsonify({'status': 'success', 'data': res}), 200

@data_sources_api_bp.route('/<source_id>/sync', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin')
def sync_data_source(source_id):
    src = NetworkDataSource.query.get(source_id)
    if not src:
        return jsonify({'status': 'error', 'message': 'Data Source not found.'}), 404
    
    res = discovery_engine.sync_data_source(src)
    return jsonify({'status': 'success', 'data': res}), 200

@data_sources_api_bp.route('/discover-all', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin')
def trigger_full_discovery():
    res = discovery_engine.discover_all_active_sources()
    return jsonify({'status': 'success', 'data': res}), 200

@data_sources_api_bp.route('/<source_id>', methods=['DELETE'])
@login_required
@roles_required('super_admin', 'network_admin')
def delete_data_source(source_id):
    src = NetworkDataSource.query.get(source_id)
    if not src:
        return jsonify({'status': 'error', 'message': 'Data Source not found.'}), 404
    
    db.session.delete(src)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Data Source removed.'}), 200
