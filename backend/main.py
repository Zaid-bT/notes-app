from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Base,engine,SessionLocal
from models import Note #import models makes SQLAlchemy aware of the Note model.
from schemas import NoteCreate

#checks the database and creates the notes table if it doesn't already exist.
Base.metadata.create_all(bind=engine)

# creates FastApi app
app = FastAPI()

# Allow our React frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#ceate a database session for each request
# a temporary connection/workspace for performing database operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# This function runs when someone visits the root URL "/"
@app.get("/")
def home():
    return {"message": "Notes App API is running!"}

#get notes from PostgreSQL
@app.get("/api/notes") #allows React frontend to communicate with FastAPi
def get_notes(db: Session =  Depends(get_db)):
    return db.query(Note).all() #returns all notes from the database


#add a new note in PostgreSQL
@app.post("/api/notes")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = Note(
        title=note.title,
        content=note.content,
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note