import sys
sys.path.insert(0, '.')
from scripts.writer import write

err_exc = """class NetWatchException(Exception):
    def __init__(self, message='An internal enterprise error occurred.', status_code=500, payload=None, error_code='INTERNAL_ERROR'):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}
        self.error_code = error_code

    def to_dict(self):
        rv = dict(self.payload)
        rv['status'] = 'error'
        rv['error_code'] = self.error_code
        rv['message'] = self.message
        return rv

class ValidationError(NetWatchException):
    def __init__(self, message='Validation failed on request payload.', payload=None):
        super().__init__(message=message, status_code=400, payload=payload, error_code='VALIDATION_ERROR')

class AuthenticationError(NetWatchException):
    def __init__(self, message='Authentication credentials missing or invalid.', payload=None):
        super().__init__(message=message, status_code=401, payload=payload, error_code='AUTHENTICATION_FAILED')

class AuthorizationError(NetWatchException):
    def __init__(self, message='Insufficient privileges to perform this operation.', payload=None):
        super().__init__(message=message, status_code=403, payload=payload, error_code='PERMISSION_DENIED')

class NotFoundError(NetWatchException):
    def __init__(self, message='Requested network resource was not found.', payload=None):
        super().__init__(message=message, status_code=404, payload=payload, error_code='RESOURCE_NOT_FOUND')

class ConflictError(NetWatchException):
    def __init__(self, message='Resource state conflict detected.', payload=None):
        super().__init__(message=message, status_code=409, payload=payload, error_code='RESOURCE_CONFLICT')

class RateLimitExceededError(NetWatchException):
    def __init__(self, message='Rate limit exceeded. Please throttle telemetry requests.', payload=None):
        super().__init__(message=message, status_code=429, payload=payload, error_code='RATE_LIMIT_EXCEEDED')

class TelemetryIngestionError(NetWatchException):
    def __init__(self, message='Telemetry frame corrupted or invalid schema format.', payload=None):
        super().__init__(message=message, status_code=422, payload=payload, error_code='TELEMETRY_INGESTION_ERROR')

class PrivacyViolationError(NetWatchException):
    def __init__(self, message='Telemetry violates enterprise privacy boundary rules.', payload=None):
        super().__init__(message=message, status_code=403, payload=payload, error_code='PRIVACY_BOUNDARY_VIOLATION')

class EngineExecutionError(NetWatchException):
    def __init__(self, message='Diagnostic or intelligence engine failed during computation.', payload=None):
        super().__init__(message=message, status_code=500, payload=payload, error_code='ENGINE_EXECUTION_ERROR')
"""
write('app/errors/exceptions.py', err_exc)

err_handlers = """from flask import jsonify, render_template, request
from app.errors.exceptions import NetWatchException

def register_error_handlers(app):
    @app.errorhandler(NetWatchException)
    def handle_netwatch_exception(error):
        if request.path.startswith('/api/') or request.is_json:
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response
        return render_template(
            'errors/400.html',
            error_code=error.error_code,
            status_code=error.status_code,
            message=error.message,
            title=f'Error {error.status_code}'
        ), error.status_code

    @app.errorhandler(400)
    def handle_bad_request(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'BAD_REQUEST',
                'message': getattr(e, 'description', 'The request could not be parsed by the server.')
            }), 400
        return render_template('errors/400.html', message=getattr(e, 'description', 'Invalid request')), 400

    @app.errorhandler(401)
    def handle_unauthorized(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'UNAUTHORIZED',
                'message': 'Authentication required to access this resource.'
            }), 401
        return render_template('errors/403.html', message='Please sign in to proceed.'), 401

    @app.errorhandler(403)
    def handle_forbidden(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'FORBIDDEN',
                'message': 'You do not have administrative permission for this resource.'
            }), 403
        return render_template('errors/403.html', message='Access denied by security policy.'), 403

    @app.errorhandler(404)
    def handle_not_found(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'NOT_FOUND',
                'message': 'Requested endpoint or network resource does not exist.'
            }), 404
        return render_template('errors/404.html', message='Resource not found.'), 404

    @app.errorhandler(429)
    def handle_too_many_requests(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'RATE_LIMIT_EXCEEDED',
                'message': 'Too many requests. Please throttle your queries.'
            }), 429
        return render_template('errors/400.html', message='Rate limit exceeded.'), 429

    @app.errorhandler(500)
    def handle_internal_server_error(e):
        app.logger.error(f'Unhandled server error: {e}', exc_info=True)
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'INTERNAL_SERVER_ERROR',
                'message': 'An unexpected server error occurred. Telemetry recorded for review.'
            }), 500
        return render_template('errors/500.html', message='Internal system error occurred.'), 500
"""
write('app/errors/handlers.py', err_handlers)
write('app/errors/__init__.py', 'from app.errors.exceptions import *\\nfrom app.errors.handlers import register_error_handlers\\n')

# Utils
utils_crypto = """import hashlib
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
"""
write('app/utils/crypto.py', utils_crypto)

utils_ip = """import ipaddress
import re

OUI_VENDOR_DATABASE = {
    '00:50:56': 'VMware Virtual NIC',
    '00:0C:29': 'VMware Virtual NIC',
    '00:1A:11': 'Google Cloud Interface',
    'F0:9F:C2': 'Ubiquiti Networks',
    '00:15:5D': 'Microsoft Hyper-V',
    '00:1B:21': 'Intel Corporate',
    '3C:D9:2B': 'Hewlett Packard Enterprise',
    '00:26:08': 'Cisco Systems',
    '00:24:B2': 'Cisco Systems',
    'D8:67:D9': 'Dell Inc.',
    'B8:27:EB': 'Raspberry Pi Foundation',
    'DC:A6:32': 'Raspberry Pi Trading',
    '70:85:C2': 'Apple Inc.',
    'AC:DE:48': 'Apple Inc.',
    'F4:39:09': 'Samsung Electronics',
    '08:00:27': 'Oracle VirtualBox'
}

def is_valid_ipv4(ip_str: str) -> bool:
    if not ip_str or not isinstance(ip_str, str):
        return False
    try:
        ipaddress.IPv4Address(ip_str.strip())
        return True
    except ipaddress.AddressValueError:
        return False

def is_valid_ipv6(ip_str: str) -> bool:
    if not ip_str or not isinstance(ip_str, str):
        return False
    try:
        ipaddress.IPv6Address(ip_str.strip())
        return True
    except ipaddress.AddressValueError:
        return False

def is_private_ip(ip_str: str) -> bool:
    try:
        ip = ipaddress.ip_address(ip_str.strip())
        return ip.is_private
    except ValueError:
        return False

def normalize_mac_address(mac_str: str) -> str:
    if not mac_str or not isinstance(mac_str, str):
        return ''
    clean = re.sub(r'[^a-fA-F0-9]', '', mac_str.strip())
    if len(clean) != 12:
        return mac_str.upper()
    return ':'.join(clean[i:i+2].upper() for i in range(0, 12, 2))

def lookup_mac_vendor(mac_str: str) -> str:
    norm = normalize_mac_address(mac_str)
    if len(norm) >= 8:
        prefix = norm[:8]
        return OUI_VENDOR_DATABASE.get(prefix, 'Enterprise Network Hardware')
    return 'Unknown Vendor'

def parse_cidr_subnet(cidr_str: str):
    try:
        net = ipaddress.ip_network(cidr_str.strip(), strict=False)
        return {
            'network_address': str(net.network_address),
            'netmask': str(net.netmask),
            'broadcast_address': str(net.broadcast_address),
            'total_hosts': net.num_addresses - 2 if net.num_addresses > 2 else net.num_addresses,
            'prefix_length': net.prefixlen,
            'is_private': net.is_private
        }
    except ValueError as e:
        raise ValueError(f'Invalid CIDR notation "{cidr_str}": {str(e)}')

def ip_in_subnet(ip_str: str, cidr_str: str) -> bool:
    try:
        ip = ipaddress.ip_address(ip_str.strip())
        net = ipaddress.ip_network(cidr_str.strip(), strict=False)
        return ip in net
    except ValueError:
        return False
"""
write('app/utils/ip_utils.py', utils_ip)

utils_dt = """from datetime import datetime, time, timedelta, timezone

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

def format_iso_utc(dt: datetime) -> str:
    if not dt:
        return ''
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).isoformat()

def parse_iso_datetime(dt_str: str) -> datetime:
    if not dt_str:
        return utc_now()
    dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)

def is_within_office_hours(dt: datetime, start_time_str: str = '09:00', end_time_str: str = '18:00', work_days: list = None) -> bool:
    if work_days is None:
        work_days = [0, 1, 2, 3, 4]
    if dt.weekday() not in work_days:
        return False
    start_h, start_m = map(int, start_time_str.split(':'))
    end_h, end_m = map(int, end_time_str.split(':'))
    start_t = time(start_h, start_m)
    end_t = time(end_h, end_m)
    current_t = dt.time()
    return start_t <= current_t <= end_t

def format_relative_time(dt: datetime) -> str:
    if not dt:
        return 'never'
    now = utc_now()
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    diff = now - dt
    seconds = int(diff.total_seconds())
    if seconds < 0:
        return 'just now'
    if seconds < 60:
        return f'{seconds}s ago' if seconds > 5 else 'just now'
    minutes = seconds // 60
    if minutes < 60:
        return f'{minutes}m ago'
    hours = minutes // 60
    if hours < 24:
        return f'{hours}h ago'
    days = hours // 24
    if days < 30:
        return f'{days}d ago'
    months = days // 30
    if months < 12:
        return f'{months}mo ago'
    years = days // 365
    return f'{years}y ago'
"""
write('app/utils/datetime_utils.py', utils_dt)

utils_math = """import math
from typing import List, Union

def format_bytes(byte_count: Union[int, float]) -> str:
    if byte_count is None or byte_count < 0:
        return '0 B'
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    val = float(byte_count)
    idx = 0
    while val >= 1024.0 and idx < len(units) - 1:
        val /= 1024.0
        idx += 1
    if idx == 0:
        return f'{int(val)} B'
    return f'{val:.2f} {units[idx]}'

def format_bitrate(bps: Union[int, float]) -> str:
    if bps is None or bps < 0:
        return '0 bps'
    units = ['bps', 'Kbps', 'Mbps', 'Gbps', 'Tbps']
    val = float(bps)
    idx = 0
    while val >= 1000.0 and idx < len(units) - 1:
        val /= 1000.0
        idx += 1
    if idx == 0:
        return f'{int(val)} bps'
    return f'{val:.2f} {units[idx]}'

def calculate_mean(values: List[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

def calculate_stddev(values: List[float], mean: float = None) -> float:
    if not values or len(values) < 2:
        return 0.0
    if mean is None:
        mean = calculate_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)

def calculate_z_score(value: float, mean: float, stddev: float) -> float:
    if stddev <= 1e-9:
        return 0.0
    return (value - mean) / stddev

def calculate_ewma(values: List[float], alpha: float = 0.2) -> List[float]:
    if not values:
        return []
    ewma_series = [values[0]]
    for v in values[1:]:
        new_ewma = (alpha * v) + ((1.0 - alpha) * ewma_series[-1])
        ewma_series.append(new_ewma)
    return ewma_series

def calculate_percentile(values: List[float], percentile: float) -> float:
    if not values:
        return 0.0
    sorted_v = sorted(values)
    k = (len(sorted_v) - 1) * (percentile / 100.0)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_v[int(k)]
    d0 = sorted_v[int(f)] * (c - k)
    d1 = sorted_v[int(c)] * (k - f)
    return d0 + d1
"""
write('app/utils/network_math.py', utils_math)

utils_val = """import re
from typing import Union
from app.errors.exceptions import ValidationError

DOMAIN_REGEX = re.compile(r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-_]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9_.-]{3,32}$')

def validate_domain_name(domain: str) -> str:
    if not domain or not isinstance(domain, str):
        raise ValidationError('Domain name cannot be empty.')
    clean = domain.strip().lower()
    if clean.startswith('http://') or clean.startswith('https://'):
        clean = clean.split('://')[1].split('/')[0].split(':')[0]
    if not DOMAIN_REGEX.match(clean) and clean != 'localhost':
        raise ValidationError(f'Invalid domain syntax "{domain}".')
    return clean

def validate_email(email: str) -> str:
    if not email or not isinstance(email, str):
        raise ValidationError('Email address cannot be empty.')
    clean = email.strip().lower()
    if not EMAIL_REGEX.match(clean):
        raise ValidationError(f'Invalid email address format "{email}".')
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
        raise ValidationError(f'Network port must be between 1 and 65535, received "{port}".')

def sanitize_search_query(query: str, max_length: int = 100) -> str:
    if not query or not isinstance(query, str):
        return ''
    clean = query.strip()[:max_length]
    return re.sub(r'[\x00-\x1f\x7f]', '', clean)
"""
write('app/utils/validators.py', utils_val)

utils_exp = """import csv
import io
import json
from flask import Response, make_response

def export_to_csv_response(rows: list, fieldnames: list, filename: str = 'export.csv') -> Response:
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    response.headers['Content-Type'] = 'text/csv; charset=utf-8'
    return response

def export_to_json_response(data, filename: str = 'export.json') -> Response:
    json_str = json.dumps(data, indent=2, default=str)
    response = make_response(json_str)
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response
"""
write('app/utils/exporters.py', utils_exp)
write('app/utils/__init__.py', '''from app.utils.crypto import hash_password, verify_password, generate_jwt_token, decode_jwt_token, generate_api_key, calculate_audit_chain_hash
from app.utils.ip_utils import is_valid_ipv4, is_valid_ipv6, is_private_ip, normalize_mac_address, lookup_mac_vendor, parse_cidr_subnet, ip_in_subnet
from app.utils.datetime_utils import utc_now, format_iso_utc, parse_iso_datetime, is_within_office_hours, format_relative_time
from app.utils.network_math import format_bytes, format_bitrate, calculate_mean, calculate_stddev, calculate_z_score, calculate_ewma, calculate_percentile
from app.utils.validators import validate_domain_name, validate_email, validate_username, validate_port, sanitize_search_query
from app.utils.exporters import export_to_csv_response, export_to_json_response
''')
print('Errors and Utils built successfully.')
