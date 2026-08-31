from flask import Blueprint, request, jsonify
from app.repositories.user_repository import UserRepository
from app.middleware.auth_middleware import login_required, roles_required, get_current_user
from app.errors.exceptions import NotFoundError, ValidationError

users_api_bp = Blueprint('users_api', __name__, url_prefix='/api/v1/users')
user_repo = UserRepository()

@users_api_bp.route('', methods=['GET'])
@login_required
@roles_required('super_admin', 'network_admin', 'security_analyst')
def list_users():
    search = request.args.get('search')
    role = request.args.get('role')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    result = user_repo.list_users(search=search, role=role, page=page, per_page=per_page)
    return jsonify({
        'status': 'success',
        'data': {
            'items': [u.to_dict() for u in result['items']],
            'total': result['total'],
            'page': result['page'],
            'pages': result['pages']
        }
    }), 200

@users_api_bp.route('/<user_id>', methods=['GET'])
@login_required
def get_user(user_id):
    user = user_repo.get_by_id(user_id)
    if not user:
        raise NotFoundError('User not found.')
    return jsonify({'status': 'success', 'data': user.to_dict()}), 200

@users_api_bp.route('/<user_id>/status', methods=['PATCH'])
@login_required
@roles_required('super_admin')
def toggle_user_status(user_id):
    user = user_repo.get_by_id(user_id)
    if not user:
        raise NotFoundError('User not found.')
    data = request.get_json() or {}
    is_active = data.get('is_active', not user.is_active)
    user_repo.update(user, {'is_active': is_active})
    return jsonify({'status': 'success', 'message': 'User status updated.', 'data': user.to_dict()}), 200

@users_api_bp.route('/roles', methods=['GET'])
@login_required
def list_roles():
    roles = user_repo.list_roles()
    return jsonify({'status': 'success', 'data': [r.to_dict() for r in roles]}), 200
