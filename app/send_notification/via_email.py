import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from typing import List
from app.models.notification import NotificationModel


async def send_notification_email(notification: NotificationModel, emails: List[str]):
    # Email configuration (replace placeholders with actual values)
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    smtp_username = 'your_smtp_username'
    smtp_password = 'your_smtp_password'
    sender_email = 'your_sender_email@example.com'
    subject = 'Notification from Your App'

    # Construct the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(emails)
    message['Subject'] = subject

    # Add the notification message to the email body
    body = f"Notification Message:\n\n{notification.message}"
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, emails, message.as_string())

    print(f"Email notification sent to {emails}: {notification.dict()}")