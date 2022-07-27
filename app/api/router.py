from fastapi import APIRouter
from app.api.employee import view as EmployeeView
from app.api.auth import view as AuthView

router = APIRouter()

router.include_router(router=AuthView.router, prefix="/auth", tags=["Auth"])
router.include_router(router=EmployeeView.router, prefix="/employee", tags=["Employee"])