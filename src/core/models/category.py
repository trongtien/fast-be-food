from email.policy import default
from sqlalchemy import (Column, DateTime, Integer, String, Table, create_engine)
# from .modal_base import BareBaseModel
from sqlalchemy.sql import func
from src.core.database.postgres import metadata as metadata_postges
from src.core.database.postgres import base_schemaly

class Categories(base_schemaly):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid_local = Column(String(50))
    name = Column(String(50), default="")
    is_deleted = Column( Integer, default=0)
    created_at = Column( DateTime, default=func.now(), nullable=False)
    created_by = Column( String, default="")
    updated_at = Column( DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column( DateTime, default=func.now(), onupdate=func.now())
    deleted_by = Column( String, default="")
    
    