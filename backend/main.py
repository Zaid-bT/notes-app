from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base,engine
import models #import models makes SQLAlchemy aware of the Note model.

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


# This function runs when someone visits the root URL "/"
@app.get("/")
def home():
    return {"message": "Notes App API is running!"}

@app.get("/api/notes") #allows React frontend to communicate with FastAPi
def get_notes():
    return [
        {
            "id" : 1,
            "title" : "My First Note",
            "content" : "learning full stack development."
        },
        {
            "id" : 2,
            "title" : "useful link",
            "content" : "https://fastapi.tiangolo.com/"
        }
    ]