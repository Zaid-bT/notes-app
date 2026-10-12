
from database import engine

try:
    with engine.connect():
        print("Database connection successful")
except Exception as e:
    print(f"Database connection failed")
    print(e)