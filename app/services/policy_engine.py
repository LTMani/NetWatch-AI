import json
from typing import List, Dict, Any
from app.models.policy import NetworkPolicy, PolicyViolationEvent
from app.models.telemetry import NetworkFlowMetric, DNSQueryLog
from app.models.alert import Alert
from app.repositories.policy_repository import PolicyRepository
from app.constants import PolicyAction, AlertSeverity
from app.utils.datetime_utils import utc_now
from app.models.base import db

class PolicyExecutionEngine:
    def __init__(self, policy_repo: PolicyRepository = None):
        self.policy_repo = policy_repo or PolicyRepository()

    def evaluate_flow(self, flow: NetworkFlowMetric) -> List[PolicyViolationEvent]:
        """Evaluates active network policies against ingested flow metric."""
        violations = []
        policies = self.policy_repo.list_policies(enabled_only=True)

        for policy in policies:
            try:
                cond = json.loads(policy.condition_json) if isinstance(policy.condition_json, str) else policy.condition_json
            except Exception:
                continue

            metric = cond.get('metric', 'bytes_out')
            operator = cond.get('operator', '>')
            threshold = cond.get('threshold', 100_000_000)

            val = getattr(flow, metric, 0)
            triggered = False
            if operator == '>' and val > threshold:
                triggered = True
            elif operator == '>=' and val >= threshold:
                triggered = True

            if triggered:
                v = PolicyViolationEvent(
                    policy_id=policy.id,
                    device_id=flow.device_id,
                    severity=policy.severity,
                    violation_details=f'Policy "{policy.name}" violated: {metric}={val} {operator} {threshold}.',
                    observed_value=str(val),
                    timestamp=utc_now()
                )
                self.policy_repo.record_violation(v)
                violations.append(v)

                # Generate alert if required
                alert = Alert(
                    title=f'Policy Breach: {policy.name}',
                    category='POLICY',
                    severity=policy.severity,
                    device_id=flow.device_id,
                    subnet_id=flow.subnet_id,
                    source='PolicyEngine',
                    message=f'Device breached enterprise rule {policy.name}. Observed: {val}.',
                    timestamp=utc_now()
                )
                db.session.add(alert)
                db.session.commit()

        return violations
