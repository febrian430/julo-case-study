from peewee import *
from models.wallet import Wallet
from models.base import Base
from enum import Enum
import datetime

class Transaction(Base):
    id = TextField(primary_key=True)
    reference_id = TextField(unique=True)
    wallet_id = ForeignKeyField(Wallet, to_field=Wallet.id)
    amount = DecimalField(max_digits=15, decimal_places=3)
    created_at = TimestampField(default=datetime.datetime.now())
    status = TextField() # refer to TransactionStatus enum
    type = TextField()

class TransactionStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class TransactionType(Enum):
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"