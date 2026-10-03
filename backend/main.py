from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Notes App API is running!"}