from flask import Blueprint, jsonify
from app.services.dashboard_service import DashboardService
from app.middleware.auth_middleware import login_required

dashboard_api_bp = Blueprint('dashboard_api', __name__, url_prefix='/api/v1/dashboard')
dash_service = DashboardService()

@dashboard_api_bp.route('/summary', methods=['GET'])
@login_required
def get_dashboard_summary():
    data = dash_service.get_executive_summary()
    return jsonify({'status': 'success', 'data': data}), 200
