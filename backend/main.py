from fastapi import FastAPI

# creates FastApi app
app = FastAPI()

# This function runs when someone visits the root URL "/"
@app.get("/")
def home():
    return {"message": "Notes App API is running!"}