from fastapi import APIRouter, HTTPException
from src.core.config.schema_base import DataResponse
from .schema import CategoryReponse, CategoryRequest
from .service import ServiceCategory

router = APIRouter()

@router.post('/create', response_model=DataResponse[CategoryReponse])
async def create_category(request_body: CategoryRequest):
    category_response = await ServiceCategory().create(name=request_body.name)

    print("category_response", category_response)

    if not category_response:
        raise HTTPException(status_code=400, detail='Incorrect name')

    return DataResponse().success_response(data=category_response)
