from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from app.repositories.device_repository import DeviceRepository
from app.repositories.audit_repository import AuditRepository
from app.models.device import Device, DeviceInterface, DeviceHistory, DeviceTag
from app.models.organization import Subnet
from app.utils.ip_utils import normalize_mac_address, lookup_mac_vendor, ip_in_subnet
from app.utils.datetime_utils import utc_now
from app.constants import DeviceStatus, DeviceType, RiskLevel, AuditAction
from app.errors.exceptions import NotFoundError, ConflictError, ValidationError

class DeviceService:
    def __init__(self, device_repo: DeviceRepository = None, audit_repo: AuditRepository = None):
        self.device_repo = device_repo or DeviceRepository()
        self.audit_repo = audit_repo or AuditRepository()

    def register_device(self, data: Dict[str, Any], creator_id: str = None) -> Device:
        mac = normalize_mac_address(data.get('mac_address', ''))
        if not mac:
            raise ValidationError('Valid MAC address is required.')
        if self.device_repo.get_by_mac(mac):
            raise ConflictError(f'Device with MAC {mac} is already registered.')

        ip = data.get('ip_address', '').strip()
        vendor = lookup_mac_vendor(mac)
        
        device = Device(
            name=data.get('name', f'Endpoint-{mac[-5:].replace(":", "")}'),
            hostname=data.get('hostname'),
            ip_address=ip,
            mac_address=mac,
            device_type=data.get('device_type', DeviceType.WORKSTATION.value),
            operating_system=data.get('operating_system', 'Unknown OS'),
            os_version=data.get('os_version'),
            vendor=vendor,
            status=data.get('status', DeviceStatus.ONLINE.value),
            department_id=data.get('department_id'),
            site_id=data.get('site_id'),
            subnet_id=data.get('subnet_id'),
            assigned_user=data.get('assigned_user'),
            assigned_email=data.get('assigned_email'),
            is_authorized=bool(data.get('is_authorized', True))
        )
        created = self.device_repo.create(device)
        
        # Log history
        history = DeviceHistory(
            device_id=created.id,
            event_type='DEVICE_REGISTERED',
            new_value=f'IP: {ip}, MAC: {mac}',
            reason='Initial hardware inventory discovery'
        )
        from app.models.base import db
        db.session.add(history)
        db.session.commit()

        self.audit_repo.log_event(
            action=AuditAction.DEVICE_CREATED,
            resource_type='Device',
            username='system' if not creator_id else creator_id,
            resource_id=created.id,
            status='SUCCESS',
            details={'mac': mac, 'ip': ip, 'name': created.name}
        )
        return created

    def update_device(self, device_id: str, data: Dict[str, Any], user_id: str = None) -> Device:
        device = self.device_repo.get_by_id(device_id)
        if not device:
            raise NotFoundError('Device not found.')

        old_status = device.status
        old_ip = device.ip_address

        self.device_repo.update(device, data)

        if 'ip_address' in data and data['ip_address'] != old_ip:
            h = DeviceHistory(device_id=device.id, event_type='IP_CHANGED', old_value=old_ip, new_value=data['ip_address'], reason='DHCP lease renewal')
            from app.models.base import db
            db.session.add(h)
            db.session.commit()

        self.audit_repo.log_event(
            action=AuditAction.DEVICE_UPDATED,
            resource_type='Device',
            username=user_id or 'admin',
            resource_id=device.id,
            status='SUCCESS',
            details={'updated_fields': list(data.keys())}
        )
        return device

    def toggle_quarantine(self, device_id: str, quarantined: bool, reason: str = 'Policy violation', user_id: str = None) -> Device:
        device = self.device_repo.get_by_id(device_id)
        if not device:
            raise NotFoundError('Device not found.')
        
        device.is_quarantined = quarantined
        device.status = DeviceStatus.UNAUTHORIZED.value if quarantined else DeviceStatus.ONLINE.value
        from app.models.base import db
        db.session.commit()

        self.audit_repo.log_event(
            action='device_quarantine_toggled',
            resource_type='Device',
            username=user_id or 'admin',
            resource_id=device.id,
            status='SUCCESS',
            details={'quarantined': quarantined, 'reason': reason}
        )
        return device
