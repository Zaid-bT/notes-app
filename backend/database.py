
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#load variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

#create a database connection 
engine = create_engine(DATABASE_URL)

#create database sessions
SessionLocal = sessionmaker(bind=engine)

#base class for our database models
Base = declarative_base()