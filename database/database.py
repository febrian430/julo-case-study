from peewee import *
from os import getenv
from logger.logger import logger 

db: PostgresqlDatabase = None

def connect():
    host = getenv("POSTGRES_DB_HOST")
    port = getenv("POSTGRES_DB_PORT")
    user = getenv("POSTGRES_DB_USER")
    password = getenv("POSTGRES_DB_PASSWORD")
    name = getenv("POSTGRES_DB_NAME")
    
    global db
    try:
        db = PostgresqlDatabase(name, user=user, password=password, host=host, port=port)
        is_connected = db.connect()
        if is_connected:
            logger.info("connection to db successful")
        else:
            logger.error(f'failed connecting to db')    
    except Exception as e:
        logger.error(f'error connecting to db: {e}')
        raise e

def get_db():
    if db is None:
        connect()
    return db