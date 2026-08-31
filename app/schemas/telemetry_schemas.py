from typing import Dict, Any, List
from app.errors.exceptions import ValidationError

class TelemetryBatchSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> List[Dict[str, Any]]:
        if not isinstance(data, dict):
            raise ValidationError('Invalid JSON body.')
        flows = data.get('flows', [])
        if not isinstance(flows, list):
            raise ValidationError('Flows parameter must be a list.')
        if len(flows) > 5000:
            raise ValidationError('Flow batch exceeds maximum size of 5,000 frames.')
        return flows
