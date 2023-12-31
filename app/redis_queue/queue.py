import aioredis
from fastapi import BackgroundTasks
from app.models.notification import NotificationModel
from typing import List

from app.send_notification.via_email import send_notification_email
from app.send_notification.via_sms import send_notification_sms
from app.send_notification.via_websocket import send_notification_websocket


async def send_notification(notification: NotificationModel, emails: List[str], phone_numbers: List[str]):
    # Check the 'ends' field to determine the notification method
    ends = notification.ends

    # If '1' is in ends, send notification on UI
    if 1 in ends:
        print(f"Sending UI notification: {notification.dict()}")

    # If '2' is in ends, send notification via email
    if 2 in ends:
        await send_notification_email(notification, emails)

    # If '3' is in ends, send notification via websocket
    if 3 in ends:
        await send_notification_websocket(notification)

    # If '4' is in ends, send notification via SMS
    if 4 in ends:
        await send_notification_sms(notification, phone_numbers)


async def background_send_notification(notification: NotificationModel):
    
    background_tasks = BackgroundTasks()
    
    # Assume you have a list of emails and phone numbers associated with the notification
    emails = ["farazkhalid05@yahoo.com", "farazkhalid05@hotmail.com"]
    phone_numbers = ["1234567890", "9876543210"]

    # Schedule the task to send notifications in the background
    background_tasks.add_task(send_notification, notification, emails, phone_numbers)
