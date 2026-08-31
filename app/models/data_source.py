from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class NetworkDataSource(BaseModel):
    __tablename__ = 'nw_data_sources'

    name = Column(String(128), nullable=False, index=True)
    source_type = Column(String(64), default='ROUTER_CONTROLLER', nullable=False, index=True)
    provider = Column(String(64), default='ubiquiti_unifi', nullable=False)
    endpoint_url = Column(String(256), nullable=False)
    host = Column(String(128), nullable=True)
    port = Column(Integer, default=443, nullable=False)
    
    auth_type = Column(String(32), default='API_TOKEN', nullable=False)
    encrypted_secret = Column(String(512), nullable=True)
    
    is_active = Column(Boolean, default=True, nullable=False, index=True)
    sync_interval_minutes = Column(Integer, default=15, nullable=False)
    
    last_sync_at = Column(DateTime, nullable=True)
    sync_status = Column(String(32), default='PENDING', nullable=False) # SUCCESS, FAILED, PENDING, NEVER
    sync_message = Column(Text, nullable=True)
    
    devices_discovered_count = Column(Integer, default=0, nullable=False)
    telemetry_records_count = Column(Integer, default=0, nullable=False)
    
    description = Column(Text, nullable=True)
    created_by = Column(String(64), default='admin', nullable=False)

    devices = relationship('Device', back_populates='data_source')

    def to_dict(self, exclude=None):
        data = super().to_dict(exclude=exclude)
        data['encrypted_secret'] = '••••••••' if self.encrypted_secret else None
        return data
