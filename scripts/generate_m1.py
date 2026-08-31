# -*- coding: utf-8 -*-
"
NetWatch AI - Milestone 1 Generator: Core Architecture, Auth, RBAC, Models, Repositories, Services, APIs.
"
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def write_file(rel_path, content):
    full_path = BASE_DIR / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, w, encoding=utf-8) as f:
        f.write(content.strip() + \n)
    print(f [+] Created {rel_path} ({len(content.splitlines())} lines))

print(=*70)
print(GENERATING MILESTONE 1: CORE ARCHITECTURE & AUTHENTICATION)
print(=*70)

# 1. app/config.py
write_file(app/config.py, '''"
NetWatch AI - Enterprise Configuration Module.
Handles environment-based configuration without storing sensitive credentials in source control.
"
import os
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class BaseConfig:
    "Base application configuration."
    SECRET_KEY = os.getenv('SECRET_KEY', 'netwatch-enterprise-default-session-key-dev-mode-only')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'netwatch-enterprise-jwt-token-secret-dev-mode-only')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES_MINUTES', '60')))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES_DAYS', '30')))
    
    # Session and Cookie Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=int(os.getenv('PERMANENT_SESSION_LIFETIME_SECONDS', '86400')))
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', str(16 * 1024 * 1024)))
    
    # Database Settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = False
    
    # Storage & Exports Directories
    STORAGE_DIR = BASE_DIR / 'storage'
    EXPORTS_DIR = STORAGE_DIR / 'exports'
    BACKUPS_DIR = STORAGE_DIR / 'backups'
    UPLOADS_DIR = STORAGE_DIR / 'uploads'
    
    # Enterprise Metadata Defaults
    DEFAULT_ORGANIZATION = os.getenv('DEFAULT_ORGANIZATION_NAME', 'Apex Enterprise Global')
    DEFAULT_SITE = os.getenv('DEFAULT_SITE_NAME', 'Headquarters Primary')
    DEFAULT_OFFICE_START = os.getenv('DEFAULT_OFFICE_START_TIME', '09:00')
    DEFAULT_OFFICE_END = os.getenv('DEFAULT_OFFICE_END_TIME', '18:00')
    DEFAULT_WORK_DAYS = [int(d) for d in os.getenv('DEFAULT_WORK_DAYS', '0,1,2,3,4').split(',')]
    DEFAULT_TIMEZONE = os.getenv('DEFAULT_TIMEZONE', 'UTC')
    
    # Network Health Calculation Weights (Must sum to 1.0)
    HEALTH_WEIGHTS = {
        'latency': float(os.getenv('HEALTH_WEIGHT_LATENCY', '0.25')),
        'packet_loss': float(os.getenv('HEALTH_WEIGHT_PACKET_LOSS', '0.25')),
        'jitter': float(os.getenv('HEALTH_WEIGHT_JITTER', '0.15')),
        'bandwidth_saturation': float(os.getenv('HEALTH_WEIGHT_BANDWIDTH_SATURATION', '0.15')),
        'error_rate': float(os.getenv('HEALTH_WEIGHT_ERROR_RATE', '0.10')),
        'link_flap': float(os.getenv('HEALTH_WEIGHT_LINK_FLAP', '0.10'))
    }
    
    # Anomaly Detection Parameters
    ANOMALY_BASELINE_WINDOW_DAYS = int(os.getenv('ANOMALY_BASELINE_WINDOW_DAYS', '30'))
    ANOMALY_Z_SCORE_THRESHOLD = float(os.getenv('ANOMALY_Z_SCORE_THRESHOLD', '3.0'))
    ANOMALY_EWMA_ALPHA = float(os.getenv('ANOMALY_EWMA_ALPHA', '0.2'))
    ANOMALY_ISOLATION_CONTAMINATION = float(os.getenv('ANOMALY_ISOLATION_CONTAMINATION', '0.03'))
    ANOMALY_MIN_SAMPLE_COUNT = int(os.getenv('ANOMALY_MIN_SAMPLE_COUNT', '30'))
    
    # Risk Decay Parameters
    RISK_HALF_LIFE_HOURS = float(os.getenv('RISK_DECAY_HALF_LIFE_HOURS', '72.0'))
    
    # AI Network Copilot Mode
    AI_PROVIDER = os.getenv('AI_PROVIDER', 'deterministic')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    AI_MODEL_NAME = os.getenv('AI_MODEL_NAME', 'gemini-1.5-pro')
    
    # Privacy & Integrity Boundaries
    AUDIT_LOG_TAMPER_CHECK_ENABLED = os.getenv('AUDIT_LOG_TAMPER_CHECK_ENABLED', 'True').lower() in ('true', '1', 'yes')
    PRIVACY_PAYLOAD_MASKING_ENABLED = os.getenv('PRIVACY_PAYLOAD_MASKING_ENABLED', 'True').lower() in ('true', '1', 'yes')

class DevelopmentConfig(BaseConfig):
    "Development environment configuration."
    DEBUG = True
    TESTING = False
    SESSION_COOKIE_SECURE = False
    db_path = BASE_DIR / 'instance' / 'netwatch.db'
    db_path.parent.mkdir(parents=True, exist_ok=True)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{db_path.as_posix()}')

class TestingConfig(BaseConfig):
    "Testing environment configuration."
    DEBUG = False
    TESTING = True
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)

class ProductionConfig(BaseConfig):
    "Production enterprise configuration."
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    db_path = BASE_DIR / 'instance' / 'netwatch.db'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{db_path.as_posix()}')

config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
''')

# 2. app/errors/exceptions.py
write_file(app/errors/exceptions.py, '''"
NetWatch AI - Domain Specific Exception Hierarchy.
Provides structured exceptions mapped to meaningful HTTP status codes and error payloads.
"

class NetWatchException(Exception):
    "Base exception for all domain errors within NetWatch AI."
    def __init__(self, message=An internal enterprise error occurred., status_code=500, payload=None, error_code=INTERNAL_ERROR):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}
        self.error_code = error_code

    def to_dict(self):
        rv = dict(self.payload)
        rv[status] = error
        rv[error_code] = self.error_code
        rv[message] = self.message
        return rv

class ValidationError(NetWatchException):
    def __init__(self, message=Validation failed on request payload., payload=None):
        super().__init__(message=message, status_code=400, payload=payload, error_code=VALIDATION_ERROR)

class AuthenticationError(NetWatchException):
    def __init__(self, message=Authentication credentials missing or invalid., payload=None):
        super().__init__(message=message, status_code=401, payload=payload, error_code=AUTHENTICATION_FAILED)

class AuthorizationError(NetWatchException):
    def __init__(self, message=Insufficient privileges to perform this operation., payload=None):
        super().__init__(message=message, status_code=403, payload=payload, error_code=PERMISSION_DENIED)

class NotFoundError(NetWatchException):
    def __init__(self, message=Requested network resource was not found., payload=None):
        super().__init__(message=message, status_code=404, payload=payload, error_code=RESOURCE_NOT_FOUND)

class ConflictError(NetWatchException):
    def __init__(self, message=Resource state conflict detected., payload=None):
        super().__init__(message=message, status_code=409, payload=payload, error_code=RESOURCE_CONFLICT)

class RateLimitExceededError(NetWatchException):
    def __init__(self, message=Rate limit exceeded. Please throttle telemetry requests., payload=None):
        super().__init__(message=message, status_code=429, payload=payload, error_code=RATE_LIMIT_EXCEEDED)

class TelemetryIngestionError(NetWatchException):
    def __init__(self, message=Telemetry frame corrupted or invalid schema format., payload=None):
        super().__init__(message=message, status_code=422, payload=payload, error_code=TELEMETRY_INGESTION_ERROR)

class PrivacyViolationError(NetWatchException):
    def __init__(self, message=Telemetry violates enterprise privacy boundary rules., payload=None):
        super().__init__(message=message, status_code=403, payload=payload, error_code=PRIVACY_BOUNDARY_VIOLATION)

class EngineExecutionError(NetWatchException):
    def __init__(self, message=Diagnostic or intelligence engine failed during computation., payload=None):
        super().__init__(message=message, status_code=500, payload=payload, error_code=ENGINE_EXECUTION_ERROR)
''')

# 3. app/errors/handlers.py
write_file(app/errors/handlers.py, '''"
NetWatch AI - Global HTTP and Exception Handlers.
Formats exceptions as structured JSON for API calls and user-friendly pages for browser navigation.
"
from flask import jsonify, render_template, request
from app.errors.exceptions import NetWatchException

def register_error_handlers(app):
    "Registers unified error handlers on the Flask application."
    
    @app.errorhandler(NetWatchException)
    def handle_netwatch_exception(error):
        if request.path.startswith('/api/') or request.is_json:
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response
        return render_template(
            'errors/error.html',
            error_code=error.error_code,
            status_code=error.status_code,
            message=error.message,
            title=fError {error.status_code}
        ), error.status_code

    @app.errorhandler(400)
    def handle_bad_request(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                status: error,
                error_code: BAD_REQUEST,
                message: getattr(e, 'description', The request could not be parsed by the server.)
            }), 400
        return render_template('errors/400.html', message=getattr(e, 'description', 'Invalid request')), 400

    @app.errorhandler(401)
    def handle_unauthorized(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                status: error,
                error_code: UNAUTHORIZED,
                message: Authentication required to access this resource.
            }), 401
        return render_template('errors/401.html', message=Please sign in to proceed.), 401

    @app.errorhandler(403)
    def handle_forbidden(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                status: error,
                error_code: FORBIDDEN,
                message: You do not have administrative permission for this resource.
            }), 403
        return render_template('errors/403.html', message=Access denied by security policy.), 403

    @app.errorhandler(404)
    def handle_not_found(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                status: error,
                error_code: NOT_FOUND,
                message: Requested endpoint or network resource does not exist.
            }), 404
        return render_template('errors/404.html', message=Resource not found.), 404

    @app.errorhandler(429)
    def handle_too_many_requests(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                status: error,
                error_code: RATE_LIMIT_EXCEEDED,
                message: Too many requests. Please throttle your queries.
            }), 429
        return render_template('errors/429.html', message=Rate limit exceeded.), 429

    @app.errorhandler(500)
    def handle_internal_server_error(e):
        app.logger.error(fUnhandled server error: {e}, exc_info=True)
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                status: error,
                error_code: INTERNAL_SERVER_ERROR,
                message: An unexpected server error occurred. Telemetry recorded for review.
            }), 500
        return render_template('errors/500.html', message=Internal system error occurred.), 500
''')

# 4. app/utils/crypto.py
write_file(app/utils/crypto.py, '''"
NetWatch AI - Cryptographic, Token & Integrity Utilities.
Provides secure password hashing, JWT generation, tamper-proof audit hashing, and API key generation.
"
import hashlib
import hmac
import secrets
import time
from datetime import datetime, timezone
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

def hash_password(password: str) -> str:
    "Hashes a password using scrypt/pbkdf2 with high iteration cost."
    if not password or len(password) < 8:
        raise ValueError(Password must be at least 8 characters long.)
    return generate_password_hash(password, method='scrypt')

def verify_password(password: str, hashed: str) -> bool:
    "Verifies a plain text password against a stored secure hash."
    if not password or not hashed:
        return False
    return check_password_hash(hashed, password)

def generate_jwt_token(user_id: str, email: str, role: str, expires_in_seconds: int = 3600, token_type: str = access) -> str:
    "Generates a cryptographically signed JWT token with standard claims."
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
    "Decodes and validates a signed JWT token."
    secret = current_app.config.get('JWT_SECRET_KEY') or current_app.config.get('SECRET_KEY')
    try:
        return jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise ValueError(JWT token has expired.)
    except jwt.InvalidTokenError as e:
        raise ValueError(fInvalid JWT token: {str(e)})

def generate_api_key(prefix: str = nw_live_) -> str:
    "Generates an enterprise-grade random API key for network telemetry collectors."
    random_bytes = secrets.token_urlsafe(32)
    return f{prefix}{random_bytes}

def calculate_sha256(data: str) -> str:
    "Calculates SHA256 hex digest for a string payload."
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def calculate_audit_chain_hash(previous_hash: str, timestamp: str, action: str, user_id: str, details_json: str) -> str:
    "
    Constructs an immutable cryptographic block hash chaining audit log entries.
    Prevents retrospective tampering or unauthorized record deletion.
    "
    secret = current_app.config.get('SECRET_KEY', 'tamper-proof-audit-key')
    payload = f{previous_hash or '0'*64}|{timestamp}|{action}|{user_id}|{details_json}
    return hmac.new(secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest()
''')

# 5. app/utils/ip_utils.py
write_file(app/utils/ip_utils.py, '''"
NetWatch AI - Enterprise IP & Network Addressing Utilities.
Handles IPv4/IPv6 validation, CIDR ranges, MAC normalization, and RFC1918 private space detection.
"
import ipaddress
import re

OUI_VENDOR_DATABASE = {
    00:50:56: VMware Virtual NIC,
    00:0C:29: VMware Virtual NIC,
    00:1A:11: Google Cloud Interface,
    F0:9F:C2: Ubiquiti Networks,
    00:15:5D: Microsoft Hyper-V,
    00:1B:21: Intel Corporate,
    3C:D9:2B: Hewlett Packard Enterprise,
    00:26:08: Cisco Systems,
    00:24:B2: Cisco Systems,
    D8:67:D9: Dell Inc.,
    B8:27:EB: Raspberry Pi Foundation,
    DC:A6:32: Raspberry Pi Trading,
    70:85:C2: Apple Inc.,
    AC:DE:48: Apple Inc.,
    F4:39:09: Samsung Electronics,
    08:00:27: Oracle VirtualBox
}

def is_valid_ipv4(ip_str: str) -> bool:
    "Validates IPv4 string representation."
    if not ip_str or not isinstance(ip_str, str):
        return False
    try:
        ip = ipaddress.IPv4Address(ip_str.strip())
        return True
    except ipaddress.AddressValueError:
        return False

def is_valid_ipv6(ip_str: str) -> bool:
    "Validates IPv6 string representation."
    if not ip_str or not isinstance(ip_str, str):
        return False
    try:
        ip = ipaddress.IPv6Address(ip_str.strip())
        return True
    except ipaddress.AddressValueError:
        return False

def is_private_ip(ip_str: str) -> bool:
    "Returns True if IP is within RFC 1918 / RFC 4193 private space."
    try:
        ip = ipaddress.ip_address(ip_str.strip())
        return ip.is_private
    except ValueError:
        return False

def is_loopback_ip(ip_str: str) -> bool:
    "Returns True if IP is a loopback address."
    try:
        ip = ipaddress.ip_address(ip_str.strip())
        return ip.is_loopback
    except ValueError:
        return False

def normalize_mac_address(mac_str: str) -> str:
    "Normalizes MAC address to standard colon-delimited uppercase format (AA:BB:CC:DD:EE:FF)."
    if not mac_str or not isinstance(mac_str, str):
        return "
 clean = re.sub(r'[^a-fA-F0-9]', '', mac_str.strip())
 if len(clean) != 12:
 return mac_str.upper()
 return :.join(clean[i:i+2].upper() for i in range(0, 12, 2))

def lookup_mac_vendor(mac_str: str) -> str:
 "Looks up hardware vendor from MAC Organizationally Unique Identifier (OUI)."
 norm = normalize_mac_address(mac_str)
 if len(norm) >= 8:
 prefix = norm[:8]
 return OUI_VENDOR_DATABASE.get(prefix, Enterprise Network Hardware)
 return Unknown Vendor

def parse_cidr_subnet(cidr_str: str):
 "Parses CIDR notation into network object, network address, netmask, and broadcast."
 try:
 net = ipaddress.ip_network(cidr_str.strip(), strict=False)
 return {
 network_address: str(net.network_address),
 netmask: str(net.netmask),
 broadcast_address: str(net.broadcast_address),
 total_hosts: net.num_addresses - 2 if net.num_addresses > 2 else net.num_addresses,
 prefix_length: net.prefixlen,
 is_private: net.is_private
 }
 except ValueError as e:
 raise ValueError(fInvalid CIDR notation '{cidr_str}': {str(e)})

def ip_in_subnet(ip_str: str, cidr_str: str) -> bool:
 "Checks if an IP address belongs to a specified CIDR subnet."
 try:
 ip = ipaddress.ip_address(ip_str.strip())
 net = ipaddress.ip_network(cidr_str.strip(), strict=False)
 return ip in net
 except ValueError:
 return False
''')

# 6. app/utils/datetime_utils.py
write_file(app/utils/datetime_utils.py, '''"
NetWatch AI - Datetime and Business Hours Window Utilities.
Handles UTC conversions, office hours calculation, time bucketing, and human-readable formatters.
"
from datetime import datetime, time, timedelta, timezone

def utc_now() -> datetime:
 "Returns the current timezone-aware UTC datetime."
 return datetime.now(timezone.utc)

def format_iso_utc(dt: datetime) -> str:
 "Formats datetime to standard ISO 8601 UTC string."
 if not dt:
 return 
 if dt.tzinfo is None:
 dt = dt.replace(tzinfo=timezone.utc)
 return dt.astimezone(timezone.utc).isoformat()

def parse_iso_datetime(dt_str: str) -> datetime:
 "Parses ISO 8601 string into a timezone-aware UTC datetime."
 if not dt_str:
 return utc_now()
 dt = datetime.fromisoformat(dt_str.replace(Z, +00:00))
 if dt.tzinfo is None:
 dt = dt.replace(tzinfo=timezone.utc)
 return dt.astimezone(timezone.utc)

def is_within_office_hours(dt: datetime, start_time_str: str = 09:00, end_time_str: str = 18:00, work_days: list = None) -> bool:
 "
 Determines if a given timestamp falls within configured corporate office hours.
 Work days default to Monday(0) through Friday(4).
 "
 if work_days is None:
 work_days = [0, 1, 2, 3, 4]
 
 # Check weekday
 if dt.weekday() not in work_days:
 return False
 
 # Parse start and end times
 start_h, start_m = map(int, start_time_str.split(:))
 end_h, end_m = map(int, end_time_str.split(:))
 
 start_t = time(start_h, start_m)
 end_t = time(end_h, end_m)
 
 current_t = dt.time()
 return start_t <= current_t <= end_t

def get_time_buckets(start_dt: datetime, end_dt: datetime, bucket_minutes: int = 60) -> list:
 "Generates continuous time interval buckets between two dates."
 buckets = []
 current = start_dt
 delta = timedelta(minutes=bucket_minutes)
 while current < end_dt:
 next_dt = min(current + delta, end_dt)
 buckets.append((current, next_dt))
 current = next_dt
 return buckets

def format_relative_time(dt: datetime) -> str:
 "Returns a friendly relative human string (e.g., '2 minutes ago', '3 hours ago')."
 if not dt:
 return never
 now = utc_now()
 if dt.tzinfo is None:
 dt = dt.replace(tzinfo=timezone.utc)
 diff = now - dt
 seconds = int(diff.total_seconds())
 if seconds < 0:
 return just now
 if seconds < 60:
 return f{seconds}s ago if seconds > 5 else just now
 minutes = seconds // 60
 if minutes < 60:
 return f{minutes}m ago
 hours = minutes // 60
 if hours < 24:
 return f{hours}h ago
 days = hours // 24
 if days < 30:
 return f{days}d ago
 months = days // 30
 if months < 12:
 return f{months}mo ago
 years = days // 365
 return f{years}y ago
''')

# 7. app/utils/network_math.py
write_file(app/utils/network_math.py, '''"
NetWatch AI - Network Telemetry Mathematics & Statistics.
Calculates bandwidth rates, statistical deviations, EWMA smoothing, and percentiles.
"
import math
from typing import List, Union

def format_bytes(byte_count: Union[int, float]) -> str:
 "Converts a raw byte count into a human-readable string with units."
 if byte_count is None or byte_count < 0:
 return 0 B
 units = [B, KB, MB, GB, TB, PB]
 val = float(byte_count)
 idx = 0
 while val >= 1024.0 and idx < len(units) - 1:
 val /= 1024.0
 idx += 1
 if idx == 0:
 return f{int(val)} B
 return f{val:.2f} {units[idx]}

def format_bitrate(bps: Union[int, float]) -> str:
 "Converts bits-per-second into human-readable network bandwidth string."
 if bps is None or bps < 0:
 return 0 bps
 units = [bps, Kbps, Mbps, Gbps, Tbps]
 val = float(bps)
 idx = 0
 while val >= 1000.0 and idx < len(units) - 1:
 val /= 1000.0
 idx += 1
 if idx == 0:
 return f{int(val)} bps
 return f{val:.2f} {units[idx]}

def calculate_mean(values: List[float]) -> float:
 "Calculates arithmetic mean of a dataset."
 if not values:
 return 0.0
 return sum(values) / len(values)

def calculate_stddev(values: List[float], mean: float = None) -> float:
 "Calculates sample standard deviation of a dataset."
 if not values or len(values) < 2:
 return 0.0
 if mean is None:
 mean = calculate_mean(values)
 variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
 return math.sqrt(variance)

def calculate_z_score(value: float, mean: float, stddev: float) -> float:
 "Calculates standard score (Z-score) measuring deviations from mean."
 if stddev <= 1e-9:
 return 0.0
 return (value - mean) / stddev

def calculate_ewma(values: List[float], alpha: float = 0.2) -> List[float]:
 "Calculates Exponentially Weighted Moving Average (EWMA) series."
 if not values:
 return []
 ewma_series = [values[0]]
 for v in values[1:]:
 new_ewma = (alpha * v) + ((1.0 - alpha) * ewma_series[-1])
 ewma_series.append(new_ewma)
 return ewma_series

def calculate_percentile(values: List[float], percentile: float) -> float:
 "Calculates the P-th percentile (0 to 100) of a dataset."
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

def calculate_median_absolute_deviation(values: List[float]) -> float:
 "Calculates Median Absolute Deviation (MAD), robust to heavy outliers."
 if not values:
 return 0.0
 median_val = calculate_percentile(values, 50.0)
 abs_deviations = [abs(x - median_val) for x in values]
 return calculate_percentile(abs_deviations, 50.0)
''')

# 8. app/utils/validators.py
write_file(app/utils/validators.py, '''"
NetWatch AI - Input Validation and Sanitization Engine.
Validates enterprise payloads, domain syntax, ports, usernames, and query filters.
"
import re
from app.errors.exceptions import ValidationError

DOMAIN_REGEX = re.compile(
 r'^(?:[a-zA-Z0-9]'
 r'(?:[a-zA-Z0-9-_]{0,61}[a-zA-Z0-9])?\.)+'
 r'[a-zA-Z]{2,63}$'
)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9_.-]{3,32}$')

def validate_domain_name(domain: str) -> str:
 "Validates and normalizes domain name syntax."
 if not domain or not isinstance(domain, str):
 raise ValidationError(Domain name cannot be empty.)
 clean = domain.strip().lower()
 if clean.startswith(http://) or clean.startswith(https://):
 clean = clean.split(://)[1].split(/)[0].split(:)[0]
 if not DOMAIN_REGEX.match(clean) and clean != localhost:
 raise ValidationError(fInvalid domain syntax '{domain}'.)
 return clean

def validate_email(email: str) -> str:
 "Validates and normalizes user email."
 if not email or not isinstance(email, str):
 raise ValidationError(Email address cannot be empty.)
 clean = email.strip().lower()
 if not EMAIL_REGEX.match(clean):
 raise ValidationError(fInvalid email address format '{email}'.)
 return clean

def validate_username(username: str) -> str:
 "Validates username syntax."
 if not username or not isinstance(username, str):
 raise ValidationError(Username cannot be empty.)
 clean = username.strip()
 if not USERNAME_REGEX.match(clean):
 raise ValidationError(Username must be between 3 and 32 characters and contain only alphanumeric, dash, dot, or underscore characters.)
 return clean

def validate_port(port: Union[int, str]) -> int:
 "Validates network port range (1-65535)."
 try:
 p = int(port)
 if not (1 <= p <= 65535):
 raise ValueError()
 return p
 except (ValueError, TypeError):
 raise ValidationError(fNetwork port must be an integer between 1 and 65535, received '{port}'.)

def sanitize_search_query(query: str, max_length: int = 100) -> str:
 "Sanitizes user search strings, stripping dangerous characters."
 if not query or not isinstance(query, str):
 return 
 clean = query.strip()[:max_length]
 # Remove control characters
 return re.sub(r'[\x00-\x1f\x7f]', '', clean)
''')

# 9. app/utils/exporters.py
write_file(app/utils/exporters.py, '''"
NetWatch AI - Structured Data Export Utilities.
Formats telemetry, device lists, alerts, and audit logs into CSV, JSON, or downloadable streams.
"
import csv
import io
import json
from flask import Response, make_response

def export_to_csv_response(rows: list, fieldnames: list, filename: str = export.csv) -> Response:
 "Generates a downloadable CSV attachment response."
 output = io.StringIO()
 writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction='ignore')
 writer.writeheader()
 for row in rows:
 writer.writerow(row)
 
 response = make_response(output.getvalue())
 response.headers[Content-Disposition] = fattachment; filename={filename}
 response.headers[Content-Type] = text/csv; charset=utf-8
 return response

def export_to_json_response(data: dict or list, filename: str = export.json) -> Response:
 "Generates a downloadable formatted JSON attachment response."
 json_str = json.dumps(data, indent=2, default=str)
 response = make_response(json_str)
 response.headers[Content-Disposition] = fattachment; filename={filename}
 response.headers[Content-Type] = application/json; charset=utf-8
 return response
''')

print(Core utilities and configuration written.)
