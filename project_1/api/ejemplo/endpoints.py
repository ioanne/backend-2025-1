from fastapi import APIRouter


router = APIRouter()


@router.get("/") # localhost:8000/ejemplo/
async def ejemplo():
    return {"ejemplo": "ejemplo"}
