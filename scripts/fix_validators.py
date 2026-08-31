import sys
sys.path.insert(0, '.')
from scripts.writer import write

utils_val = '''import re
from typing import Union
from app.errors.exceptions import ValidationError

DOMAIN_REGEX = re.compile(r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-_]{0,61}[a-zA-Z0-9])?\\.)+[a-zA-Z]{2,63}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9_.-]{3,32}$')

def validate_domain_name(domain: str) -> str:
    if not domain or not isinstance(domain, str):
        raise ValidationError('Domain name cannot be empty.')
    clean = domain.strip().lower()
    if clean.startswith('http://') or clean.startswith('https://'):
        clean = clean.split('://')[1].split('/')[0].split(':')[0]
    if not DOMAIN_REGEX.match(clean) and clean != 'localhost':
        raise ValidationError(f'Invalid domain syntax \"{domain}\".')
    return clean

def validate_email(email: str) -> str:
    if not email or not isinstance(email, str):
        raise ValidationError('Email address cannot be empty.')
    clean = email.strip().lower()
    if not EMAIL_REGEX.match(clean):
        raise ValidationError(f'Invalid email address format \"{email}\".')
    return clean

def validate_username(username: str) -> str:
    if not username or not isinstance(username, str):
        raise ValidationError('Username cannot be empty.')
    clean = username.strip()
    if not USERNAME_REGEX.match(clean):
        raise ValidationError('Username must be between 3 and 32 characters and contain alphanumeric or dash/underscore.')
    return clean

def validate_port(port: Union[int, str]) -> int:
    try:
        p = int(port)
        if not (1 <= p <= 65535):
            raise ValueError()
        return p
    except (ValueError, TypeError):
        raise ValidationError(f'Network port must be between 1 and 65535, received \"{port}\".')

def sanitize_search_query(query: str, max_length: int = 100) -> str:
    if not query or not isinstance(query, str):
        return ''
    clean = query.strip()[:max_length]
    return ''.join(ch for ch in clean if ord(ch) >= 32 and ord(ch) != 127)
'''
write('app/utils/validators.py', utils_val)
