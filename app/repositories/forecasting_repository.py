from typing import List, Optional
from sqlalchemy import desc
from app.models.forecasting import CapacityForecast
from app.models.base import db

class ForecastingRepository:
    def get_latest_forecasts(self) -> List[CapacityForecast]:
        return CapacityForecast.query.order_by(desc(CapacityForecast.generated_at)).limit(5).all()

    def save_forecast(self, forecast: CapacityForecast) -> CapacityForecast:
        db.session.add(forecast)
        db.session.commit()
        return forecast
