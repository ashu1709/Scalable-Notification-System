from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    topic: Mapped[str] = mapped_column(index=True)
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    delivered: Mapped[int] = mapped_column(default=0)
