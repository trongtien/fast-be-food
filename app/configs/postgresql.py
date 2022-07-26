from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .env_config import config_get_env


HOST=config_get_env("HOST_PG_DEV_LIVE", str)
UERNAME=config_get_env("USERNAME_PG_DEV_LIVE", str)
PASSWORD=config_get_env("PASSWORD_PG_DEV_LIVE", str)
PORT=config_get_env("PORT_PG_DEV_LIVE", str)
DB_NAME=config_get_env("DATABASE_NAME_PG_DEV_LIVE", str)


SQLALCHEMY_DATABASE_POSTGRESQL_URL="postgresql://{username}:{password}@{host}:{port}/{db_name}".format(
        username=UERNAME, password=PASSWORD, host=HOST, port=PORT, db_name=DB_NAME
    )


engine_postgresql = create_engine(SQLALCHEMY_DATABASE_POSTGRESQL_URL)


SessionLocalPostgre = sessionmaker(autocommit=False, autoflush=False, bind=engine_postgresql)


Base_postgresql = declarative_base()

