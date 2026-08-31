from functools import wraps
from flask import request, g, jsonify, session
from app.utils.crypto import decode_jwt_token
from app.repositories.user_repository import UserRepository
from app.errors.exceptions import AuthenticationError, AuthorizationError

def get_current_user():
    if hasattr(g, 'current_user') and g.current_user:
        return g.current_user

    # 1. Check Session Cookie (for web browser views)
    user_id = session.get('user_id')
    if user_id:
        user = UserRepository().get_by_id(user_id)
        if user and user.is_active:
            g.current_user = user
            return user

    # 2. Check Authorization Header (for REST API calls)
    auth_header = request.headers.get('Authorization', '')
    if auth_header.startswith('Bearer '):
        token = auth_header.split(' ', 1)[1].strip()
        try:
            payload = decode_jwt_token(token)
            user = UserRepository().get_by_id(payload.get('sub'))
            if user and user.is_active:
                g.current_user = user
                return user
        except Exception:
            pass

    return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = get_current_user()
        if not user:
            raise AuthenticationError('Authentication required.')
        return f(*args, **kwargs)
    return decorated_function

def roles_required(*required_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = get_current_user()
            if not user:
                raise AuthenticationError('Authentication required.')
            user_roles = [r.name for r in user.roles]
            # Super admin bypasses all role checks
            if 'super_admin' in user_roles:
                return f(*args, **kwargs)
            if not any(r in user_roles for r in required_roles):
                raise AuthorizationError(f'Access requires one of the following roles: {", ".join(required_roles)}')
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def permissions_required(*required_perms):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = get_current_user()
            if not user:
                raise AuthenticationError('Authentication required.')
            if user.has_role('super_admin'):
                return f(*args, **kwargs)
            for perm in required_perms:
                if not user.has_permission(perm):
                    raise AuthorizationError(f'Missing required permission: {perm}')
            return f(*args, **kwargs)
        return decorated_function
    return decorator
