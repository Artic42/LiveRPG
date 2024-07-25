from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
import routers.responseHandling as responseHandling
import databaseManager.eventConsults as eventConsults

router = APIRouter()


@router.get("/event/read/{ID}")
def readEvent(ID: int, request: Request):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")

    # Consult database
    description = eventConsults.getEventDescription("/Database.db", ID)
    hacking = eventConsults.getEventHack("/Database.db", ID)
    wait = eventConsults.getEventWait("/Database.db", ID)
    activate = eventConsults.getEventActivate("/Database.db", ID)
    activated = eventConsults.getEventActivated("/Database.db", ID)
    redirectID = eventConsults.getEventRedirectID("/Database.db", ID)
    equip = eventConsults.getEventEquip("/Database.db", ID)

    return JSONResponse({
        "status": 200,
        "description": description,
        "hacking": hacking,
        "wait": wait,
        "activate": activate,
        "activated": activated,
        "redirectID": redirectID,
        "equip": equip
    })


@router.get("/event/readDescription/{ID}")
def readDescription(ID: int, request: Request):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")

    description = eventConsults.getEventDescription("/Database.db", ID)

    return JSONResponse({
        "status": 200,
        "description": description
    })


@router.get("/event/readFlags/{ID}")
def readFlags(ID: int, request: Request):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")

    hacking = eventConsults.getEventHack("/Database.db", ID)
    wait = eventConsults.getEventWait("/Database.db", ID)
    activate = eventConsults.getEventActivate("/Database.db", ID)
    equip = eventConsults.getEventEquip("/Database.db", ID)

    return JSONResponse({
        "status": 200,
        "hacking": hacking,
        "wait": wait,
        "activate": activate,
        "equip": equip
    })


@router.get("/event/activated/{ID}")
def getEventActivated(ID: int, request: Request):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")

    # Consult database
    activated = eventConsults.getEventActivated("/Database.db", ID)

    return JSONResponse({
        "status": 200,
        "activated": activated
    })


@router.get("/event/readRedirect/{ID}")
def readRedirect(ID: int, request: Request):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")

    # Consult database

    redirectID = eventConsults.getEventRedirectID("/Database.db", ID)

    return JSONResponse({
        "status": 200,
        "redirectID": redirectID
    })
