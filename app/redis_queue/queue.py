# app/redis_queue/queue.py
import json
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from redis import Redis
from app.models.response import NotificationResponse
from app.models.notification import NotificationModel
from typing import List, Dict, Union


REDIS_CLIENT = Redis(host='redis', port=6379, db=0)


def send_notification_to_queue(notification: NotificationResponse):    
    try:
        # Push the notification to the Redis queue
        notification_str = json.dumps(notification)
        REDIS_CLIENT.rpush('notifications_queue', notification_str)
        print(notification_str, "notification_str")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error pushing to Redis queue: {str(e)}")
    
def fetch_notification_from_queue():
    try:
        # Fetch all notifications from the Redis queue
        notifications = REDIS_CLIENT.lrange('notifications_queue', 0, -1)
        
        # Deserialize each notification string into a dictionary
        deserialized_notifications = [json.loads(notification.decode("utf-8")) for notification in notifications]
        print("\n\n\n\n\n\n", deserialized_notifications,  "here here new\n\n\n\n\n\n\n\n")

        
        return deserialized_notifications
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching from Redis queue: {str(e)}")


