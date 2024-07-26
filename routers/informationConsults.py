from fastapi import APIRouter
from fastapi.responses import JSONResponse
import routers.responseHandling as responseHandling
import databaseManager.infoConsults as infoConsults


router = APIRouter()


@router.get("/information/readKnown/{ID}")
def readKnown(ID: int):
    # Check if the ID exists
    if ID not in infoConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not found")

    # Get the known character
    knownCharacter = infoConsults.getKnownCharacter("/Database.db", ID)
    return JSONResponse({"status": 200, "knownCharacter": knownCharacter})


@router.get("/information/readAbout/{ID}")
def readAbout(ID: int):
    # Check if the ID exists
    if ID not in infoConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not found")

    # Get the about character
    aboutCharacter = infoConsults.getAboutCharacter("/Database.db", ID)
    return JSONResponse({"status": 200, "aboutCharacter": aboutCharacter})


@router.get("/information/readDescription/{ID}")
def readDescription(ID: int):
    # Check if the ID exists
    if ID not in infoConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not found")

    # Get the description
    description = infoConsults.getDescription("/Database.db", ID)
    return JSONResponse({"status": 200, "description": description})


@router.get("/information/readFull/{ID}")
def readFull(ID: int):
    # Check if the ID exists
    if ID not in infoConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not found")

    # Get the full information
    knownCharacter = infoConsults.getKnownCharacter("/Database.db", ID)
    aboutCharacter = infoConsults.getAboutCharacter("/Database.db", ID)
    description = infoConsults.getDescription("/Database.db", ID)
    return JSONResponse({"status": 200,
                         "knownCharacter": knownCharacter,
                         "aboutCharacter": aboutCharacter,
                         "description": description})
