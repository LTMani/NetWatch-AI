from flask import Blueprint, request, jsonify
from app.services.copilot_engine import GroundedNetworkCopilotEngine
from app.repositories.copilot_repository import CopilotRepository
from app.middleware.auth_middleware import login_required, get_current_user

copilot_api_bp = Blueprint('copilot_api', __name__, url_prefix='/api/v1/copilot')
copilot_engine = GroundedNetworkCopilotEngine()
copilot_repo = CopilotRepository()

@copilot_api_bp.route('/ask', methods=['POST'])
@copilot_api_bp.route('/query', methods=['POST'])
@login_required
def ask_copilot():
    data = request.get_json() or {}
    query = data.get('query', '').strip()
    if not query:
        return jsonify({'status': 'error', 'message': 'Query cannot be empty.'}), 400
    
    user = get_current_user()
    conv_id = data.get('conversation_id')
    result = copilot_engine.process_query(query, conversation_id=conv_id, user_id=user.id if user else None)
    return jsonify({'status': 'success', 'data': result}), 200

@copilot_api_bp.route('/conversations', methods=['GET'])
@login_required
def get_conversations():
    user = get_current_user()
    convs = copilot_repo.list_user_conversations(user_id=user.id if user else None)
    return jsonify({'status': 'success', 'data': [c.to_dict() for c in convs]}), 200
