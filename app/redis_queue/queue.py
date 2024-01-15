# app/redis_queue/queue.py
from fastapi import HTTPException
from redis import Redis
from app.models.response import NotificationResponse
from app.models.notification import NotificationModel



REDIS_CLIENT = Redis(host='redis', port=6379, db=0)

def send_notification_to_queue(notification: NotificationModel):
    try:
        REDIS_CLIENT.rpush('NOTIFICATION_QUEUE', notification)
        REDIS_CLIENT.set('my-first-key', 'code-always')
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Here here: {str(e)}")
    finally:
        pass
 

def fetch_notification_from_queue():

    try:
        # Fetch notifications from the Redis queue
        notifications = REDIS_CLIENT.get('notifications_queue', 0)
        return [eval(notification) for notification in notifications]
    finally:
        # No need to explicitly close the connection with the 'redis' library
        pass

