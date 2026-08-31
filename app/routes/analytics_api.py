from flask import Blueprint, request, jsonify
from app.services.office_hours_service import OfficeHoursAnalyticsService
from app.services.bandwidth_service import BandwidthAnalyticsService
from app.middleware.auth_middleware import login_required

analytics_api_bp = Blueprint('analytics_api', __name__, url_prefix='/api/v1/analytics')
office_service = OfficeHoursAnalyticsService()
bw_service = BandwidthAnalyticsService()

@analytics_api_bp.route('/office-hours', methods=['GET'])
@login_required
def get_office_hours_analytics():
    days = int(request.args.get('days', 7))
    data = office_service.get_activity_comparison(days=days)
    return jsonify({'status': 'success', 'data': data}), 200

@analytics_api_bp.route('/bandwidth', methods=['GET'])
@login_required
def get_bandwidth_analytics():
    hours = int(request.args.get('hours', 24))
    data = bw_service.get_bandwidth_overview(hours=hours)
    return jsonify({'status': 'success', 'data': data}), 200
