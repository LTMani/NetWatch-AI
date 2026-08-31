from typing import List, Optional
from sqlalchemy import desc
from app.models.policy import NetworkPolicy, PolicyViolationEvent
from app.repositories.base_repository import BaseRepository
from app.models.base import db

class PolicyRepository(BaseRepository):
    def __init__(self):
        super().__init__(NetworkPolicy)

    def list_policies(self, enabled_only: bool = False) -> List[NetworkPolicy]:
        query = NetworkPolicy.query.filter_by(is_deleted=False)
        if enabled_only:
            query = query.filter_by(is_enabled=True)
        return query.order_by(desc(NetworkPolicy.created_at)).all()

    def record_violation(self, violation: PolicyViolationEvent):
        db.session.add(violation)
        # Increment policy violation counter
        policy = NetworkPolicy.query.get(violation.policy_id)
        if policy:
            policy.violation_count += 1
            import datetime
            policy.last_triggered_at = datetime.datetime.now(datetime.timezone.utc)
        db.session.commit()
        return violation
