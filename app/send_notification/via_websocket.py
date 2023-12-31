from app.models.notification import NotificationModel


async def send_notification_websocket(notification: NotificationModel):
    # Implement your logic to send notifications via websocket
    # Here, we'll just print the websocket notification for demonstration purposes
    print(f"Sending websocket notification: ")