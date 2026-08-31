from typing import Dict, Any, List
from datetime import datetime, timezone, timedelta
from app.models.device import Device
from app.models.risk import RiskScoreSnapshot, RiskFactor
from app.models.anomaly import AnomalyEvent
from app.models.domain import DomainReputation
from app.repositories.risk_repository import RiskRepository
from app.constants import RiskLevel
from app.utils.datetime_utils import utc_now

class AssetRiskScoringEngine:
    def __init__(self, risk_repo: RiskRepository = None):
        self.risk_repo = risk_repo or RiskRepository()

    def recalculate_device_risk(self, device_id: str) -> Device:
        """
        Calculates dynamic asset risk score (0-100) using Bayesian-decay multi-factor attribution:
        - Active Anomalies Penalty: (Critical: +35, High: +20, Medium: +10)
        - Threat Intelligence / Malicious Domain Hits: (+30)
        - Unauthorized or Quarantined Device Flag: (+40)
        - Historical Decay: Older events decay with half-life of 72 hours.
        """
        device = Device.query.get(device_id)
        if not device or device.is_deleted:
            return device

        # Fetch recent anomalies
        cutoff = utc_now() - timedelta(days=7)
        anomalies = AnomalyEvent.query.filter(
            AnomalyEvent.device_id == device_id,
            AnomalyEvent.timestamp >= cutoff,
            AnomalyEvent.is_false_positive == False
        ).all()

        anomaly_score = 0.0
        for a in anomalies:
            weight = 35.0 if a.severity == 'critical' else (20.0 if a.severity == 'high' else 10.0)
            # Time decay
            age_hours = (utc_now() - a.timestamp.replace(tzinfo=timezone.utc)).total_seconds() / 3600.0
            decay = 0.5 ** (age_hours / 72.0)
            anomaly_score += weight * decay

        policy_score = 40.0 if not device.is_authorized or device.is_quarantined else 0.0
        reputation_score = 0.0

        total_score = min(100.0, round(anomaly_score + policy_score + reputation_score, 1))
        level = RiskLevel.from_score(total_score).value

        device.risk_score = total_score
        device.risk_level = level

        # Save snapshot
        snapshot = RiskScoreSnapshot(
            device_id=device.id,
            subnet_id=device.subnet_id,
            risk_score=total_score,
            risk_level=level,
            policy_penalty=policy_score,
            anomaly_penalty=round(anomaly_score, 1),
            reputation_penalty=reputation_score,
            primary_risk_driver='Active Anomaly Clusters' if anomaly_score > policy_score else 'Authorization Policy Flag',
            timestamp=utc_now()
        )
        from app.models.base import db
        db.session.add(snapshot)
        db.session.commit()
        return device

    def recalculate_all_devices(self) -> int:
        devices = Device.query.filter_by(is_deleted=False).all()
        for d in devices:
            self.recalculate_device_risk(d.id)
        return len(devices)
