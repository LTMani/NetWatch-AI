from typing import Dict, Any, Optional
from app.errors.exceptions import ValidationError
from app.utils.validators import validate_email, validate_username

class LoginRequestSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, str]:
        if not isinstance(data, dict):
            raise ValidationError('Invalid JSON body.')
        identifier = data.get('identifier') or data.get('username') or data.get('email')
        password = data.get('password')
        if not identifier or not str(identifier).strip():
            raise ValidationError('Username or email is required.')
        if not password or not str(password).strip():
            raise ValidationError('Password is required.')
        return {
            'identifier': str(identifier).strip(),
            'password': str(password).strip(),
            'remember_me': bool(data.get('remember_me', False))
        }

class RegisterRequestSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValidationError('Invalid JSON body.')
        username = validate_username(data.get('username', ''))
        email = validate_email(data.get('email', ''))
        password = data.get('password', '')
        full_name = data.get('full_name', '').strip()
        if not password or len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        if not full_name:
            raise ValidationError('Full name is required.')
        return {
            'username': username,
            'email': email,
            'password': password,
            'full_name': full_name,
            'role': data.get('role', 'security_analyst')
        }

class PasswordChangeSchema:
    @staticmethod
    def validate(data: Dict[str, Any]) -> Dict[str, str]:
        current_password = data.get('current_password', '')
        new_password = data.get('new_password', '')
        if not current_password:
            raise ValidationError('Current password is required.')
        if not new_password or len(new_password) < 8:
            raise ValidationError('New password must be at least 8 characters long.')
        return {
            'current_password': current_password,
            'new_password': new_password
        }
