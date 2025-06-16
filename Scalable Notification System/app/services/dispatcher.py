from app.services.slack import SlackService
from app.services.email import EmailService


class Dispatcher:
    def __init__(self):
        self.services = {
            "sales": SlackService(),
            "pricing": EmailService(),
        }

    async def dispatch(self, topic: str, description: str) -> bool:
        service = self.services.get(topic)
        if not service:
            raise ValueError(f"Unsupported topic: {topic}")
        return await service.send(description)
