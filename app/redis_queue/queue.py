# app/redis_queue/queue.py
# import aioredis
# from fastapi import BackgroundTasks, Depends, WebSocket
# from app.models.notification import NotificationModel
# from app.send_notification.via_email import process_email_queue
# from app.send_notification.via_websocket import websocket_endpoint
# from app.utils import get_redis, get_websocket



# async def send_notification(notification: NotificationModel, background_tasks: BackgroundTasks, websocket: WebSocket = Depends(get_websocket), redis: aioredis.Redis = Depends(get_redis)):
    
#     # Check the 'ends' field to determine the notification method
#     ends = notification.ends

#     # If '1' is in ends, send notification on UI
#     if 1 in ends:
#         users = [1,2,3]
#         await websocket_endpoint(users, websocket, background_tasks, redis)

#     # If '2' is in ends, send notification via email
#     if 2 in ends:
#         # Assume you have a list of emails associated with the notification
#         emails = ["email@example.com", "another_email@example.com"]
#         background_tasks.add_task(process_email_queue, redis)

#     # You can add more conditions for other notification methods (e.g., '3' for another method)

    # Add your logic for any other notification methods here
    
    
# app/redis_queue/queue.py
from fastapi import HTTPException
from redis import Redis
from rq import Queue
from app.models.response import NotificationResponse
from app.models.notification import NotificationModel



REDIS_CLIENT = Redis(host='redis', port=6379, db=0)

def send_notification_to_queue(notification: NotificationModel):
    # Connect to Redis
    # REDIS_CLIENT.rpush('QUEUE', notification)
    
    print("here here 2")
     
    try:
        print("\n\n\n\n\n\n\n\nREDIS_CLIENT", REDIS_CLIENT , "\n\n\n\n\n\n\n\n")
        

        REDIS_CLIENT.set('my-first-key', 'code-always')
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Here here: {str(e)}")
    finally:
        print("here here 2")


    # try:
    #     # Push the notification to the Redis queue
    #     # redis_client.lpush('notifications_queue', str(notification))
    #     # task_queue.enqueue("vgvhgchgch")
        
    # finally:
    #     # No need to explicitly close the connection with the 'redis' library
    #     pass

def fetch_notification_from_queue():

    try:
        # Fetch notifications from the Redis queue
        notifications = REDIS_CLIENT.lrange('notifications_queue', 0, -1)
        return [eval(notification) for notification in notifications]
    finally:
        # No need to explicitly close the connection with the 'redis' library
        pass

