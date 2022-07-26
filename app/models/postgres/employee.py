from sqlalchemy import Column, Integer, VARCHAR
from app.configs.postgresql import Base_postgresql
from .base import BaseModelPostgres

class EmployeeModel(BaseModelPostgres, Base_postgresql):
    __tablename__ = 'employee'

    username=Column("username", VARCHAR(255), nullable=True)
    password=Column("password", VARCHAR(255), nullable=True)
    last_name=Column("last_name",VARCHAR(255))
    first_name=Column("first_name",VARCHAR(255))
    avarta=Column("avarta",VARCHAR(255))
    status=Column("status", Integer)
    role=Column("role", VARCHAR(255))
    token=Column("token", VARCHAR(255))
    refresh_token=Column("refresh_token", VARCHAR(255))
