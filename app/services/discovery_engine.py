from typing import Dict, Any, List
from datetime import datetime, timezone
from app.models.base import db
from app.models.data_source import NetworkDataSource
from app.models.device import Device, DeviceHistory
from app.models.organization import Subnet
from app.services.connectors.connector_factory import NetworkConnectorFactory
from app.utils.datetime_utils import utc_now
from app.utils.ip_utils import normalize_mac_address, lookup_mac_vendor

class NetworkDiscoveryEngine:
    def __init__(self):
        pass

    def sync_data_source(self, source: NetworkDataSource) -> Dict[str, Any]:
        """Runs automated client device discovery for a specific authorized network connector."""
        connector = NetworkConnectorFactory.get_connector({
            'name': source.name,
            'source_type': source.source_type,
            'provider': source.provider,
            'endpoint_url': source.endpoint_url,
            'host': source.host,
            'port': source.port,
            'auth_type': source.auth_type
        })

        try:
            # 1. Test Connectivity
            test_res = connector.test_connection()
            if not test_res.get('success', False):
                source.sync_status = 'FAILED'
                source.sync_message = test_res.get('message', 'Failed to communicate with network source.')
                source.last_sync_at = utc_now()
                db.session.commit()
                return {'success': False, 'message': source.sync_message, 'new_devices': 0, 'updated_devices': 0}

            # 2. Discover Devices
            discovered_raw = connector.discover_connected_devices()
            new_count = 0
            updated_count = 0

            matching_subnet = Subnet.query.first()

            for item in discovered_raw:
                mac = normalize_mac_address(item.get('mac_address', ''))
                if not mac:
                    continue

                ip = item.get('ip_address', '').strip()
                existing = Device.query.filter_by(mac_address=mac).first()

                if existing:
                    # Update dynamic status & telemetry moments
                    existing.ip_address = ip
                    existing.hostname = item.get('hostname') or existing.hostname
                    existing.status = item.get('status', 'online')
                    existing.last_seen_at = utc_now()
                    existing.data_freshness = 'LIVE'
                    existing.data_source_id = source.id
                    updated_count += 1
                else:
                    # Register discovered authorized asset
                    new_dev = Device(
                        name=item.get('name') or f'Endpoint-{mac[-5:].replace(":", "")}',
                        hostname=item.get('hostname'),
                        ip_address=ip,
                        mac_address=mac,
                        device_type=item.get('device_type', 'workstation'),
                        operating_system=item.get('operating_system', 'Generic OS'),
                        vendor=item.get('vendor') or lookup_mac_vendor(mac),
                        status=item.get('status', 'online'),
                        discovery_source=item.get('discovery_source', 'DISCOVERED_ROUTER'),
                        data_source_id=source.id,
                        data_freshness='LIVE',
                        subnet_id=matching_subnet.id if matching_subnet else None,
                        assigned_user=item.get('assigned_user'),
                        assigned_email=item.get('assigned_email'),
                        is_authorized=True,
                        risk_score=15.0,
                        risk_level='LOW'
                    )
                    db.session.add(new_dev)
                    new_count += 1

            source.sync_status = 'SUCCESS'
            source.sync_message = f'Successfully discovered and ingested {len(discovered_raw)} client endpoints.'
            source.last_sync_at = utc_now()
            source.devices_discovered_count = len(discovered_raw)
            db.session.commit()

            return {
                'success': True,
                'message': source.sync_message,
                'new_devices': new_count,
                'updated_devices': updated_count,
                'total_discovered': len(discovered_raw)
            }

        except Exception as e:
            source.sync_status = 'FAILED'
            source.sync_message = str(e)
            source.last_sync_at = utc_now()
            db.session.commit()
            return {'success': False, 'message': str(e), 'new_devices': 0, 'updated_devices': 0}

    def discover_all_active_sources(self) -> Dict[str, Any]:
        """Discovers and updates inventory from all active company data sources."""
        sources = NetworkDataSource.query.filter_by(is_active=True).all()

        if not sources:
            # Seed default enterprise source if none exists yet
            default_src = NetworkDataSource(
                name='Core Gateway & DHCP Lease Ingestion',
                source_type='ROUTER_CONTROLLER',
                provider='ubiquiti_unifi',
                endpoint_url='https://unifi-core.corp.internal:8443',
                host='unifi-core.corp.internal',
                port=8443,
                auth_type='API_TOKEN',
                is_active=True,
                description='Automated authorized enterprise controller client ingestion'
            )
            db.session.add(default_src)
            db.session.commit()
            sources = [default_src]

        total_new = 0
        total_updated = 0
        total_found = 0

        for src in sources:
            res = self.sync_data_source(src)
            total_new += res.get('new_devices', 0)
            total_updated += res.get('updated_devices', 0)
            total_found += res.get('total_discovered', 0)

        return {
            'success': True,
            'active_sources_count': len(sources),
            'new_devices_added': total_new,
            'existing_devices_updated': total_updated,
            'total_nodes_polled': total_found,
            'message': f'Discovered {total_new} new devices, updated {total_updated} active nodes across {len(sources)} data sources.'
        }
