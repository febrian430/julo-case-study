from peewee import *
from ..database import get_db

class Base(Model):
    class Meta:
        database = get_db()