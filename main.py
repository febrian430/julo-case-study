from fastapi import FastAPI
from database.database import connect as connect_database

connect_database()

app = FastAPI()


@app.get("/ping")
def ping():
    return {"ping": "pong"}