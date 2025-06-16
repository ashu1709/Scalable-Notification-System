import logging
from pathlib import Path
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.config import load_config
from app.db import models
from app.db.database import engine
from app.controllers import notification_controller

log_path = Path("logs/assist_notifier.log")
log_path.parent.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(log_path), logging.StreamHandler()],
)

load_config()
app = FastAPI(title="Assist Notifier", version="1.0.0")
models.Base.metadata.create_all(bind=engine)
app.include_router(notification_controller.router)
templates = Jinja2Templates(directory="app/templates")
