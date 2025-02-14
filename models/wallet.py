from peewee import *

class Wallet(Model):
    id = CharField()
    customer_id = CharField()
    # only either `enabled_at` or `disabled_at` must have value. the other one must be null
    enabled_at = TimestampField(null=True)
    disabled_at = TimestampField(null=True)
