import time
from collections import defaultdict
from functools import wraps
from flask import request
from app.errors.exceptions import RateLimitExceededError

_request_history = defaultdict(list)

def rate_limit(max_requests: int = 60, window_seconds: int = 60):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ip = request.remote_addr or '127.0.0.1'
            now = time.time()
            # Clean expired timestamps
            _request_history[ip] = [ts for ts in _request_history[ip] if now - ts < window_seconds]
            if len(_request_history[ip]) >= max_requests:
                raise RateLimitExceededError(f'Rate limit of {max_requests} requests per {window_seconds}s exceeded.')
            _request_history[ip].append(now)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
