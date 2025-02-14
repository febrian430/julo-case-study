from peewee import *
from database.database import get_db

class Base(Model):
    class Meta:
        database = get_db()