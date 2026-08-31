import json
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
        """
        Grounded AI Network Copilot Query Pipeline:
        1. Classifies Natural Language Intent
        2. Retrieves Real Telemetry, Health, Risk & Incident Data
        3. Formulates Synthesized Grounded Response with Metrics & Action Chips
        """
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
            response_text = f'The composite network health score is **{health.overall_score}/100** ({health.health_status.upper()}).\n\n'
            response_text += f'- **Path Latency**: Average round-trip time is {health.avg_latency_ms} ms.\n'
            response_text += f'- **Packet Loss**: {health.avg_packet_loss_pct}% drop rate across active interfaces.\n'
            response_text += f'- **Bandwidth**: Currently utilizing {health.total_bandwidth_mbps} Mbps.\n\n'
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
                response_text = f'Identified **{len(high_risk)} high-risk assets** exceeding security threshold (Score >= 50):\n\n'
                for d in high_risk:
                    response_text += f'- **{d.name}** ({d.ip_address}) -- Risk Score: **{d.risk_score}/100** ({d.risk_level.upper()}) | User: {d.assigned_user or "Unassigned"}\n'
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
                response_text = f'Detected **{len(anoms)} anomalous events** in the last 24-hour window:\n\n'
                for a in anoms:
                    response_text += f'- **{a.anomaly_type.replace("_", " ").title()}** on {a.device.name if a.device else "Subnet"}: {a.description}\n'
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
            
            response_text = f'Current Incident Response Board reports **{len(incidents)} tracked incidents**:\n\n'
            for inc in incidents:
                response_text += f'- **{inc.incident_number}**: {inc.title} -- Status: {inc.status.upper()} | Severity: {inc.severity.upper()}\n'
                
            actions = [
                {'label': 'Open Incident War Room', 'url': '/incidents', 'icon': 'alert-octagon'},
                {'label': 'Review Policies', 'url': '/policies', 'icon': 'file-text'}
            ]

        else:
            intent = 'GENERAL_COPILOT_ASSISTANCE'
            response_text = 'NetWatch AI Copilot is online and monitoring all telemetry streams. You can ask me:\n\n'
            response_text += '- *"Why is the network slow today?"*\n'
            response_text += '- *"Which devices have the highest risk scores?"*\n'
            response_text += '- *"Show recent bandwidth anomalies and spikes."*\n'
            response_text += '- *"What is the status of active incidents?"*'
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
