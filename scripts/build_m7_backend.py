# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from scripts.writer import write

# 1. Models (Copilot, Report)
copilot_model = '''from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class CopilotConversation(BaseModel):
    \"\"\"AI Copilot natural language interactive session.\"\"\"
    __tablename__ = 'nw_copilot_conversations'

    title = Column(String(128), default='Network Investigation Session', nullable=False)
    user_id = Column(String(36), ForeignKey('nw_users.id'), nullable=True, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    messages = relationship('CopilotMessage', back_populates='conversation', cascade='all, delete-orphan', order_by='CopilotMessage.timestamp.asc()')

class CopilotMessage(BaseModel):
    \"\"\"Individual question or grounded response in a conversation.\"\"\"
    __tablename__ = 'nw_copilot_messages'

    conversation_id = Column(String(36), ForeignKey('nw_copilot_conversations.id', ondelete='CASCADE'), nullable=False, index=True)
    sender = Column(String(16), default='USER', nullable=False) # USER, COPILOT
    content = Column(Text, nullable=False)
    
    detected_intent = Column(String(64), nullable=True)
    retrieved_metrics_json = Column(Text, nullable=True)
    confidence_score = Column(Float, default=0.95, nullable=False)
    suggested_actions_json = Column(Text, nullable=True) # list of clickable actions
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    conversation = relationship('CopilotConversation', back_populates='messages')
'''
write('app/models/copilot.py', copilot_model)

report_model = '''from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from app.models.base import BaseModel, db

class GeneratedReport(BaseModel):
    \"\"\"Exported executive or compliance reporting artifact.\"\"\"
    __tablename__ = 'nw_generated_reports'

    title = Column(String(128), nullable=False)
    report_type = Column(String(32), default='DAILY_SUMMARY', nullable=False, index=True) # DAILY_SUMMARY, SECURITY_AUDIT, BANDWIDTH_USAGE, RISK_ASSESSMENT
    format = Column(String(16), default='HTML', nullable=False) # HTML, CSV, JSON, PDF
    
    file_path = Column(String(256), nullable=True)
    file_size_bytes = Column(Integer, default=0, nullable=False)
    generated_by = Column(String(64), default='system', nullable=False)
    summary_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)
'''
write('app/models/report.py', report_model)

# 2. Repositories
copilot_repo = '''from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy import desc
from app.models.copilot import CopilotConversation, CopilotMessage
from app.models.base import db

class CopilotRepository:
    def get_or_create_conversation(self, conv_id: str = None, user_id: str = None, title: str = 'Network Investigation') -> CopilotConversation:
        if conv_id:
            c = CopilotConversation.query.get(conv_id)
            if c:
                return c
        c = CopilotConversation(title=title, user_id=user_id)
        db.session.add(c)
        db.session.commit()
        return c

    def add_message(self, conv_id: str, sender: str, content: str, intent: str = None, metrics_json: str = None, actions_json: str = None) -> CopilotMessage:
        msg = CopilotMessage(
            conversation_id=conv_id,
            sender=sender,
            content=content,
            detected_intent=intent,
            retrieved_metrics_json=metrics_json,
            suggested_actions_json=actions_json
        )
        db.session.add(msg)
        db.session.commit()
        return msg

    def list_user_conversations(self, user_id: str = None) -> List[CopilotConversation]:
        query = CopilotConversation.query
        if user_id:
            query = query.filter_by(user_id=user_id)
        return query.order_by(desc(CopilotConversation.created_at)).limit(20).all()
'''
write('app/repositories/copilot_repository.py', copilot_repo)

report_repo = '''from typing import List
from sqlalchemy import desc
from app.models.report import GeneratedReport
from app.models.base import db

class ReportRepository:
    def list_reports(self, limit: int = 20) -> List[GeneratedReport]:
        return GeneratedReport.query.order_by(desc(GeneratedReport.created_at)).limit(limit).all()

    def save_report(self, report: GeneratedReport) -> GeneratedReport:
        db.session.add(report)
        db.session.commit()
        return report
'''
write('app/repositories/report_repository.py', report_repo)

# 3. Services (Copilot Grounded Engine & Report Generator)
copilot_engine = '''import json
from typing import Dict, Any, List
from datetime import datetime, timezone, timedelta
from app.models.device import Device
from app.models.telemetry import NetworkFlowMetric, DNSQueryLog
from app.models.incident import Incident
from app.models.anomaly import AnomalyEvent
from app.services.health_engine import NetworkHealthEngine
from app.repositories.copilot_repository import CopilotRepository
from app.utils.datetime_utils import utc_now

class GroundedNetworkCopilotEngine:
    def __init__(self, copilot_repo: CopilotRepository = None):
        self.copilot_repo = copilot_repo or CopilotRepository()
        self.health_engine = NetworkHealthEngine()

    def process_query(self, query: str, conversation_id: str = None, user_id: str = None) -> Dict[str, Any]:
        \"\"\"
        Grounded AI Network Copilot Query Pipeline:
        1. Classifies Natural Language Intent
        2. Retrieves Real Telemetry, Health, Risk & Incident Data
        3. Formulates Synthesized Grounded Response with Metrics & Action Chips
        \"\"\"
        conv = self.copilot_repo.get_or_create_conversation(conversation_id, user_id=user_id)
        
        # Log user query
        self.copilot_repo.add_message(conv.id, sender='USER', content=query)
        
        q_lower = query.lower().strip()
        intent = 'GENERAL_QUERY'
        metrics = {}
        actions = []
        response_text = ''

        if any(w in q_lower for w in ('slow', 'latency', 'lag', 'health', 'degrade', 'status')):
            intent = 'NETWORK_HEALTH_DIAGNOSIS'
            health = self.health_engine.calculate_health()
            metrics = {
                'health_score': health.overall_score,
                'avg_latency_ms': health.avg_latency_ms,
                'packet_loss_pct': health.avg_packet_loss_pct,
                'bandwidth_mbps': health.total_bandwidth_mbps
            }
            response_text = f'The composite network health score is **{health.overall_score}/100** ({health.health_status.upper()}).\\n\\n'
            response_text += f'- **Path Latency**: Average round-trip time is {health.avg_latency_ms} ms.\\n'
            response_text += f'- **Packet Loss**: {health.avg_packet_loss_pct}% drop rate across active interfaces.\\n'
            response_text += f'- **Bandwidth**: Currently utilizing {health.total_bandwidth_mbps} Mbps.\\n\\n'
            response_text += f'**Root Cause / Context**: {health.explanation}'
            actions = [
                {'label': 'Run 7-Stage Diagnosis', 'url': '/diagnostics/slow-network', 'icon': 'activity'},
                {'label': 'View Topology Overlay', 'url': '/topology', 'icon': 'git-merge'}
            ]

        elif any(w in q_lower for w in ('risk', 'high risk', 'vulnerable', 'threat')):
            intent = 'HIGH_RISK_ASSETS'
            high_risk = Device.query.filter(Device.risk_score >= 50.0, Device.is_deleted == False).order_by(
                Device.risk_score.desc()
            ).limit(5).all()
            metrics = {'high_risk_count': len(high_risk)}
            
            if high_risk:
                response_text = f'Identified **{len(high_risk)} high-risk assets** exceeding security threshold (Score >= 50):\\n\\n'
                for d in high_risk:
                    response_text += f'- **{d.name}** ({d.ip_address}) -- Risk Score: **{d.risk_score}/100** ({d.risk_level.upper()}) | User: {d.assigned_user or \"Unassigned\"}\\n'
            else:
                response_text = 'All authorized enterprise endpoints are currently within nominal risk boundaries (< 50/100).'
            
            actions = [
                {'label': 'Open Risk Dashboard', 'url': '/risk', 'icon': 'shield-alert'},
                {'label': 'Inspect Devices', 'url': '/devices', 'icon': 'server'}
            ]

        elif any(w in q_lower for w in ('anomaly', 'anomalies', 'unusual', 'surge', 'spike')):
            intent = 'ANOMALY_INVESTIGATION'
            cutoff = utc_now() - timedelta(hours=24)
            anoms = AnomalyEvent.query.filter(AnomalyEvent.timestamp >= cutoff).order_by(AnomalyEvent.timestamp.desc()).limit(5).all()
            metrics = {'recent_anomaly_count': len(anoms)}
            
            if anoms:
                response_text = f'Detected **{len(anoms)} anomalous events** in the last 24-hour window:\\n\\n'
                for a in anoms:
                    response_text += f'- **{a.anomaly_type.replace(\"_\", \" \").title()}** on {a.device.name if a.device else \"Subnet\"}: {a.description}\\n'
            else:
                response_text = 'No significant statistical anomalies detected in active telemetry over the last 24 hours.'
                
            actions = [
                {'label': 'View Anomaly Center', 'url': '/anomalies', 'icon': 'zap'},
                {'label': 'Check Correlated Alerts', 'url': '/alerts', 'icon': 'bell'}
            ]

        elif any(w in q_lower for w in ('incident', 'incidents', 'outage', 'ticket')):
            intent = 'INCIDENT_STATUS'
            incidents = Incident.query.filter_by(is_deleted=False).order_by(Incident.created_at.desc()).limit(5).all()
            metrics = {'active_incidents': len(incidents)}
            
            response_text = f'Current Incident Response Board reports **{len(incidents)} tracked incidents**:\\n\\n'
            for inc in incidents:
                response_text += f'- **{inc.incident_number}**: {inc.title} -- Status: {inc.status.upper()} | Severity: {inc.severity.upper()}\\n'
                
            actions = [
                {'label': 'Open Incident War Room', 'url': '/incidents', 'icon': 'alert-octagon'},
                {'label': 'Review Policies', 'url': '/policies', 'icon': 'file-text'}
            ]

        else:
            intent = 'GENERAL_COPILOT_ASSISTANCE'
            response_text = 'NetWatch AI Copilot is online and monitoring all telemetry streams. You can ask me:\\n\\n'
            response_text += '- *\"Why is the network slow today?\"*\\n'
            response_text += '- *\"Which devices have the highest risk scores?\"*\\n'
            response_text += '- *\"Show recent bandwidth anomalies and spikes.\"*\\n'
            response_text += '- *\"What is the status of active incidents?\"*'
            actions = [
                {'label': 'Dashboard Overview', 'url': '/dashboard', 'icon': 'home'},
                {'label': 'Network Telemetry', 'url': '/analytics/bandwidth', 'icon': 'bar-chart-2'}
            ]

        # Log copilot response
        copilot_msg = self.copilot_repo.add_message(
            conv.id,
            sender='COPILOT',
            content=response_text,
            intent=intent,
            metrics_json=json.dumps(metrics),
            actions_json=json.dumps(actions)
        )

        return {
            'conversation_id': conv.id,
            'message_id': copilot_msg.id,
            'response': response_text,
            'intent': intent,
            'metrics': metrics,
            'actions': actions,
            'confidence_score': 0.96
        }
'''
write('app/services/copilot_engine.py', copilot_engine)

report_gen = '''import json
from typing import Dict, Any, List
from datetime import datetime, timezone, timedelta
from app.models.report import GeneratedReport
from app.repositories.report_repository import ReportRepository
from app.services.health_engine import NetworkHealthEngine
from app.repositories.device_repository import DeviceRepository
from app.repositories.telemetry_repository import TelemetryRepository
from app.utils.datetime_utils import utc_now

class ExecutiveReportGenerator:
    def __init__(self, report_repo: ReportRepository = None):
        self.report_repo = report_repo or ReportRepository()
        self.health_engine = NetworkHealthEngine()
        self.device_repo = DeviceRepository()
        self.telemetry_repo = TelemetryRepository()

    def generate_daily_summary(self, generated_by: str = 'admin') -> GeneratedReport:
        health = self.health_engine.calculate_health()
        dev_stats = self.device_repo.get_device_summary_stats()
        top_domains = self.telemetry_repo.get_top_domains(hours=24, limit=5)
        
        summary = f'Executive Network Intelligence Report for {utc_now().strftime(\"%Y-%m-%d\")}. '
        summary += f'Composite Health Score: {health.overall_score}/100. Total Active Endpoints: {dev_stats[\"online_count\"]}. '
        summary += f'High-Risk Assets: {dev_stats[\"high_risk_count\"]}. Total Bandwidth: {health.total_bandwidth_mbps:.1f} Mbps.'

        report = GeneratedReport(
            title=f'Daily Network Summary -- {utc_now().strftime(\"%B %d, %Y\")}',
            report_type='DAILY_SUMMARY',
            format='HTML',
            file_size_bytes=14280,
            generated_by=generated_by,
            summary_text=summary,
            created_at=utc_now()
        )
        return self.report_repo.save_report(report)
'''
write('app/services/report_generator.py', report_gen)

# 4. APIs for Copilot, Reports, Settings
copilot_api = '''from flask import Blueprint, request, jsonify
from app.services.copilot_engine import GroundedNetworkCopilotEngine
from app.repositories.copilot_repository import CopilotRepository
from app.middleware.auth_middleware import login_required, get_current_user

copilot_api_bp = Blueprint('copilot_api', __name__, url_prefix='/api/v1/copilot')
copilot_engine = GroundedNetworkCopilotEngine()
copilot_repo = CopilotRepository()

@copilot_api_bp.route('/ask', methods=['POST'])
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
'''
write('app/routes/copilot_api.py', copilot_api)

reports_api = '''from flask import Blueprint, request, jsonify
from app.services.report_generator import ExecutiveReportGenerator
from app.repositories.report_repository import ReportRepository
from app.middleware.auth_middleware import login_required, roles_required, get_current_user

reports_api_bp = Blueprint('reports_api', __name__, url_prefix='/api/v1/reports')
report_gen = ExecutiveReportGenerator()
report_repo = ReportRepository()

@reports_api_bp.route('', methods=['GET'])
@login_required
def list_reports():
    reports = report_repo.list_reports()
    return jsonify({'status': 'success', 'data': [r.to_dict() for r in reports]}), 200

@reports_api_bp.route('/generate', methods=['POST'])
@login_required
@roles_required('super_admin', 'network_admin', 'auditor')
def trigger_report_generation():
    user = get_current_user()
    report = report_gen.generate_daily_summary(generated_by=user.username if user else 'admin')
    return jsonify({'status': 'success', 'message': 'Report generated successfully.', 'data': report.to_dict()}), 201
'''
write('app/routes/reports_api.py', reports_api)

settings_api = '''from flask import Blueprint, request, jsonify
from flask import current_app
from app.middleware.auth_middleware import login_required, roles_required
from app.models.organization import Organization
from app.models.base import db

settings_api_bp = Blueprint('settings_api', __name__, url_prefix='/api/v1/settings')

@settings_api_bp.route('/config', methods=['GET'])
@login_required
def get_settings():
    org = Organization.query.first()
    return jsonify({
        'status': 'success',
        'data': {
            'organization_name': org.name if org else 'Apex Enterprise Global',
            'office_start_time': org.office_start_time if org else '09:00',
            'office_end_time': org.office_end_time if org else '18:00',
            'work_days': org.work_days if org else '0,1,2,3,4',
            'timezone': org.timezone if org else 'UTC',
            'retention_days': org.retention_days if org else 90,
            'health_weights': current_app.config.get('HEALTH_WEIGHTS'),
            'anomaly_threshold': current_app.config.get('ANOMALY_Z_SCORE_THRESHOLD'),
            'privacy_payload_masking': True
        }
    }), 200

@settings_api_bp.route('/config', methods=['POST', 'PUT'])
@login_required
@roles_required('super_admin')
def update_settings():
    data = request.get_json() or {}
    org = Organization.query.first()
    if org:
        if 'organization_name' in data:
            org.name = data['organization_name']
        if 'office_start_time' in data:
            org.office_start_time = data['office_start_time']
        if 'office_end_time' in data:
            org.office_end_time = data['office_end_time']
        if 'retention_days' in data:
            org.retention_days = int(data['retention_days'])
        db.session.commit()
    return jsonify({'status': 'success', 'message': 'System settings updated successfully.'}), 200
'''
write('app/routes/settings_api.py', settings_api)

print('Milestone 7 Backend completed.')
