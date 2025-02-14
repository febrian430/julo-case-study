from peewee import *
from models.base import Base

class Wallet(Base):
    id = TextField(primary_key=True)
    customer_id = TextField()
    # only either `enabled_at` or `disabled_at` must have value. the other one must be null
    enabled_at = TimestampField(null=True)
    disabled_at = TimestampField(null=True)
    balance: int = 0
