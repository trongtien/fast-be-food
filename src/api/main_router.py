from fastapi import APIRouter
from .category.route import router as category_router


router = APIRouter(prefix="/v1")


router.include_router(category_router, tags=["category"], prefix="/category")

