import configs
from pymongo import MongoClient
from pymongo.database import Database

db: Database = None

def conn() -> Database:
    global db
    if db is None:
        db = MongoClient(
            username=configs.DB_USER, 
            password=configs.DB_PWD, 
            host=configs.DB_HOST,
            port=configs.DB_PORT
        ).get_database(configs.DB_NAME)

        return db
    else:
        return db
