import os
from dotenv import load_dotenv


def load_config():
    load_dotenv()
    os.environ.setdefault("ENVIRONMENT", "development")
