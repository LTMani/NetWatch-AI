class NetWatchException(Exception):
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
