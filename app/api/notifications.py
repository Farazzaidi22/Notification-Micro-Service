# app/api/notifications.py
from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db as get_database
from app.models.notification import NotificationModel
from app.models.response import NotificationResponse, CreateNotification
from app.api.pagination import Pagination
from typing import List, Any
from redis_queue.queue import background_send_notification

router = APIRouter()

@router.post("/notifications/", response_model=NotificationResponse)
def create_notification(notification: CreateNotification) -> Any:
    
    # Create a new session using the global engine
    db = get_database()
    
    # Save the notification to the database
    db_notification = NotificationModel(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)

    return db_notification



@router.get("/notifications/", response_model=List[NotificationResponse])
def get_notifications(org_id: int, receiver: int, end: int, pagination: Pagination = Depends())  -> Any:
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
        
        
@router.get("/notifications/{notification_id}", response_model=NotificationResponse)
def get_notification(notification_id: int) -> Any:
    # Create a new session using the global engine
    db = get_database()

    try:
        notification = db.query(NotificationModel).filter(NotificationModel.id == notification_id).first()

        if notification is None:
            raise HTTPException(status_code=404, detail="Notification not found")

        background_send_notification(notification)
        
        # Convert SQLAlchemy object to Pydantic model
        return notification
    finally:
        db.close()
