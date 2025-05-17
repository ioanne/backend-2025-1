from fastapi import APIRouter


router = APIRouter()


@router.get("/") # localhost:8000/ejemplo/
async def ejemplo2():
    return {"ejemplo2": "ejemplo2"}
