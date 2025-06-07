from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

# Создаём таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Зависимость для подключения к базе
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to WhenDo API"}

@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db, event)

@app.get("/events/", response_model=list[schemas.Event])
def read_events(db: Session = Depends(get_db)):
    return crud.get_all_events(db)
