from typing import Dict, Any
from app.errors.exceptions import ValidationError
from app.utils.validators import validate_domain_name

class DomainFilterRuleSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, Any]:
        pattern = data.get('domain_pattern', '').strip()
        if not pattern:
            raise ValidationError('Domain pattern is required.')
        return {
            'domain_pattern': pattern.lower(),
            'category': data.get('category'),
            'action': data.get('action', 'BLOCK').upper(),
            'reason': data.get('reason', 'Administrative network policy'),
            'is_enabled': bool(data.get('is_enabled', True))
        }
