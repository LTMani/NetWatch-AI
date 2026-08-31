from typing import List
from sqlalchemy import desc
from app.models.digital_twin import TwinScenario
from app.models.base import db

class DigitalTwinRepository:
    def list_scenarios(self, limit: int = 15) -> List[TwinScenario]:
        return TwinScenario.query.order_by(desc(TwinScenario.timestamp)).limit(limit).all()

    def save_scenario(self, scenario: TwinScenario) -> TwinScenario:
        db.session.add(scenario)
        db.session.commit()
        return scenario
