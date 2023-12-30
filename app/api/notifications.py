# app/api/notifications.py
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.database import get_db as get_database
from app.models.notification import NotificationModel
from app.redis_queue.queue import background_send_notification
from app.models.response import NotificationResponse
from app.api.pagination import Pagination
from typing import List

router = APIRouter()

# @router.post("/notifications/", response_model=dict)
# def create_notification(notification: NotificationModel, db: Session = Depends(get_database)):
#     # Your logic to save the notification to the database
#     # ...

#     # Use BackgroundTasks directly within the endpoint function
#     background_tasks = BackgroundTasks()
#     background_tasks.add_task(background_send_notification, notification)

#     return {"message": "Notification received and will be processed asynchronously."}

@router.get("/notifications/", response_model=List[NotificationResponse])
def get_notifications(org_id: int, receiver: int, end: int, pagination: Pagination = Depends()):
    # Create a new session using the global engine
    db = get_database()

    try:
        skip = (pagination.page - 1) * pagination.per_page
        limit = pagination.per_page

        notifications = db.query(NotificationModel).offset(skip).limit(limit).all()
        
        # Convert SQLAlchemy objects to Pydantic models
        return notifications
    finally:
        db.close()
