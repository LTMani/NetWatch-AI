from typing import List, Optional, Dict, Any
from sqlalchemy import or_, desc, func
from app.models.device import Device, DeviceInterface, DeviceHistory, DeviceTag
from app.models.organization import Subnet, Department
from app.repositories.base_repository import BaseRepository
from app.models.base import db
from app.utils.datetime_utils import utc_now

class DeviceRepository(BaseRepository):
    def __init__(self):
        super().__init__(Device)

    def get_by_mac(self, mac_address: str) -> Optional[Device]:
        return self.model.query.filter_by(mac_address=mac_address.upper(), is_deleted=False).first()

    def get_by_ip(self, ip_address: str) -> Optional[Device]:
        return self.model.query.filter_by(ip_address=ip_address.strip(), is_deleted=False).first()

    def list_devices(self, search: str = None, status: str = None, device_type: str = None,
                     department_id: str = None, subnet_id: str = None, min_risk: float = None,
                     page: int = 1, per_page: int = 25):
        query = self.model.query.filter_by(is_deleted=False)
        if search:
            s = f'%{search.strip()}%'
            query = query.filter(or_(
                self.model.name.ilike(s),
                self.model.hostname.ilike(s),
                self.model.ip_address.ilike(s),
                self.model.mac_address.ilike(s),
                self.model.assigned_user.ilike(s)
            ))
        if status:
            query = query.filter_by(status=status)
        if device_type:
            query = query.filter_by(device_type=device_type)
        if department_id:
            query = query.filter_by(department_id=department_id)
        if subnet_id:
            query = query.filter_by(subnet_id=subnet_id)
        if min_risk is not None:
            query = query.filter(self.model.risk_score >= min_risk)
        
        pagination = query.order_by(desc(self.model.risk_score), desc(self.model.last_seen_at)).paginate(page=page, per_page=per_page, error_out=False)
        return {
            'items': pagination.items,
            'total': pagination.total,
            'page': pagination.page,
            'per_page': pagination.per_page,
            'pages': pagination.pages
        }

    def get_device_summary_stats(self) -> Dict[str, Any]:
        total = self.model.query.filter_by(is_deleted=False).count()
        online = self.model.query.filter_by(status='online', is_deleted=False).count()
        offline = self.model.query.filter_by(status='offline', is_deleted=False).count()
        degraded = self.model.query.filter_by(status='degraded', is_deleted=False).count()
        high_risk = self.model.query.filter(self.model.risk_score >= 70.0, self.model.is_deleted == False).count()
        unauthorized = self.model.query.filter_by(is_authorized=False, is_deleted=False).count()
        
        # Type breakdown
        type_counts = db.session.query(
            Device.device_type, func.count(Device.id)
        ).filter_by(is_deleted=False).group_by(Device.device_type).all()
        
        return {
            'total_devices': total,
            'online_count': online,
            'offline_count': offline,
            'degraded_count': degraded,
            'high_risk_count': high_risk,
            'unauthorized_count': unauthorized,
            'type_breakdown': {t: count for t, count in type_counts}
        }

    def update_last_seen(self, device_id: str):
        device = self.get_by_id(device_id)
        if device:
            device.last_seen_at = utc_now()
            db.session.commit()
