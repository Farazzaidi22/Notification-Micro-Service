# app/redis_queue/queue.py
import aioredis
from fastapi import BackgroundTasks
from app.models.notification import NotificationModel

async def send_notification(notification: NotificationModel):
    # Implement your logic to send notifications (e.g., push to Redis queue)
    # Here, we'll just print the notification for demonstration purposes
    print(f"Sending notification: {notification.dict()}")

async def background_send_notification(notification: NotificationModel, background_tasks: BackgroundTasks):
    # Use the background_tasks to schedule the task
    background_tasks.add_task(send_notification, notification)
