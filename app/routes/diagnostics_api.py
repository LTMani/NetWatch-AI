from flask import Blueprint, request, jsonify
from app.services.diagnostics_engine import SlowNetworkDiagnosticEngine
from app.repositories.diagnostics_repository import DiagnosticsRepository
from app.middleware.auth_middleware import login_required, get_current_user

diagnostics_api_bp = Blueprint('diagnostics_api', __name__, url_prefix='/api/v1/diagnostics')
diag_engine = SlowNetworkDiagnosticEngine()
diag_repo = DiagnosticsRepository()

@diagnostics_api_bp.route('/run', methods=['POST'])
@login_required
def run_diagnosis_endpoint():
    user = get_current_user()
    scope = (request.get_json() or {}).get('scope', 'Global Gateway')
    session = diag_engine.run_diagnosis(target_scope=scope, initiated_by=user.username if user else 'admin')
    return jsonify({
        'status': 'success',
        'message': 'Diagnostic wizard completed successfully.',
        'data': {
            'session': session.to_dict(),
            'steps': [s.to_dict() for s in session.steps]
        }
    }), 201

@diagnostics_api_bp.route('/sessions', methods=['GET'])
@login_required
def list_diagnostic_sessions():
    sessions = diag_repo.list_recent_sessions(limit=15)
    return jsonify({
        'status': 'success',
        'data': [s.to_dict() for s in sessions]
    }), 200
