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
        orm_mode = True
