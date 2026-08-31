from flask import Blueprint, request, jsonify
from app.models.policy import NetworkPolicy
from app.repositories.policy_repository import PolicyRepository
from app.middleware.auth_middleware import login_required, roles_required, get_current_user
from app.models.base import db
import json

policies_api_bp = Blueprint('policies_api', __name__, url_prefix='/api/v1/policies')
policy_repo = PolicyRepository()

@policies_api_bp.route('', methods=['GET'])
@login_required
def list_policies():
    policies = policy_repo.list_policies()
    return jsonify({
        'status': 'success',
        'data': [p.to_dict() for p in policies]
    }), 200

@policies_api_bp.route('', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin')
def create_policy():
    data = request.get_json() or {}
    user = get_current_user()
    cond = data.get('condition_json')
    if isinstance(cond, dict):
        cond = json.dumps(cond)
        
    policy = NetworkPolicy(
        name=data['name'],
        description=data.get('description'),
        category=data.get('category', 'BANDWIDTH'),
        severity=data.get('severity', 'high'),
        action=data.get('action', 'create_incident'),
        is_enabled=bool(data.get('is_enabled', True)),
        condition_json=cond or '{"metric": "bytes_out", "operator": ">", "threshold": 100000000}',
        created_by=user.username if user else 'admin'
    )
    db.session.add(policy)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Policy created.', 'data': policy.to_dict()}), 201

@policies_api_bp.route('/<policy_id>/toggle', methods=['PATCH'])
@login_required
@roles_required('super_admin', 'network_admin')
def toggle_policy(policy_id):
    p = policy_repo.get_by_id(policy_id)
    if not p:
        return jsonify({'status': 'error', 'message': 'Policy not found.'}), 404
    p.is_enabled = not p.is_enabled
    db.session.commit()
    return jsonify({'status': 'success', 'message': f'Policy state set to {p.is_enabled}.', 'data': p.to_dict()}), 200
