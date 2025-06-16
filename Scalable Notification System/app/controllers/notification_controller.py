from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.services.notification_service import NotificationService
from app.services.dependencies import get_notification_service
from app.repositories.notification_repository import NotificationRepository
from app.db.dependencies import get_db
from app.schemas import NotificationRequest

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.post("/notify")
async def notify(
    request_body: NotificationRequest,
    service: NotificationService = Depends(get_notification_service),
):
    try:
        notification = await service.handle_notification(
            request_body.topic, request_body.description
        )
        return {
            "message": f"Notification sent via {notification.topic} channel.",
            "id": notification.id,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_class=HTMLResponse)
async def admin_panel(request: Request, db: Session = Depends(get_db)):
    repo = NotificationRepository(db)
    notifications = repo.get_all_notifications()
    return templates.TemplateResponse(
        "index.html", {"request": request, "notifications": notifications}
    )
