from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    description: str

class Event(BaseModel):
    id: int
    description: str
    created_at: datetime

    class Config:
        orm_mode = True
