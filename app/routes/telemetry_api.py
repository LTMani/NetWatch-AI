from flask import Blueprint, request, jsonify
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
