# app/redis_queue/queue.py
from fastapi import HTTPException
from redis import Redis
from app.models.response import NotificationResponse
from app.models.notification import NotificationModel



REDIS_CLIENT = Redis(host='redis', port=6379, db=0)

def send_notification_to_queue(notification: NotificationModel):
    try:
        # Push the notification to the Redis queue
        REDIS_CLIENT.rpush('notifications_queue', str(notification))
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error pushing to Redis queue: {str(e)}")

def fetch_notification_from_queue():
    try:
        # Fetch all notifications from the Redis queue
        notifications = REDIS_CLIENT.lrange('notifications_queue', 0, -1)
        return [eval(notification) for notification in notifications]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching from Redis queue: {str(e)}")
