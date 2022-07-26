from sqlalchemy.orm import Session
from app.configs.postgresql import SessionLocalPostgre


class RepositoryBase:

    def __init__(self, is_init_db_postgres: bool = True) -> None:
        self.postgre_session: Session = None
        
        if is_init_db_postgres:
            self.postgre_session = SessionLocalPostgre()


    def close_postgre_session(self):
        if self.postgre_session:
            self.postgre_session.close()
