import os
import logging


class SlackService:
    async def send(self, message: str) -> bool:
        webhook_url = os.getenv("SLACK_WEBHOOK_URL")
        logging.info(f"[MOCK] Sending to Slack webhook ({webhook_url}): {message}")
        return True
