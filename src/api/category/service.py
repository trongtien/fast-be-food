import uuid
import databases
from fastapi import Depends
from unicodedata import category
from .schema import CategoryReponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.models.category import Categories
from src.core.database.postgres import databaseBase
from sqlalchemy.orm import Session

class ServiceCategory:

    @staticmethod
    async def create(* ,name: str):
        # session = Session()
        db = Session
        
        db_user = Categories(name=name, is_deleted=0, uuid_local=uuid.uuid4())
        db.add(db_user)
        db.commit()
        # return db.query(Categories).filter(Categories.id == user_id).first()
        # query = Categories.insert().values(name=name, is_deleted=0, uuid_local=uuid.uuid4())
        # last_insert = await databaseBase.execute(query=query)
        # print("last_insert", last_insert)
        return db_user
            
       