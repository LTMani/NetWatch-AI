from flask import Blueprint, request, jsonify, session
from app.services.auth_service import AuthService
from app.schemas.auth_schemas import LoginRequestSchema, RegisterRequestSchema, PasswordChangeSchema
from app.middleware.auth_middleware import login_required, get_current_user
from app.middleware.rate_limiter import rate_limit

auth_api_bp = Blueprint('auth_api', __name__, url_prefix='/api/v1/auth')
auth_service = AuthService()

@auth_api_bp.route('/login', methods=['POST'])
@rate_limit(max_requests=15, window_seconds=60)
def login():
    data = LoginRequestSchema.validate(request.get_json() or {})
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    result = auth_service.authenticate(data['identifier'], data['password'], ip_address=ip, user_agent=ua)
    
    session['user_id'] = result['user']['id']
    session['username'] = result['user']['username']
    session['role'] = result['user']['primary_role']
    if data['remember_me']:
        session.permanent = True

    return jsonify({
        'status': 'success',
        'message': 'Authentication successful.',
        'data': result
    }), 200

@auth_api_bp.route('/register', methods=['POST'])
@rate_limit(max_requests=10, window_seconds=60)
def register():
    data = RegisterRequestSchema.validate(request.get_json() or {})
    current_user = get_current_user()
    creator_id = current_user.id if current_user else None
    user = auth_service.register(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        full_name=data['full_name'],
        role_name=data['role'],
        creator_id=creator_id
    )
    return jsonify({
        'status': 'success',
        'message': 'User registered successfully.',
        'data': user.to_dict()
    }), 201

@auth_api_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({
        'status': 'success',
        'message': 'Logged out successfully.'
    }), 200

@auth_api_bp.route('/me', methods=['GET'])
@login_required
def get_me():
    user = get_current_user()
    return jsonify({
        'status': 'success',
        'data': user.to_dict()
    }), 200

@auth_api_bp.route('/change-password', methods=['POST'])
@login_required
def change_password():
    user = get_current_user()
    data = PasswordChangeSchema.validate(request.get_json() or {})
    auth_service.change_password(user.id, data['current_password'], data['new_password'])
    session.clear()
    return jsonify({
        'status': 'success',
        'message': 'Password updated successfully. Please log in again.'
    }), 200
