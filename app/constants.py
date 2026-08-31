from enum import Enum

class UserRole(str, Enum):
    SUPER_ADMIN = 'super_admin'
    NETWORK_ADMIN = 'network_admin'
    SECURITY_ANALYST = 'security_analyst'
    AUDITOR = 'auditor'

    @classmethod
    def all_roles(cls):
        return [cls.SUPER_ADMIN, cls.NETWORK_ADMIN, cls.SECURITY_ANALYST, cls.AUDITOR]

    @property
    def display_name(self):
        names = {
            self.SUPER_ADMIN: 'Super Administrator',
            self.NETWORK_ADMIN: 'Network Administrator',
            self.SECURITY_ANALYST: 'Security Analyst',
            self.AUDITOR: 'Auditor'
        }
        return names.get(self, self.value)

class DeviceStatus(str, Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    DEGRADED = 'degraded'
    MAINTENANCE = 'maintenance'
    UNAUTHORIZED = 'unauthorized'

class DeviceType(str, Enum):
    WORKSTATION = 'workstation'
    LAPTOP = 'laptop'
    SERVER = 'server'
    ROUTER = 'router'
    SWITCH = 'switch'
    FIREWALL = 'firewall'
    ACCESS_POINT = 'access_point'
    PRINTER = 'printer'
    IOT_GATEWAY = 'iot_gateway'
    VIRTUAL_MACHINE = 'virtual_machine'

class AlertSeverity(str, Enum):
    CRITICAL = 'critical'
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    INFO = 'info'

    @property
    def score_weight(self):
        weights = {
            self.CRITICAL: 40,
            self.HIGH: 25,
            self.MEDIUM: 15,
            self.LOW: 5,
            self.INFO: 1
        }
        return weights.get(self, 1)

class IncidentStatus(str, Enum):
    OPEN = 'open'
    INVESTIGATING = 'investigating'
    IDENTIFIED = 'identified'
    MONITORING = 'monitoring'
    RESOLVED = 'resolved'
    CLOSED = 'closed'

class IncidentSeverity(str, Enum):
    SEV1_CRITICAL = 'sev1_critical'
    SEV2_HIGH = 'sev2_high'
    SEV3_MEDIUM = 'sev3_medium'
    SEV4_LOW = 'sev4_low'

class RiskLevel(str, Enum):
    CRITICAL = 'critical'
    HIGH = 'high'
    ELEVATED = 'elevated'
    MODERATE = 'moderate'
    LOW = 'low'
    NEGLIGIBLE = 'negligible'

    @classmethod
    def from_score(cls, score: float):
        if score >= 85:
            return cls.CRITICAL
        elif score >= 70:
            return cls.HIGH
        elif score >= 50:
            return cls.ELEVATED
        elif score >= 30:
            return cls.MODERATE
        elif score >= 15:
            return cls.LOW
        return cls.NEGLIGIBLE

class AnomalyType(str, Enum):
    BANDWIDTH_SURGE = 'bandwidth_surge'
    OFF_HOURS_EXFILTRATION = 'off_hours_exfiltration'
    BEACONING_ACTIVITY = 'beaconing_activity'
    DOMAIN_FLAPPING = 'domain_flapping'
    PORT_SCAN_PATTERN = 'port_scan_pattern'
    LATENCY_SPIKE = 'latency_spike'
    PACKET_LOSS_CLUSTER = 'packet_loss_cluster'
    DNS_TUNNEL_SUSPICION = 'dns_tunnel_suspicion'
    UNKNOWN_DEVICE_SURGE = 'unknown_device_surge'

class NetworkProtocol(str, Enum):
    TCP = 'TCP'
    UDP = 'UDP'
    ICMP = 'ICMP'
    HTTP = 'HTTP'
    HTTPS = 'HTTPS'
    DNS = 'DNS'
    SSH = 'SSH'
    RDP = 'RDP'
    SNMP = 'SNMP'
    NTP = 'NTP'
    OTHER = 'OTHER'

class DomainCategoryEnum(str, Enum):
    BUSINESS = 'Business'
    DEVELOPMENT = 'Development'
    DOCUMENTATION = 'Documentation'
    COMMUNICATION = 'Communication'
    CLOUD_SERVICES = 'Cloud Services'
    SOCIAL_MEDIA = 'Social Media'
    ENTERTAINMENT = 'Entertainment'
    STREAMING = 'Streaming'
    NEWS = 'News'
    SHOPPING = 'Shopping'
    GAMING = 'Gaming'
    CRYPTOCURRENCY = 'Cryptocurrency'
    SUSPICIOUS = 'Suspicious'
    MALICIOUS = 'Malicious'
    UNKNOWN = 'Unknown'

class PolicyAction(str, Enum):
    ALERT_ONLY = 'alert_only'
    FLAG_HIGH_RISK = 'flag_high_risk'
    CREATE_INCIDENT = 'create_incident'
    QUARANTINE_RECOMMENDATION = 'quarantine_recommendation'
    THROTTLE_RECOMMENDATION = 'throttle_recommendation'

class HealthStatus(str, Enum):
    OPTIMAL = 'optimal'
    HEALTHY = 'healthy'
    DEGRADED = 'degraded'
    WARNING = 'warning'
    CRITICAL = 'critical'

    @classmethod
    def from_score(cls, score: float):
        if score >= 90:
            return cls.OPTIMAL
        elif score >= 75:
            return cls.HEALTHY
        elif score >= 60:
            return cls.DEGRADED
        elif score >= 40:
            return cls.WARNING
        return cls.CRITICAL

class AuditAction(str, Enum):
    USER_LOGIN = 'user_login'
    USER_LOGOUT = 'user_logout'
    USER_LOGIN_FAILED = 'user_login_failed'
    PASSWORD_CHANGE = 'password_change'
    ROLE_ASSIGNED = 'role_assigned'
    DEVICE_CREATED = 'device_created'
    DEVICE_UPDATED = 'device_updated'
    DEVICE_DECOMMISSIONED = 'device_decommissioned'
    POLICY_CREATED = 'policy_created'
    POLICY_UPDATED = 'policy_updated'
    POLICY_DISABLED = 'policy_disabled'
    INCIDENT_CREATED = 'incident_created'
    INCIDENT_STATUS_CHANGED = 'incident_status_changed'
    DIAGNOSTIC_RUN = 'diagnostic_run'
    DIGITAL_TWIN_SIMULATION = 'digital_twin_simulation'
    SYSTEM_CONFIG_UPDATED = 'system_config_updated'
    REPORT_GENERATED = 'report_generated'

class TopologyNodeType(str, Enum):
    INTERNET = 'internet'
    FIREWALL = 'firewall'
    CORE_ROUTER = 'core_router'
    DISTRIBUTION_SWITCH = 'distribution_switch'
    ACCESS_SWITCH = 'access_switch'
    ACCESS_POINT = 'access_point'
    SERVER = 'server'
    WORKSTATION = 'workstation'
    GATEWAY = 'gateway'
