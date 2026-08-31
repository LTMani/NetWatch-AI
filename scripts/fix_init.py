import sys
sys.path.insert(0, '.')
from scripts.writer import write

write('app/errors/__init__.py', '''from app.errors.exceptions import (
    NetWatchException, ValidationError, AuthenticationError,
    AuthorizationError, NotFoundError, ConflictError,
    RateLimitExceededError, TelemetryIngestionError,
    PrivacyViolationError, EngineExecutionError
)
from app.errors.handlers import register_error_handlers
''')
