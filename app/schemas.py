from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    description: str
class EventType(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Event(BaseModel):
    id: int
    description: str
    created_at: datetime
    event_type: EventType

    class Config:
        orm_mode = True

