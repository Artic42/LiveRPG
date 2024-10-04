from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
import os
import ntfy
import time

router = APIRouter()


@router.get("/bomb/arm")
def armBomb(request: Request):
    os.system("touch /bombArmed")
    return JSONResponse({
        "status": 200,
        "message": "Bomb armed"
    })


@router.get("/bomb/disarm")
def disarmBomb(request: Request):
    os.system("rm /bombArmed")
    return JSONResponse({
        "status": 200,
        "message": "Bomb disarmed"
    })


@router.get("/bomb/explode")
def explodeBomb(request: Request):
    ntfy.sendExplosionNtfy()
    os.system("touch /exploded")
    os.system("rm /bombArmed")
    os.system("rm /lastAccess")
    return JSONResponse({
        "status": 200,
        "message": "Bomb exploded"
    })


@router.get("/bomb/stillAlive")
def stillAlive(request: Request):
    value = int(time.time())
    file = open("/lastAccess", "w")
    file.write(str(value) + "\n")
    file.close()
