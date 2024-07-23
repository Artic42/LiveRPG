from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel
import routers.responseHandling as responseHandling
import databaseManager.characterActions as characterActions
import databaseManager.characterConsults as characterConsults

router = APIRouter()

class textBlob(BaseModel):
    text: str
    test: int
    
class character(BaseModel):
    name: str
    player: str
    strength: int
    medicine: int
    hacking: int
    background: textBlob
    mainObjective: textBlob
    secondaryObjective: textBlob
    loseCondition: textBlob

@router.post("/character/create/{ID}")
def createCharacter(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDAlreadyExists("ID already exists")
    
    # Create the character
    characterActions.createCharacter("/Database.db", ID)
    
    # Return success
    return responseHandling.success("Character created")

@router.delete("/character/delete/{ID}")
def deleteCharacter(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    print (characterConsults.getAllIDs("/Database.db"))
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Delete the character
    characterActions.deleteCharacter("/Database.db", ID)
    
    # Return success
    return responseHandling.success("Character deleted")

@router.put("/character/editName/{ID}/{name}")
def editName(ID: int, name: str):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Edit the name
    characterActions.editName("/Database.db", ID, name)
    
    # Return success
    return responseHandling.success("Name edited")

@router.put("/character/editPlayer/{ID}/{player}")
def editPlayer(ID: int, player: str):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Edit the player
    characterActions.editPlayer("/Database.db", ID, player)
    
    # Return success
    return responseHandling.success("Player edited")

@router.put("/character/editCharacteristics/{ID}/strength{strength}/medicine{medicine}/hacking{hacking}")
def editCharacteristics(ID:int,strength:int,medicine:int,hacking:int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if strength < 0 or strength > 5:
        return responseHandling.errorIncorrectParameter("Strength must be an integer between 0 and 5")
    if medicine < 0 or medicine > 5:
        return responseHandling.errorIncorrectParameter("Medicine must be an integer between 0 and 5")
    if hacking < 0 or hacking > 5:
        return responseHandling.errorIncorrectParameter("Hacking must be an integer between 0 and 5")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Edit the characteristics
    characterActions.editCharacteristics("/Database.db", ID, strength, medicine, hacking)
    
    # Return success
    return responseHandling.success("Characteristics edited")

@router.put("/character/editBackground/{ID}")
async def editBackground(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Get body as json
    body = await request.json()
    
    # Check correct format of body
    if "background" not in body:
        return responseHandling.errorWrongFormatBody("No background specified")
    
    # Edit the background
    characterActions.editBackground("/Database.db", ID, body["background"])
    
    # Return success
    return responseHandling.success("Background edited")

@router.put("/character/editMainObjective/{ID}")
async def editMainObjective(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "mainObjective" in body:
        return responseHandling.errorWrongFormatBody("No main objective specified")
    
    # Edit the main objective
    characterActions.editMainObjective("/Database.db", ID, body["mainObjective"])
    
    # Return success
    return responseHandling.success("Main objective edited")

@router.put("/character/editSecondaryObjective/{ID}")
async def editSecondaryObjective(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "secondaryObjective" in body:
        return responseHandling.errorWrongFormatBody("No secondary objective specified")
    
    # Edit the secondary objective
    characterActions.editSecondaryObjective("/Database.db", ID, body["secondaryObjective"])
    
    # Return success
    return responseHandling.success("Secondary objective edited")

@router.put("/character/editLoseCondition/{ID}")
async def editLoseCondition(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "loseCondition" in body:
        return responseHandling.errorWrongFormatBody("No lose condition specified")
    
    # Edit the lose condition
    characterActions.editLoseCondition("/Database.db", ID, body["loseCondition"])
    
    # Return success
    return responseHandling.success("Lose condition edited")

router.get("/character/edit/{ID}")
async def editFullCharacter(ID: int, request: Request):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Extract body as json
    body = await request.json()
    
    # Check correct format of body
    if "name" not in body:
        return responseHandling.errorWrongFormatBody("No name specified")
    if "player" not in body:
        return responseHandling.errorWrongFormatBody("No player specified")
    if "strength" not in body:
        return responseHandling.errorWrongFormatBody("No strength specified")
    if "medicine" not in body:
        return responseHandling.errorWrongFormatBody("No medicine specified")
    if "hacking" not in body:
        return responseHandling.errorWrongFormatBody("No hacking specified")
    if "background" not in body:
        return responseHandling.errorWrongFormatBody("No background specified")
    if "mainObjective" not in body:
        return responseHandling.errorWrongFormatBody("No main objective specified")
    if "secondaryObjective" not in body:
        return responseHandling.errorWrongFormatBody("No secondary objective specified")
    if "loseCondition" not in body:
        return responseHandling.errorWrongFormatBody("No lose condition specified")
    
    
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
    
    # Return success
    return responseHandling.success("Character edited")