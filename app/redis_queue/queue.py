# app/redis_queue/queue.py
import aioredis
from fastapi import BackgroundTasks, Depends
from app.models.notification import NotificationModel
from app.send_notification.via_email import process_email_queue

async def get_redis() -> aioredis.Redis:
    # Create a connection to the Redis server
    redis = await aioredis.from_url("redis://localhost", username="", password="")
    return redis

async def send_notification(notification: NotificationModel, background_tasks: BackgroundTasks, redis: aioredis.Redis = Depends(get_redis),):
    
    # Check the 'ends' field to determine the notification method
    ends = notification.ends

    # If '1' is in ends, send notification on UI
    if 1 in ends:
        print(f"Sending UI notification: {notification.dict()}")

    # If '2' is in ends, send notification via email
    if 2 in ends:
        # Assume you have a list of emails associated with the notification
        emails = ["email@example.com", "another_email@example.com"]
        background_tasks.add_task(process_email_queue, redis)

    # You can add more conditions for other notification methods (e.g., '3' for another method)

    # Add your logic for any other notification methods here
