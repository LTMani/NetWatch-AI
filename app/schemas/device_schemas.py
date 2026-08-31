from typing import Dict, Any
from app.errors.exceptions import ValidationError
from app.utils.ip_utils import is_valid_ipv4, normalize_mac_address

class DeviceCreateSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValidationError('Invalid JSON body.')
        name = data.get('name', '').strip()
        mac = normalize_mac_address(data.get('mac_address', ''))
        ip = data.get('ip_address', '').strip()
        
        if not name:
            raise ValidationError('Device name is required.')
        if not mac:
            raise ValidationError('Valid MAC address is required.')
        if ip and not is_valid_ipv4(ip):
            raise ValidationError('Invalid IPv4 address.')
            
        return {
            'name': name,
            'hostname': data.get('hostname'),
            'mac_address': mac,
            'ip_address': ip,
            'device_type': data.get('device_type', 'workstation'),
            'operating_system': data.get('operating_system', 'Unknown OS'),
            'department_id': data.get('department_id'),
            'site_id': data.get('site_id'),
            'subnet_id': data.get('subnet_id'),
            'assigned_user': data.get('assigned_user'),
            'assigned_email': data.get('assigned_email'),
            'is_authorized': bool(data.get('is_authorized', True))
        }
