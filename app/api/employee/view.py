from fastapi import APIRouter

router = APIRouter()


@router.get(
    path="/",
    name="Employee Classification",
)
async def getFindAllEmployee():
    pass
