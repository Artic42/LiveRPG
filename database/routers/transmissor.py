from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
import os


router = APIRouter()


@router.put("/jammer/activate")
def jammerArtivate(request: Request):
    os.system("touch /jammerActivated")
    return JSONResponse({
        "status": 200,
        "message": "Jammer activated"
    })


@router.put("/jammer/deactivate")
def jammerDeactivate(request: Request):
    os.system("rm /jammerActivated")
    return JSONResponse({
        "status": 200,
        "message": "Jammer deactivated"
    })


@router.get("/jammer/activated")
def jammerActivated(request: Request):
    if os.path.exists("/jammerActivated"):
        return JSONResponse({
            "status": 200,
            "message": "Jammer activated",
            "activated": 1
        })
    return JSONResponse({
        "status": 200,
        "message": "Jammer deactivated",
        "activated": 0
    })
