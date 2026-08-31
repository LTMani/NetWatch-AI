import os
from flask import Flask, render_template, session, g
from app.config import config_by_name
from app.models.base import db
from app.errors.handlers import register_error_handlers
from app.middleware.security_headers import add_security_headers
from app.middleware.auth_middleware import get_current_user

def create_app(config_name: str = 'development') -> Flask:
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    # Load configuration
    config_obj = config_by_name.get(config_name, config_by_name['default'])
    app.config.from_object(config_obj)
    
    # Ensure storage directories exist
    os.makedirs(app.config.get('EXPORTS_DIR', 'storage/exports'), exist_ok=True)
    os.makedirs(app.config.get('BACKUPS_DIR', 'storage/backups'), exist_ok=True)
    os.makedirs(app.config.get('UPLOADS_DIR', 'storage/uploads'), exist_ok=True)
    
    # Initialize database
    db.init_app(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Hooks
    @app.before_request
    def load_user_context():
        g.current_user = get_current_user()

    @app.after_request
    def apply_security_headers(response):
        return add_security_headers(response)

    @app.context_processor
    def inject_global_context():
        return {
            'app_name': 'NetWatch AI',
            'app_tagline': 'Watch Smarter. Detect Faster.',
            'app_version': '2.4.0-enterprise',
            'current_user': getattr(g, 'current_user', None)
        }

    # Register Blueprints
    from app.routes.view_routes import views_bp
    from app.routes.auth_api import auth_api_bp
    from app.routes.users_api import users_api_bp
    from app.routes.audit_api import audit_api_bp
    from app.routes.devices_api import devices_api_bp
    from app.routes.telemetry_api import telemetry_api_bp
    from app.routes.domains_api import domains_api_bp
    from app.routes.network_api import network_api_bp
    from app.routes.health_api import health_api_bp
    from app.routes.analytics_api import analytics_api_bp
    from app.routes.dashboard_api import dashboard_api_bp
    from app.routes.diagnostics_api import diagnostics_api_bp
    from app.routes.anomalies_api import anomalies_api_bp
    from app.routes.risk_api import risk_api_bp
    from app.routes.policies_api import policies_api_bp
    from app.routes.alerts_api import alerts_api_bp
    from app.routes.incidents_api import incidents_api_bp
    from app.routes.topology_api import topology_api_bp
    from app.routes.forecasting_api import forecasting_api_bp
    from app.routes.digital_twin_api import digital_twin_api_bp
    from app.routes.copilot_api import copilot_api_bp
    from app.routes.reports_api import reports_api_bp
    from app.routes.settings_api import settings_api_bp
    from app.routes.investigation_api import investigation_api_bp
    from app.routes.data_sources_api import data_sources_api_bp

    app.register_blueprint(views_bp)
    app.register_blueprint(auth_api_bp)
    app.register_blueprint(users_api_bp)
    app.register_blueprint(audit_api_bp)
    app.register_blueprint(devices_api_bp)
    app.register_blueprint(telemetry_api_bp)
    app.register_blueprint(domains_api_bp)
    app.register_blueprint(network_api_bp)
    app.register_blueprint(health_api_bp)
    app.register_blueprint(analytics_api_bp)
    app.register_blueprint(dashboard_api_bp)
    app.register_blueprint(diagnostics_api_bp)
    app.register_blueprint(anomalies_api_bp)
    app.register_blueprint(risk_api_bp)
    app.register_blueprint(policies_api_bp)
    app.register_blueprint(alerts_api_bp)
    app.register_blueprint(incidents_api_bp)
    app.register_blueprint(topology_api_bp)
    app.register_blueprint(forecasting_api_bp)
    app.register_blueprint(digital_twin_api_bp)
    app.register_blueprint(copilot_api_bp)
    app.register_blueprint(reports_api_bp)
    app.register_blueprint(settings_api_bp)
    app.register_blueprint(investigation_api_bp)
    app.register_blueprint(data_sources_api_bp)

    return app
