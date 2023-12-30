# app/models/response.py
from pydantic import BaseModel
from typing import List

class NotificationResponse(BaseModel):
    id: int
    origin: str
    receivers: List[int]
    ends: List[int]
    severity: int
    message: str

    class Config:
        from_attributes = True


class CreateNotification(BaseModel):
    origin: str
    receivers: List[int]
    ends: List[int]
    severity: int
    message: str

    class Config:
        from_attributes = True