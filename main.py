from fastapi import FastAPI
from database.database import connect as connect_database, get_db
from models.transaction import Transaction
from models.wallet import Wallet
from routers import wallet

db = get_db()
db.create_tables([Wallet, Transaction])

app = FastAPI()
app.include_router(wallet.router)
app.include_router(wallet.private_router)

@app.get("/ping")
def ping():
    return {"ping": "pong"}