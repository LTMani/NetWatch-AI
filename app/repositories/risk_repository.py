from typing import List, Optional, Dict, Any
from sqlalchemy import desc
from app.models.risk import RiskScoreSnapshot, RiskFactor
from app.models.device import Device
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.constants import RiskLevel

class RiskRepository(BaseRepository):
    def __init__(self):
        super().__init__(RiskScoreSnapshot)

    def get_highest_risk_devices(self, limit: int = 10) -> List[Device]:
        return Device.query.filter(Device.is_deleted == False).order_by(desc(Device.risk_score)).limit(limit).all()

    def get_device_risk_factors(self, device_id: str) -> List[RiskFactor]:
        return RiskFactor.query.filter_by(device_id=device_id).order_by(desc(RiskFactor.score_impact)).all()

    def add_risk_factor(self, factor: RiskFactor):
        db.session.add(factor)
        db.session.commit()
        return factor
