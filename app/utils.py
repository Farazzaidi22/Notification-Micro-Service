import aioredis
from fastapi import Depends, HTTPException, WebSocket, WebSocketDisconnect

async def get_redis() -> aioredis.Redis:
    # Create a connection to the Redis server
    redis = await aioredis.from_url("redis://localhost", username="", password="")
    return redis

async def get_websocket(websocket: WebSocket = Depends()):
    try:
        # Try to accept the WebSocket connection
        await websocket.accept()
        return websocket
    except WebSocketDisconnect as e:
        # Handle disconnection if needed
        raise HTTPException(status_code=400, detail="WebSocket connection closed")
