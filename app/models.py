from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class EventType(Base):
    __tablename__ = "event_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    events = relationship("Event", back_populates="event_type")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    event_type_id = Column(Integer, ForeignKey("event_types.id"))
    event_type = relationship("EventType", back_populates="events")
