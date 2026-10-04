

from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True,index=True)
    password_hash: Mapped[str] = mapped_column(String(255))

"""users
----------------
id
email
password_hash"""



class Note(Base): #represents a table in the database
    __tablename__ = "notes"

    # columns' name (id,title,content,created_at,updated_at)
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )

    """    notes
------------------------------------------------
id            integer        primary key
title         varchar(200)
content       text
created_at    timestamp
updated_at    timestamp             """