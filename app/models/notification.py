from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class SystemNotification(BaseModel):
    __tablename__ = 'nw_notifications'

    user_id = Column(String(36), ForeignKey('nw_users.id'), nullable=True, index=True)
    title = Column(String(128), nullable=False)
    message = Column(Text, nullable=False)
    category = Column(String(32), default='ALERT', nullable=False, index=True)
    severity = Column(String(16), default='INFO', nullable=False, index=True)
    is_read = Column(Boolean, default=False, nullable=False, index=True)
    action_url = Column(String(256), nullable=True)

    user = relationship('User')

class WebhookEndpoint(BaseModel):
    __tablename__ = 'nw_webhooks'

    name = Column(String(128), nullable=False)
    target_url = Column(String(512), nullable=False)
    event_filter = Column(String(256), default='alert.critical,incident.created')
    secret_token = Column(String(128), nullable=True)
    is_enabled = Column(Boolean, default=True, nullable=False, index=True)
    failure_count = Column(Integer, default=0, nullable=False)
