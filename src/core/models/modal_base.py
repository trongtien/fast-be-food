from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, String, MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr

metadata = MetaData()

@as_declarative()
class Base:
    __abstract__ = True
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class BareBaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now)
    created_by = Column(String, default="")
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_by = Column(String, default="")
    deleted_at = Column(DateTime, default=datetime.now)
    deleted_by = Column(String, default="")