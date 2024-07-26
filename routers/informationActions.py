from fastapi import APIRouter
from fastapi import Request
import routers.responseHandling as responseHandling
import databaseManager.infoActions as infoActions
import databaseManager.infoConsults as infoConsults


router = APIRouter()


@router.post("/information/create/{ID}")
def createInformation(ID: int):
    # Check if the ID exists
    if ID in infoConsults.getAllIDs():
        return responseHandling.errorIDAlreadyExists("ID already exists")
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be greater than 0")

    # Create the information
    infoActions.createInformation(ID)
    return responseHandling.success("Information entry created")


@router.delete("/information/delete/{ID}")
def deleteInformation(ID: int):
    # Check if the ID exists
    if ID not in infoConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not found")

    # Delete the information
    infoActions.deleteInformation(ID)
    return responseHandling.success("Information entry deleted")


@router.put("/information/editKnown/{ID}")
async def editKnown(ID: int, request: Request):
    # Check if the ID exists
    if ID not in infoConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not found")

    # Get the known character
    knownCharacter = await request.json()
    if "knownCharacter" not in knownCharacter:
        return responseHandling.errorIncorrectParameter(
            "knownCharacter parameter not found")

    # Edit the known character
    infoActions.editKnownCharacter(ID, knownCharacter["knownCharacter"])
    return responseHandling.success("Known character edited")


@router.put("/information/editAbout/{ID}")
async def editAbout(ID: int, request: Request):
    # Check if the ID exists
    if ID not in infoConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not found")

    # Get the about character
    aboutCharacter = await request.json()
    if "aboutCharacter" not in aboutCharacter:
        return responseHandling.errorIncorrectParameter(
            "aboutCharacter parameter not found")

    # Edit the about character
    infoActions.editAboutCharacter(ID, aboutCharacter["aboutCharacter"])
    return responseHandling.success("About character edited")


@router.put("/information/editDescription/{ID}")
async def editDescription(ID: int, request: Request):
    # Check if the ID exists
    if ID not in infoConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not found")

    # Get the description
    description = await request.json()
    if "description" not in description:
        return responseHandling.errorIncorrectParameter(
            "description parameter not found")

    # Edit the description
    infoActions.editDescription(ID, description["description"])
    return responseHandling.success("Description edited")


@router.put("/information/editFull/{ID}")
async def editFull(ID: int, request: Request):
    # Check if the ID exists
    if ID not in infoConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not found")

    # Get the full information
    fullInformation = await request.json()
    if "knownCharacter" not in fullInformation:
        return responseHandling.errorIncorrectParameter(
            "knownCharacter parameter not found")
    if "aboutCharacter" not in fullInformation:
        return responseHandling.errorIncorrectParameter(
            "aboutCharacter parameter not found")
    if "description" not in fullInformation:
        return responseHandling.errorIncorrectParameter(
            "description parameter not found")

    # Edit the full information
    infoActions.editFullInformation(ID, fullInformation["knownCharacter"],
                                    fullInformation["aboutCharacter"],
                                    fullInformation["description"])
    return responseHandling.success("Full information edited")
