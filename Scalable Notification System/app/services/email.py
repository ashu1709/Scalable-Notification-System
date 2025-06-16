import os
import logging


class EmailService:
    async def send(self, message: str) -> bool:
        recipient = os.getenv("EMAIL_DESTINATION")
        logging.info(f"[MOCK] Sending email to {recipient}: {message}")
        return True
