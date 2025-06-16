from pydantic import BaseModel
from enum import Enum


class Topic(str, Enum):
    sales = "sales"
    pricing = "pricing"


class NotificationRequest(BaseModel):
    topic: Topic
    description: str
