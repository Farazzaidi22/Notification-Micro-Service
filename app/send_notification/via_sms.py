from app.models.notification import NotificationModel


async def send_notification_sms(notification: NotificationModel, phone_numbers: List[str]):
    # Implement your logic to send notifications via SMS
    # Here, we'll just print the SMS notification for demonstration purposes
    print(f"Sending SMS notification to {phone_numbers}: {notification.dict()}")