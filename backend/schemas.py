
from pydantic import BaseModel

#data required when creating a note
class NoteCreate(BaseModel):
    title: str
    content: str