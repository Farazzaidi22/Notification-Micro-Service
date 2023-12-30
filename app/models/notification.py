# app/models/notification.py
from sqlalchemy import Column, Integer, String, ARRAY
from app.db.database import Base

class NotificationModel(Base):
    
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, index=True, comment="Unique identifier for the notification")
    origin = Column(String, index=True, comment="name of service sending the notification")
    receivers = Column(ARRAY(Integer), comment=" (1-system-admin, 2-org-admin, 3-job-owner)")
    ends = Column(ARRAY(Integer), comment="where will notification be sent (1-notification_on_ui, 2-email)")
    severity = Column(Integer, comment="Severity level of the notification (1-critical, 2-high, 3-medium, 4-low)")
    message = Column(String, comment="Message content of the notification")
