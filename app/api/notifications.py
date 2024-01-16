# app/api/notifications.py
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from app.db.database import get_db as get_database
from app.models.notification import NotificationModel
from app.models.response import NotificationResponse, CreateNotification
from app.api.pagination import Pagination
from typing import List, Dict, Union, Any

from app.redis_queue.queue import fetch_notification_from_queue, send_notification_to_queue

router = APIRouter()

@router.post("/notifications/", response_model=NotificationResponse)
def create_notification(notification: CreateNotification, background_tasks: BackgroundTasks) -> Any:
    try:
        # Create a new session using the global engine
        db = get_database()

        # Save the notification to the database
        db_notification = NotificationModel(**notification.dict())
        db.add(db_notification)
        db.commit()
        db.refresh(db_notification)
        
        # Print the decoded values of db_notification
        decoded_notification = jsonable_encoder(db_notification)        
        send_notification_to_queue(decoded_notification)

        return db_notification

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        db.close()


@router.get("/notifications/", response_model=List[NotificationResponse])
def get_notifications(org_id: int, receiver: int, end: int, pagination: Pagination = Depends()) -> Any:
    try:
        # Create a new session using the global engine
        db = get_database()

        skip = (pagination.page - 1) * pagination.per_page
        limit = pagination.per_page

        query = db.query(NotificationModel)

        if org_id is not None:
            query = query.filter(NotificationModel.org_id == org_id)

        if receiver is not None:
            query = query.filter(NotificationModel.receivers.contains([receiver]))

        if end is not None:
            query = query.filter(NotificationModel.ends.contains([end]))

        notifications = query.offset(skip).limit(limit).all()

        # Convert SQLAlchemy objects to Pydantic models
        return notifications

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        db.close()


@router.get("/notifications/{notification_id}", response_model=NotificationResponse)
async def get_notification(notification_id: int, background_tasks: BackgroundTasks) -> Any:
    try:
        # Create a new session using the global engine
        db = get_database()

        notification = db.query(NotificationModel).filter(NotificationModel.id == notification_id).first()

        if notification is None:
            raise HTTPException(status_code=404, detail="Notification not found")

        # Convert SQLAlchemy object to Pydantic model
        return notification

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        db.close()



@router.get("/queue/notifications/", response_model=List[NotificationResponse])
def fetch_notifications_from_queue() -> Any:
 
    try:
        # Fetch notifications from the Redis queue
        notifications = fetch_notification_from_queue()
        
        return notifications
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
