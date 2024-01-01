import json
import aioredis

async def send_email(subject: str, message: str, recipient: str):
    # Replace this with your actual email sending logic
    print(f"Sending email to {recipient}: {subject}, {message}")

async def process_email_queue(redis_url: str):
    redis = await aioredis.from_url(redis_url)

    while True:
        # Dequeue an email task
        email_task = await redis.brpop('email_queue', timeout=10)

        if email_task is None:
            # No task found, wait and try again
            continue

        _, json_data = email_task
        email_data = json.loads(json_data)

        # Extract email details from the task
        subject = email_data.get("subject")
        message = email_data.get("message")
        recipients = email_data.get("recipients")

        # Process the email task
        await send_email(subject, message, recipients)