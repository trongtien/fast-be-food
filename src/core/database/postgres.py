from typing import Generator
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from databases import Database
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql://postgres:1@localhost/food_dev"

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


metadata = MetaData()


databaseBase = Database(DATABASE_URL)


base_schemaly = declarative_base()