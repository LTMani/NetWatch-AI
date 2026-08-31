import hashlib
import hmac
import secrets
from datetime import datetime, timezone
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

def hash_password(password: str) -> str:
    if not password or len(password) < 8:
        raise ValueError('Password must be at least 8 characters long.')
    return generate_password_hash(password, method='scrypt')

def verify_password(password: str, hashed: str) -> bool:
    if not password or not hashed:
        return False
    return check_password_hash(hashed, password)

def generate_jwt_token(user_id: str, email: str, role: str, expires_in_seconds: int = 3600, token_type: str = 'access') -> str:
    now = datetime.now(timezone.utc)
    secret = current_app.config.get('JWT_SECRET_KEY') or current_app.config.get('SECRET_KEY')
    payload = {
        'sub': user_id,
        'email': email,
        'role': role,
        'type': token_type,
        'iat': int(now.timestamp()),
        'exp': int(now.timestamp()) + expires_in_seconds,
        'jti': secrets.token_hex(16)
    }
    return jwt.encode(payload, secret, algorithm='HS256')

def decode_jwt_token(token: str) -> dict:
    secret = current_app.config.get('JWT_SECRET_KEY') or current_app.config.get('SECRET_KEY')
    try:
        return jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise ValueError('JWT token has expired.')
    except jwt.InvalidTokenError as e:
        raise ValueError(f'Invalid JWT token: {str(e)}')

def generate_api_key(prefix: str = 'nw_live_') -> str:
    random_bytes = secrets.token_urlsafe(32)
    return f'{prefix}{random_bytes}'

def calculate_sha256(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def calculate_audit_chain_hash(previous_hash: str, timestamp: str, action: str, user_id: str, details_json: str) -> str:
    secret = current_app.config.get('SECRET_KEY', 'tamper-proof-audit-key')
    payload = f'{previous_hash or "0"*64}|{timestamp}|{action}|{user_id}|{details_json}'
    return hmac.new(secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest()
