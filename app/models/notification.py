# app/models/notification.py

from sqlalchemy import Column, Integer, String, ARRAY, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class NotificationModel(Base):
    
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, index=True, comment="Unique identifier for the notification")
    origin = Column(String, index=True, comment="Name of service sending the notification")
    receivers = Column(ARRAY(Integer), comment=" (1-system-admin, 2-org-admin, 3-job-owner)")
    ends = Column(ARRAY(Integer), comment="Where will notification be sent (1-notification_on_ui, 2-email)")
    severity = Column(Integer, comment="Severity level of the notification (1-critical, 2-high, 3-medium, 4-low)")
    message = Column(String, comment="Message content of the notification")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="Timestamp indicating when the notification was created")
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="Timestamp indicating when the notification was last updated")
    deleted_at = Column(DateTime(timezone=True), nullable=True, comment="Timestamp indicating when the notification was deleted (null by default)")
