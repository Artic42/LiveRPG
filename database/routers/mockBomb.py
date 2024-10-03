from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/bomb/arm")
def armBomb():
