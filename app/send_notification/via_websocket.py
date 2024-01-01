import aioredis
from fastapi import Depends, WebSocket, BackgroundTasks
from app.models.notification import NotificationModel
from app.utils import get_redis, get_websocket


async def enqueue_message(redis: aioredis.Redis, users: list[str], message: str):
    await redis.lpush(f"messages:{users}", message)


async def process_messages(redis: aioredis.Redis, users: list[str], websocket: WebSocket):
    while True:
        message = await redis.brpop(f"messages:{users}", timeout=10)
        if message:
            _, message_data = message
            await websocket.send_text(message_data)


# Now you can use this dependency in your route
async def websocket_endpoint(
    users: list[str],
    websocket: WebSocket = Depends(get_websocket),
    background_tasks: BackgroundTasks = Depends(),
    redis: aioredis.Redis = Depends(get_redis),
):
    # Your existing websocket handling logic
    await websocket.accept()
    background_tasks.add_task(process_messages, redis, users, websocket)
    while True:
        data = await websocket.receive_text()
        await enqueue_message(redis, users, data)