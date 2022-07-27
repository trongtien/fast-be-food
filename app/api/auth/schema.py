from pydantic import BaseModel

class SchemaLoginRequest(BaseModel):
    username: str
    password: str