from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(description=event.description, created_at=datetime.utcnow())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_all_events(db: Session):
    return db.query(models.Event).order_by(models.Event.created_at.desc()).all()
