from sqlalchemy.orm import Session
from datetime import datetime
from rapidfuzz import fuzz
from .models import Event, EventType

from . import models, schemas

SIMILARITY_THRESHOLD = 70  # порог похожести в %

def find_similar_event_type(db: Session, description: str):
    all_types = db.query(EventType).all()
    for etype in all_types:
        score = fuzz.partial_ratio(description.lower(), etype.name.lower())
        if score >= SIMILARITY_THRESHOLD:
            return etype
    return None

def create_event(db: Session, event: schemas.EventCreate):
    matched_type = find_similar_event_type(db, event.description)

    if matched_type is None:
        matched_type = EventType(name=event.description)
        db.add(matched_type)
        db.commit()
        db.refresh(matched_type)

    db_event = Event(
        description=event.description,
        created_at=datetime.utcnow(),
        event_type_id=matched_type.id
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_all_events(db: Session):
    return db.query(models.Event).order_by(models.Event.created_at.desc()).all()

def get_intervals_for_event_type(db: Session, event_type_id: int) -> list[int]:
    events = (
        db.query(models.Event)
        .filter(models.Event.event_type_id == event_type_id)
        .order_by(models.Event.created_at.asc())
        .all()
    )

    intervals = []
    for i in range(1, len(events)):
        delta = events[i].created_at - events[i - 1].created_at
        intervals.append(delta.days)

    return intervals

def get_reminder_days(event_type_id: int, db: Session) -> list[int]:
    intervals = get_intervals_for_event_type(db, event_type_id)
    
    if not intervals:
        return []  # Недостаточно данных

    avg_interval = sum(intervals) // len(intervals)

    # Пример: дни до следующего события
    # (можно заменить на числа Фибоначчи [13, 17, 19] ближе к avg_interval)
    reminder_days = []
    current = 0
    fib1, fib2 = 1, 2

    while fib2 < avg_interval:
        reminder_days.append(avg_interval - fib2)
        fib1, fib2 = fib2, fib1 + fib2

    # Убираем повторы и сортируем по возрастанию
    return sorted(set(reminder_days))
