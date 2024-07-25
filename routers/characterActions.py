from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
import routers.responseHandling as responseHandling
import databaseManager.characterActions as characterActions
import databaseManager.characterConsults as characterConsults

router = APIRouter()

@router.post("/character/create/{ID}")
def createCharacter(ID: int):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDAlreadyExists("ID already exists"))
    
    # Create the character
    characterActions.createCharacter("/Database.db", ID)
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Character created"))

@router.delete("/character/delete/{ID}")
def deleteCharacter(ID: int):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDNotPresent("ID not present"))
    
    # Delete the character
    characterActions.deleteCharacter("/Database.db", ID)
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Character deleted"))

@router.put("/character/editName/{ID}")
async def editName(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDNotPresent("ID not present"))
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "name" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No name specified"))   
    
    # Edit the name
    characterActions.editName("/Database.db", ID, body["name"])
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Name edited"))

@router.put("/character/editPlayer/{ID}")
async def editPlayer(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDNotPresent("ID not present"))
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "player" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No player specified"))
    
    # Edit the player
    characterActions.editPlayer("/Database.db", ID, body["player"])
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Player edited"))

@router.put("/character/editCharacteristics/{ID}")
async def editCharacteristics(ID:int,request: Request):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDNotPresent("ID not present"))
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "strength" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No strength specified"))
    if "medicine" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No medicine specified"))
    if "hacking" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No hacking specified"))
    
    # Get values from body and check limits
    strength = body["strength"]
    medicine = body["medicine"]
    hacking = body["hacking"]
    
    if strength < 0 or strength > 5:
        return JSONResponse(responseHandling.errorIncorrectParameter("Strength must be an integer between 0 and 5"))
    if medicine < 0 or medicine > 5:
        return JSONResponse(responseHandling.errorIncorrectParameter("Medicine must be an integer between 0 and 5"))
    if hacking < 0 or hacking > 5:
        return JSONResponse(responseHandling.errorIncorrectParameter("Hacking must be an integer between 0 and 5"))
    
    # Edit the characteristics
    characterActions.editCharacteristics("/Database.db", ID, strength, medicine, hacking)
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Characteristics edited"))

@router.put("/character/editBackground/{ID}")
async def editBackground(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDNotPresent("ID not present"))
    
    # Get body as json
    body = await request.json()
    
    # Check correct format of body
    if "background" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No background specified"))
    
    # Edit the background
    characterActions.editBackground("/Database.db", ID, body["background"])
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Background edited"))

@router.put("/character/editMainObjective/{ID}")
async def editMainObjective(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDNotPresent("ID not present"))
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "mainObjective" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No main objective specified"))
    
    # Edit the main objective
    characterActions.editMainObjective("/Database.db", ID, body["mainObjective"])
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Main objective edited"))

@router.put("/character/editSecondaryObjective/{ID}")
async def editSecondaryObjective(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDNotPresent("ID not present"))
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "secondaryObjective" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No secondary objective specified"))
    
    # Edit the secondary objective
    characterActions.editSecondaryObjective("/Database.db", ID, body["secondaryObjective"])
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Secondary objective edited"))

@router.put("/character/editLoseCondition/{ID}")
async def editLoseCondition(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDNotPresent("ID not present"))
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "loseCondition" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No lose condition specified"))
    
    # Edit the lose condition
    characterActions.editLoseCondition("/Database.db", ID, body["loseCondition"])
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Lose condition edited"))

@router.put("/character/edit/{ID}")
async def editFullCharacter(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return JSONResponse(responseHandling.errorIncorrectParameter("ID must be a positive integer"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return JSONResponse(responseHandling.errorIDNotPresent("ID not present"))
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "name" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No name specified"))
    if "player" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No player specified"))
    if "strength" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No strength specified"))
    if "medicine" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No medicine specified"))
    if "hacking" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No hacking specified"))
    if "background" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No background specified"))
    if "mainObjective" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No main objective specified"))
    if "secondaryObjective" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No secondary objective specified"))
    if "loseCondition" not in body:
        return JSONResponse(responseHandling.errorWrongFormatBody("No lose condition specified"))
    
    # Get values from body and check limits
    strength = body["strength"]
    medicine = body["medicine"]
    hacking = body["hacking"]
    
    if strength < 0 or strength > 5:
        return JSONResponse(responseHandling.errorIncorrectParameter("Strength must be an integer between 0 and 5"))
    if medicine < 0 or medicine > 5:
        return JSONResponse(responseHandling.errorIncorrectParameter("Medicine must be an integer between 0 and 5"))
    if hacking < 0 or hacking > 5:
        return JSONResponse(responseHandling.errorIncorrectParameter("Hacking must be an integer between 0 and 5"))
    
    
    # Edit the full character
    characterActions.editFullCharacter("/Database.db", ID,
                                       body["name"],
                                       body["player"],
                                       body["strength"],
                                       body["medicine"],
                                       body["hacking"],
                                       body["background"],
                                       body["mainObjective"],
                                       body["secondaryObjective"],
                                       body["loseCondition"])
    
    # return JSONResponse(success
    return JSONResponse(responseHandling.success("Character edited"))