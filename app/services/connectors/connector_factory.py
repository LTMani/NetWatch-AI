from typing import Dict, Any
from app.services.connectors.base_connector import BaseNetworkConnector
from app.services.connectors.router_controller_connector import RouterControllerConnector
from app.services.connectors.dhcp_lease_connector import DHCPLeaseConnector
from app.services.connectors.snmp_collector_connector import SNMPCollectorConnector

class NetworkConnectorFactory:
    @staticmethod
    def get_connector(config: Dict[str, Any]) -> BaseNetworkConnector:
        stype = config.get('source_type', '').upper()
        if 'ROUTER' in stype or 'CONTROLLER' in stype or 'UNIFI' in stype or 'MERAKI' in stype:
            return RouterControllerConnector(config)
        elif 'DHCP' in stype or 'LEASE' in stype:
            return DHCPLeaseConnector(config)
        elif 'SNMP' in stype or 'SWITCH' in stype:
            return SNMPCollectorConnector(config)
        else:
            return RouterControllerConnector(config)
