from sqlalchemy.orm import Session
from app.services.dispatcher import Dispatcher
from app.repositories.notification_repository import NotificationRepository
from app.db.models import Notification
import logging


class NotificationService:
    def __init__(self, db: Session):
        self.db = db
        self.dispatcher = Dispatcher()
        self.repo = NotificationRepository(self.db)

    async def handle_notification(self, topic: str, description: str) -> Notification:
        logging.info(
            f"Creating notification in DB: topic='{topic}', description='{description}'"
        )
        notification = self.repo.create_notification(topic, description)

        logging.info(
            f"Attempting to dispatch notification ID={notification.id} to channel '{topic}'"
        )
        try:
            success = await self.dispatcher.dispatch(topic, description)
            self.repo.set_delivered(notification.id, success)

            if success:
                logging.info(
                    f"Notification ID={notification.id} successfully delivered via '{topic}'"
                )
            else:
                logging.warning(
                    f"Notification ID={notification.id} failed to deliver via '{topic}'"
                )
        except Exception as e:
            logging.error(f"Error dispatching notification ID={notification.id}: {e}")
            self.repo.set_delivered(notification.id, False)

        return notification
