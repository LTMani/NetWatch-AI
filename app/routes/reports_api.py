from flask import Blueprint, request, jsonify
from app.services.report_generator import ExecutiveReportGenerator
from app.repositories.report_repository import ReportRepository
from app.middleware.auth_middleware import login_required, roles_required, get_current_user

reports_api_bp = Blueprint('reports_api', __name__, url_prefix='/api/v1/reports')
report_gen = ExecutiveReportGenerator()
report_repo = ReportRepository()

@reports_api_bp.route('', methods=['GET'])
@login_required
def list_reports():
    reports = report_repo.list_reports()
    return jsonify({'status': 'success', 'data': [r.to_dict() for r in reports]}), 200

@reports_api_bp.route('/generate', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin', 'auditor')
def trigger_report_generation():
    user = get_current_user()
    report = report_gen.generate_daily_summary(generated_by=user.username if user else 'admin')
    return jsonify({'status': 'success', 'message': 'Report generated successfully.', 'data': report.to_dict()}), 201
