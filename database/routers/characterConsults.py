from fastapi import APIRouter
from fastapi import Request
import routers.responseHandling as responseHandling
import databaseManager.characterConsults as characterConsults

router = APIRouter()


@router.get("/characters")
async def getCharacters(request: Request):
    IDs = characterConsults.getAllIDs("/Database/Database.db")
    response = {"status": 200}
    for ID in IDs:
        name = characterConsults.getCharacterName("/Database/Database.db", ID)
        response[ID] = name
    return response


@router.get("/character/{ID}")
async def getCharacter(request: Request, ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    name = characterConsults.getCharacterName("/Database/Database.db", ID)
    player = characterConsults.getCharacterPlayer("/Database/Database.db", ID)
    health = characterConsults.getCharacterHealth("/Database/Database.db", ID)
    strength = characterConsults.getCharacterStrength("/Database/Database.db", ID)
    medicine = characterConsults.getCharacterMedicine("/Database/Database.db", ID)
    hacking = characterConsults.getCharacterHacking("/Database/Database.db", ID)
    background = characterConsults.getCharacterBackground("/Database/Database.db", ID)
    mainObjective = characterConsults.getCharacterMainObjective(
        "/Database/Database.db", ID)
    secondaryObjective = characterConsults.getCharacterSecondaryObjective(
        "/Database/Database.db", ID)
    loseCondition = characterConsults.getCharacterLoseCondition(
        "/Database/Database.db", ID)

    return {"status": 200,
            "ID": ID,
            "Name": name,
            "Player": player,
            "Health": health,
            "Strength": strength,
            "Medicine": medicine,
            "Hacking": hacking,
            "Background": background,
            "MainObjective": mainObjective,
            "SecondaryObjective": secondaryObjective,
            "LoseCondition": loseCondition}


@router.get("/character/{ID}/name")
async def getCharacterName(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    return {"status": 200,
            "name": characterConsults.getCharacterName("/Database/Database.db", ID)}


@router.get("/character/{ID}/player")
async def getCharacterPlayer(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    return {"status": 200,
            "player": characterConsults.getCharacterPlayer("/Database/Database.db", ID)}


@router.get("/character/{ID}/health")
async def getCharacterHealth(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    health = characterConsults.getCharacterHealth("/Database/Database.db", ID)

    return {"status": 200,
            "health": health}


@router.get("/character/{ID}/strength")
async def getCharacterStrength(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    strength = characterConsults.getCharacterStrength("/Database/Database.db", ID)

    return {"status": 200,
            "strength": strength}


@router.get("/character/{ID}/medicine")
async def getCharacterMedicine(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    medicine = characterConsults.getCharacterMedicine("/Database/Database.db", ID)

    return {"status": 200,
            "medicine": medicine}


@router.get("/character/{ID}/hacking")
async def getCharacterHacking(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    hacking = characterConsults.getCharacterHacking("/Database/Database.db", ID)

    return {"status": 200,
            "hacking": hacking}


@router.get("/character/{ID}/background")
async def getCharacterBackground(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    background = characterConsults.getCharacterBackground("/Database/Database.db", ID)

    return {"status": 200,
            "background": background}


@router.get("/character/{ID}/mainObjective")
async def getCharacterMainObjective(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    mainObjective = characterConsults.getCharacterMainObjective("/Database/Database.db",
                                                                ID)

    return {"status": 200,
            "mainObjective": mainObjective}


@router.get("/character/{ID}/secondaryObjective")
async def getCharacterSecondaryObjective(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    secondaryObjective = characterConsults.getCharacterSecondaryObjective(
        "/Database/Database.db", ID)

    return {"status": 200,
            "secondaryObjective": secondaryObjective}


@router.get("/character/{ID}/loseCondition")
async def getCharacterLoseCondition(ID: int):
    # Check for errors
    if ID < 0:
        return responseHandling.errorIncorrectParameter(
            "ID must be a positive integer")
    if ID not in characterConsults.getAllIDs("/Database/Database.db"):
        return responseHandling.errorIDNotPresent("ID not present")

    loseCondition = characterConsults.getCharacterLoseCondition("/Database/Database.db",
                                                                ID)

    return {"status": 200,
            "loseCondition": loseCondition}
