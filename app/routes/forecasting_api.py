from flask import Blueprint, jsonify
from app.services.forecasting_engine import NetworkCapacityForecastingEngine
from app.repositories.forecasting_repository import ForecastingRepository
from app.middleware.auth_middleware import login_required

forecasting_api_bp = Blueprint('forecasting_api', __name__, url_prefix='/api/v1/forecasting')
forecast_engine = NetworkCapacityForecastingEngine()
forecast_repo = ForecastingRepository()

@forecasting_api_bp.route('/projections', methods=['GET'])
@login_required
def get_forecast_projections():
    forecasts = forecast_engine.generate_capacity_forecasts()
    return jsonify({
        'status': 'success',
        'data': [f.to_dict() for f in forecasts]
    }), 200
