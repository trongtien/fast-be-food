from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CategoryRequest(BaseModel):
    name: str = None


class CategoryReponse(BaseModel):
    id: int
    uuid_local: str
    name: str
    is_deleted: int
    created_at: Optional[datetime | None] = None
    creatted_by: str
    updated_at: Optional[datetime | None] = None
    updated_by: str
    deledted_at: datetime | None = None
    deleted_by: str