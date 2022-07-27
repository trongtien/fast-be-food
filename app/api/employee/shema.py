from pydantic import BaseModel


class SchemaEmployeeResponse(BaseModel):
    username: str
    password: str
    last_name: str
    first_name: str
    avarta: str
    status: int
    role: int
    token: str
    refresh_token: str