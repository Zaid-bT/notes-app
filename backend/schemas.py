
from pydantic import BaseModel




#data requied when creating a user
class UserCreate(BaseModel):
    email: str
    password: str

#data required when logging in
class Token(BaseModel):
    access_token: str
    token_type: str

#data required when creating a note
class NoteCreate(BaseModel):
    title: str
    content: str