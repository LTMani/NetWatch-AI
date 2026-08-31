from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class TwinScenario(BaseModel):
    """Simulated What-If network scenario (e.g. Core Router Outage, 10x Surge)."""
    __tablename__ = 'nw_twin_scenarios'

    name = Column(String(128), nullable=False, index=True)
    description = Column(Text, nullable=False)
    simulation_type = Column(String(32), default='NODE_FAILURE', nullable=False) # NODE_FAILURE, LINK_CUT, DDOS_SURGE, CONFIG_ERROR
    
    baseline_resilience_score = Column(Float, default=95.0, nullable=False)
    simulated_resilience_score = Column(Float, default=65.0, nullable=False)
    impacted_devices_count = Column(Integer, default=0, nullable=False)
    disconnected_subnets_count = Column(Integer, default=0, nullable=False)
    
    cascading_failure_detected = Column(Boolean, default=False, nullable=False)
    failover_path_available = Column(Boolean, default=True, nullable=False)
    
    simulation_results_json = Column(Text, nullable=False)
    mitigation_recommendation = Column(Text, nullable=True)
    executed_by = Column(String(64), default='admin', nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
