from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
import routers.responseHandling as responseHandling
import databaseManager.eventActions as eventActions
import databaseManager.eventConsults as eventConsults

router = APIRouter()


@router.post("/create/{ID}")
def createEvent(request: Request, ID: int):
    # Check for errors
    if ID in eventConsults.getAllIDs():
        return responseHandling.errorIDAlreadyExists("ID already exists")
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID cannot be negative")

    # Create event
    eventActions.createEvent(ID)
    return JSONResponse(responseHandling.success("Event created"))


@router.delete("/delete/{ID}")
def deleteEvent(request: Request, ID: int):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID cannot be negative")

    # Delete event
    eventActions.deleteEvent(ID)
    return JSONResponse(responseHandling.success("Event deleted"))


@router.put("/event/editDescription{ID}")
def editEventName(request: Request, ID: int):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID cannot be negative")

    # Extract body as json
    body = request.json()

    # Check format
    if "description" not in body:
        responseHandling.errorIncorrectParameter("No description in body")

    eventActions.editDescription("/Database.db", ID, body["description"])
    return JSONResponse(responseHandling.success("Description updated"))


@router.put("/event/editFlags/{ID}")
def editEventFlags(ID: int, request: Request):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID cannot be negative")

    # Extract body as json
    body = request.json()

    # Checking format
    if "hacking" not in body:
        responseHandling.errorWrongFormatBody("Hacking not present")
    if "equip" not in body:
        responseHandling.errorWrongFormatBody("Equip not in body")
    if "activate" not in body:
        responseHandling.errorWrongFormatBody("Activate not in body")
    if "wait" not in body:
        responseHandling.errorWrongFormatBody("Wait not in body")

    # Edit flags on database
    eventActions.editFlags("/Database.db", ID,
                           body["hacking"],
                           body["equip"],
                           body["activate"],
                           body["wait"])

    return responseHandling.success("Flags updated")


@router.put("/event/activate/{ID}")
def activateEvent(ID: int):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID cannot be negative")

    # Activate event
    eventActions.setActivated("/Database.db", ID)
    return responseHandling.success("Event activated")


@router.put("/event/deactivate/{ID}")
def deactivateEvent(ID: int):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID cannot be negative")

    # Activate event
    eventActions.resetActivated("/Database.db", ID)
    return responseHandling.success("Event deactivated")


@router.put("/event/editRedirect/{ID}")
def editRedirectID(ID: int, request: Request):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID cannot be negative")

    # Extract body as json
    body = request.json()

    # Checking format
    if "redirectID" not in body:
        responseHandling.errorWrongFormatBody("Redirect ID not present")

    # Edit redirect Id on database
    eventActions.editRedirectID("/Database.db", ID, body["redirectID"])


@router.put("/event/editEvent/{ID}")
def editEvent(ID: int, request: Request):
    # Check for errors
    if ID not in eventConsults.getAllIDs():
        return responseHandling.errorIDNotPresent("ID not present")
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID cannot be negative")

    # Extract body as json
    body = request.json()

    # Checking format
    if "description" not in body:
        responseHandling.errorWrongFormatBody("Description not in body")
    if "hacking" not in body:
        responseHandling.errorWrongFormatBody("Hacking not present")
    if "equip" not in body:
        responseHandling.errorWrongFormatBody("Equip not in body")
    if "activate" not in body:
        responseHandling.errorWrongFormatBody("Activate not in body")
    if "wait" not in body:
        responseHandling.errorWrongFormatBody("Wait not in body")
    if "redirectID" not in body:
        responseHandling.errorWrongFormatBody("Redirect ID not present")
    if "activated" not in body:
        responseHandling.errorWrongFormatBody("Activated not in body")

    # Edit event on database
    eventActions.editFullEvent("/Database.db",
                               ID,
                               body["description"],
                               body["hacking"],
                               body["equip"],
                               body["activate"],
                               body["wait"],
                               body["activated"],
                               body["redirectID"])
    return responseHandling.success["Event updated"]
