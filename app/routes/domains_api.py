from flask import Blueprint, request, jsonify
from app.services.domain_engine import DomainClassificationEngine
from app.repositories.domain_repository import DomainRepository
from app.repositories.telemetry_repository import TelemetryRepository
from app.schemas.domain_schemas import DomainFilterRuleSchema
from app.middleware.auth_middleware import login_required, roles_required
from app.models.domain import DomainFilterRule
from app.models.base import db

domains_api_bp = Blueprint('domains_api', __name__, url_prefix='/api/v1/domains')
domain_engine = DomainClassificationEngine()
domain_repo = DomainRepository()
telemetry_repo = TelemetryRepository()

@domains_api_bp.route('/activity', methods=['GET'])
@login_required
def get_domain_activity():
    limit = int(request.args.get('limit', 50))
    dev_id = request.args.get('device_id')
    category = request.args.get('category')
    search = request.args.get('search')
    queries = telemetry_repo.get_recent_dns_queries(limit=limit, device_id=dev_id, category=category, search=search)
    return jsonify({
        'status': 'success',
        'data': [q.to_dict() for q in queries]
    }), 200

@domains_api_bp.route('/top', methods=['GET'])
@login_required
def get_top_domains():
    hours = int(request.args.get('hours', 24))
    limit = int(request.args.get('limit', 10))
    top = telemetry_repo.get_top_domains(hours=hours, limit=limit)
    return jsonify({'status': 'success', 'data': top}), 200

@domains_api_bp.route('/categories', methods=['GET'])
@login_required
def get_categories():
    cats = domain_repo.list_categories()
    distribution = telemetry_repo.get_category_traffic_distribution(hours=24)
    return jsonify({
        'status': 'success',
        'data': {
            'categories': [c.to_dict() for c in cats],
            'distribution': distribution
        }
    }), 200

@domains_api_bp.route('/classify', methods=['POST'])
@login_required
def classify_domain_endpoint():
    data = request.get_json() or {}
    domain = data.get('domain', '')
    cat, score, is_mal, desc = domain_engine.classify_domain(domain)
    return jsonify({
        'status': 'success',
        'data': {
            'domain': domain,
            'category': cat,
            'reputation_score': score,
            'is_malicious': is_mal,
            'source': desc
        }
    }), 200

@domains_api_bp.route('/filter-rules', methods=['GET', 'POST'])
@login_required
@roles_required('super_admin', 'network_admin', 'security_analyst')
def handle_filter_rules():
    if request.method == 'POST':
        data = DomainFilterRuleSchema.validate(request.get_json() or {})
        rule = DomainFilterRule(
            domain_pattern=data['domain_pattern'],
            category=data.get('category'),
            action=data['action'],
            reason=data['reason'],
            is_enabled=data['is_enabled']
        )
        db.session.add(rule)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Domain rule created.', 'data': rule.to_dict()}), 201
    
    rules = domain_repo.list_filter_rules()
    return jsonify({'status': 'success', 'data': [r.to_dict() for r in rules]}), 200
