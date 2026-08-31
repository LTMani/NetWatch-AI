import sys
sys.path.insert(0, '.')
from scripts.writer import write

view_routes = '''from flask import Blueprint, render_template, redirect, url_for, request, session
from app.middleware.auth_middleware import get_current_user
from app.repositories.device_repository import DeviceRepository
from app.repositories.incident_repository import IncidentRepository

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    user = get_current_user()
    if user:
        return redirect(url_for('views.dashboard_view'))
    return render_template('landing.html', title='NetWatch AI -- Watch Smarter. Detect Faster.')

@views_bp.route('/landing')
def landing_view():
    return render_template('landing.html', title='NetWatch AI -- Enterprise Intelligence')

@views_bp.route('/login')
def login_view():
    user = get_current_user()
    if user:
        return redirect(url_for('views.dashboard_view'))
    return render_template('auth/login.html', title='Sign In -- NetWatch AI')

@views_bp.route('/register')
def register_view():
    return render_template('auth/register.html', title='Register User -- NetWatch AI')

@views_bp.route('/dashboard')
def dashboard_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('dashboard/index.html', title='Executive Dashboard -- NetWatch AI', active_page='dashboard')

@views_bp.route('/network/overview')
def network_overview_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('network/overview.html', title='Network Overview -- NetWatch AI', active_page='network')

@views_bp.route('/devices')
def devices_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('devices/list.html', title='Device Inventory -- NetWatch AI', active_page='devices')

@views_bp.route('/devices/<device_id>')
def device_detail_view(device_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    device = DeviceRepository().get_by_id(device_id)
    return render_template('devices/detail.html', device=device, title=f'Device 360: {device.name if device else \"Unknown\"}', active_page='devices')

@views_bp.route('/domains/activity')
def domain_activity_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('domains/activity.html', title='Domain Activity -- NetWatch AI', active_page='domains')

@views_bp.route('/analytics/office-hours')
def office_hours_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('analytics/office_hours.html', title='Office Hours Analytics -- NetWatch AI', active_page='analytics')

@views_bp.route('/analytics/bandwidth')
def bandwidth_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('analytics/bandwidth.html', title='Bandwidth Analytics -- NetWatch AI', active_page='analytics')

@views_bp.route('/health')
def health_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('health/index.html', title='Network Health Engine -- NetWatch AI', active_page='health')

@views_bp.route('/diagnostics/slow-network')
def diagnostics_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('diagnostics/slow_network.html', title='Slow Network Diagnosis -- NetWatch AI', active_page='diagnostics')

@views_bp.route('/anomalies')
def anomalies_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('anomalies/index.html', title='Anomaly Detection Center -- NetWatch AI', active_page='anomalies')

@views_bp.route('/risk')
def risk_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('risk/index.html', title='Asset Risk Posture -- NetWatch AI', active_page='risk')

@views_bp.route('/alerts')
def alerts_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('alerts/index.html', title='Correlated Alerts -- NetWatch AI', active_page='alerts')

@views_bp.route('/incidents')
def incidents_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('incidents/list.html', title='Incident Response Board -- NetWatch AI', active_page='incidents')

@views_bp.route('/incidents/<incident_id>')
def incident_detail_view(incident_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    inc = IncidentRepository().get_by_id(incident_id)
    return render_template('incidents/detail.html', incident=inc, title=f'Incident {inc.incident_number if inc else \"Detail\"}', active_page='incidents')

@views_bp.route('/policies')
def policies_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('policies/index.html', title='Policy Management -- NetWatch AI', active_page='policies')

@views_bp.route('/topology')
def topology_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('topology/index.html', title='Interactive Network Topology -- NetWatch AI', active_page='topology')

@views_bp.route('/copilot')
def copilot_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('copilot/index.html', title='AI Network Copilot -- NetWatch AI', active_page='copilot')

@views_bp.route('/forecasting')
def forecasting_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('forecasting/index.html', title='Capacity Forecasting -- NetWatch AI', active_page='forecasting')

@views_bp.route('/digital-twin')
def digital_twin_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('digital_twin/index.html', title='Digital Twin Scenario Simulator -- NetWatch AI', active_page='digital_twin')

@views_bp.route('/reports')
def reports_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('reports/index.html', title='Executive Reports -- NetWatch AI', active_page='reports')

@views_bp.route('/audit-logs')
def audit_logs_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('audit/index.html', title='Audit Logs & Tamper Trail -- NetWatch AI', active_page='audit')

@views_bp.route('/users')
def users_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('users/index.html', title='User & Access Management -- NetWatch AI', active_page='users')

@views_bp.route('/settings')
def settings_view():
    user = get_current_user()
    if not user:
        return redirect(url_for('views.login_view'))
    return render_template('settings/index.html', title='System Settings & Privacy -- NetWatch AI', active_page='settings')
'''
write('app/routes/view_routes.py', view_routes)

# Update app/__init__.py with all blueprints
app_init = """import os
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

    return app
"""
write('app/__init__.py', app_init)
print('View routes and all blueprints registered in app factory.')
