from typing import List, Optional
from app.models.notification import SystemNotification, WebhookEndpoint
from app.models.base import db

class NotificationService:
    def get_notifications_for_user(self, user_id: Optional[str] = None, unread_only: bool = False, limit: int = 20) -> List[SystemNotification]:
        query = SystemNotification.query.filter(
            (SystemNotification.user_id == user_id) | (SystemNotification.user_id == None),
            SystemNotification.is_deleted == False
        )
        if unread_only:
            query = query.filter_by(is_read=False)
        return query.order_by(SystemNotification.created_at.desc()).limit(limit).all()

    def create_notification(self, title: str, message: str, category: str = 'ALERT', severity: str = 'INFO', user_id: str = None, action_url: str = None) -> SystemNotification:
        notif = SystemNotification(
            title=title,
            message=message,
            category=category,
            severity=severity,
            user_id=user_id,
            action_url=action_url
        )
        db.session.add(notif)
        db.session.commit()
        return notif

    def mark_as_read(self, notification_id: str):
        notif = SystemNotification.query.get(notification_id)
        if notif:
            notif.is_read = True
            db.session.commit()
            return True
        return False
