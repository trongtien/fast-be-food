from src.core.database.postgres import databaseBase as database_postgres
from typing import Callable

def event_start_app() -> Callable:
    database_postgres.connect()


def event_close_app() -> Callable:
    database_postgres.disconnect()