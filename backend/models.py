from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))

    # A user can have multiple notes
    notes: Mapped[list["Note"]] = relationship(
        "Note",
        back_populates="owner"
    )

    """users
----------------
id
email
password_hash"""


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Connect the note to its owner
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )

    # Relationship back to the user
    owner: Mapped[User] = relationship(
        "User",
        back_populates="notes"
    )
"""    notes
------------------------------------------------
id            integer        primary key
title         varchar(200)
content       text
created_at    timestamp
updated_at    timestamp             """