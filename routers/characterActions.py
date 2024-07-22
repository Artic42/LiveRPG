from fastapi import APIRouter
from pydantic import BaseModel
import routers.responseHandling as responseHandling
import databaseManager.characterActions as characterActions
import databaseManager.characterConsults as characterConsults

router = APIRouter()

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

@router.put("/character/editBackground/{ID}/{background}")
def editBackground(ID: int, background: str):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Edit the background
    characterActions.editBackground("/Database.db", ID, background)
    
    # Return success
    return responseHandling.success("Background edited")

@router.put("/character/editMainObjective/{ID}/{mainObjective}")
def editMainObjective(ID: int, mainObjective: str):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Edit the main objective
    characterActions.editMainObjective("/Database.db", ID, mainObjective)
    
    # Return success
    return responseHandling.success("Main objective edited")

@router.put("/character/editSecondaryObjective/{ID}/{secondaryObjective}")
def editSecondaryObjective(ID: int, secondaryObjective: str):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Edit the secondary objective
    characterActions.editSecondaryObjective("/Database.db", ID, secondaryObjective)
    
    # Return success
    return responseHandling.success("Secondary objective edited")

@router.put("/character/editLoseCondition/{ID}/{loseCondition}")
def editLoseCondition(ID: int, loseCondition: str):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter("ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")
    
    # Edit the lose condition
    characterActions.editLoseCondition("/Database.db", ID, loseCondition)
    
    # Return success
    return responseHandling.success("Lose condition edited")

   