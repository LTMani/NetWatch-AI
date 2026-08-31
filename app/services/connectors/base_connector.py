from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BaseNetworkConnector(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.name = config.get('name', 'Generic Connector')
        self.endpoint_url = config.get('endpoint_url', '')
        self.host = config.get('host', '')
        self.port = config.get('port', 443)
        self.auth_type = config.get('auth_type', 'API_TOKEN')

    @abstractmethod
    def test_connection(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def discover_connected_devices(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def ingest_telemetry_moments(self) -> List[Dict[str, Any]]:
        pass
