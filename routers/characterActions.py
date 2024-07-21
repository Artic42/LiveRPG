from fastapi import APIRouter

router = APIRouter()

@router.get("/character")
def get_character():
    return {"Hello": "World"}