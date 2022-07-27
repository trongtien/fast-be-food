from fastapi import APIRouter
from typing import Any
from app.lib.schema_base import PagingReponse
# from .shema import SchemaEmployeeResponse

router = APIRouter()


@router.get(
    path="/",
    name="Employee Classification"
)
async def getFindAllEmployee():
    return PagingReponse[Any](data = [],
        total_item = 0,
        total_page = 0,
        current_page = 0) 
