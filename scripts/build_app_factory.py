import sys
sys.path.insert(0, '.')
from scripts.writer import write

app_init = """import os
from flask import Flask, render_template, session, g
from app.config import config_by_name
from app.models.base import db
from app.errors.handlers import register_error_handlers
from app.middleware.security_headers import add_security_headers
from app.middleware.auth_middleware import get_current_user

def create_app(config_name: str = 'development') -> Flask:
    \"\"\"NetWatch AI Application Factory.\"\"\"
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    # Load configuration
    config_obj = config_by_name.get(config_name, config_by_name['default'])
    app.config.from_object(config_obj)
    
    # Ensure storage directories exist
    os.makedirs(app.config.get('EXPORTS_DIR', 'storage/exports'), exist_ok=True)
    os.makedirs(app.config.get('BACKUPS_DIR', 'storage/backups'), exist_ok=True)
    os.makedirs(app.config.get('UPLOADS_DIR', 'storage/uploads'), exist_ok=True)
    
    # Initialize extensions
    db.init_app(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Request lifecycle hooks
    @app.before_request
    def load_user_context():
        g.current_user = get_current_user()

    @app.after_request
    def apply_security_headers(response):
        return add_security_headers(response)

    # Template context processors
    @app.context_processor
    def inject_global_context():
        return {
            'app_name': 'NetWatch AI',
            'app_tagline': 'Watch Smarter. Detect Faster.',
            'app_version': '2.4.0-enterprise',
            'current_user': getattr(g, 'current_user', None)
        }

    # Register Blueprints
    from app.routes.auth_api import auth_api_bp
    from app.routes.users_api import users_api_bp
    from app.routes.audit_api import audit_api_bp
    
    app.register_blueprint(auth_api_bp)
    app.register_blueprint(users_api_bp)
    app.register_blueprint(audit_api_bp)

    return app
"""
write('app/__init__.py', app_init)
