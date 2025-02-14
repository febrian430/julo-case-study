from peewee import *
import models.wallet
from enum import Enum
import datetime

class Transaction(Model):
    id = CharField()
    reference_id = CharField()
    wallet_id = ForeignKeyField(models.wallet, backref="transactions")
    amount = DecimalField()
    created_at = TimestampField(default=datetime.datetime.timestamp())
    status = CharField() # refer to TransactionStatus enum

class TransactionStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
