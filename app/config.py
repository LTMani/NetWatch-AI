import os
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'netwatch-enterprise-default-session-key-dev-mode-only')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'netwatch-enterprise-jwt-token-secret-dev-mode-only')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES_MINUTES', '60')))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES_DAYS', '30')))
    
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(seconds=int(os.getenv('PERMANENT_SESSION_LIFETIME_SECONDS', '86400')))
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', str(16 * 1024 * 1024)))
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = False
    
    STORAGE_DIR = BASE_DIR / 'storage'
    EXPORTS_DIR = STORAGE_DIR / 'exports'
    BACKUPS_DIR = STORAGE_DIR / 'backups'
    UPLOADS_DIR = STORAGE_DIR / 'uploads'
    
    DEFAULT_ORGANIZATION = os.getenv('DEFAULT_ORGANIZATION_NAME', 'Apex Enterprise Global')
    DEFAULT_SITE = os.getenv('DEFAULT_SITE_NAME', 'Headquarters Primary')
    DEFAULT_OFFICE_START = os.getenv('DEFAULT_OFFICE_START_TIME', '09:00')
    DEFAULT_OFFICE_END = os.getenv('DEFAULT_OFFICE_END_TIME', '18:00')
    DEFAULT_WORK_DAYS = [int(d) for d in os.getenv('DEFAULT_WORK_DAYS', '0,1,2,3,4').split(',')]
    DEFAULT_TIMEZONE = os.getenv('DEFAULT_TIMEZONE', 'UTC')
    
    HEALTH_WEIGHTS = {
        'latency': float(os.getenv('HEALTH_WEIGHT_LATENCY', '0.25')),
        'packet_loss': float(os.getenv('HEALTH_WEIGHT_PACKET_LOSS', '0.25')),
        'jitter': float(os.getenv('HEALTH_WEIGHT_JITTER', '0.15')),
        'bandwidth_saturation': float(os.getenv('HEALTH_WEIGHT_BANDWIDTH_SATURATION', '0.15')),
        'error_rate': float(os.getenv('HEALTH_WEIGHT_ERROR_RATE', '0.10')),
        'link_flap': float(os.getenv('HEALTH_WEIGHT_LINK_FLAP', '0.10'))
    }
    
    ANOMALY_BASELINE_WINDOW_DAYS = int(os.getenv('ANOMALY_BASELINE_WINDOW_DAYS', '30'))
    ANOMALY_Z_SCORE_THRESHOLD = float(os.getenv('ANOMALY_Z_SCORE_THRESHOLD', '3.0'))
    ANOMALY_EWMA_ALPHA = float(os.getenv('ANOMALY_EWMA_ALPHA', '0.2'))
    ANOMALY_ISOLATION_CONTAMINATION = float(os.getenv('ANOMALY_ISOLATION_CONTAMINATION', '0.03'))
    ANOMALY_MIN_SAMPLE_COUNT = int(os.getenv('ANOMALY_MIN_SAMPLE_COUNT', '30'))
    
    RISK_HALF_LIFE_HOURS = float(os.getenv('RISK_DECAY_HALF_LIFE_HOURS', '72.0'))
    
    AI_PROVIDER = os.getenv('AI_PROVIDER', 'deterministic')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    AI_MODEL_NAME = os.getenv('AI_MODEL_NAME', 'gemini-1.5-pro')
    
    AUDIT_LOG_TAMPER_CHECK_ENABLED = os.getenv('AUDIT_LOG_TAMPER_CHECK_ENABLED', 'True').lower() in ('true', '1', 'yes')
    PRIVACY_PAYLOAD_MASKING_ENABLED = os.getenv('PRIVACY_PAYLOAD_MASKING_ENABLED', 'True').lower() in ('true', '1', 'yes')

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SESSION_COOKIE_SECURE = False
    db_path = BASE_DIR / 'instance' / 'netwatch.db'
    db_path.parent.mkdir(parents=True, exist_ok=True)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{db_path.as_posix()}')

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)

class ProductionConfig(BaseConfig):
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
