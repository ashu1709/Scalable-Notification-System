from sqlalchemy.orm import Session
from app.db.models import Notification


class NotificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_notification(self, topic: str, description: str) -> Notification:
        notification = Notification(topic=topic, description=description)
        self.db.add(notification)
        self.db.commit()
        self.db.refresh(notification)
        return notification

    def set_delivered(self, notification_id: int, delivered: bool) -> None:
        notification = self.db.query(Notification).get(notification_id)
        if notification:
            notification.delivered = 1 if delivered else 0
            self.db.commit()

    def get_all_notifications(self):
        return (
            self.db.query(Notification).order_by(Notification.created_at.desc()).all()
        )
