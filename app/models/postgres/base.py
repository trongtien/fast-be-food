from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.ext.declarative import declared_attr

class BaseModelPostgres(object):


    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
        
    __mapper_args__= {'always_refresh': True}


    id=Column("id", Integer, nullable=True,  primary_key =True) 
    created_at=Column("created_at", DateTime) 
    created_by=Column("created_by", VARCHAR(255)) 
    updated_at=Column("updated_at", DateTime) 
    updated_by=Column("updated_by", VARCHAR(255)) 
    deleted_at=Column("deleted_at", DateTime) 
    deleted_by=Column("deleted_by", VARCHAR(255)) 