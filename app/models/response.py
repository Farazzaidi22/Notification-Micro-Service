# app/models/response.py
from pydantic import BaseModel
from typing import List

class NotificationResponse(BaseModel):
    id: int
    org_id: int
    sender: str
    receivers: List[int]
    ends: List[int]
    severity: int
    message: str

    class Config:
        from_attributes = True


class CreateNotification(BaseModel):
    sender: str
    org_id: int
    receivers: List[int]
    ends: List[int]
    severity: int
    message: str

    class Config:
        from_attributes = True