import os
import time
import uvicorn
import asyncio
import random
from fastapi import FastAPI
from fastapi import Request
from fastapi import UploadFile
from fastapi import File
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import routers.characterActions as characterActions
import routers.characterConsults as characterConsults
import routers.eventActions as eventActions
import routers.eventConsults as eventConsults
import routers.informationActions as informationActions
import routers.informationConsults as informationConsults
import routers.responseHandling as responseHandling
import routers.mockBomb as mockBomb
import databaseManager.userConsults as userConsults
from fastapi.middleware.cors import CORSMiddleware
import shutil
import ntfy

app = FastAPI()

app.include_router(characterActions.router)
app.include_router(characterConsults.router)
app.include_router(eventConsults.router)
app.include_router(eventActions.router)
app.include_router(informationActions.router)
app.include_router(informationConsults.router)
app.include_router(mockBomb.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/about")
def read_root():
    return {"Version": "0.1",
            "AppName": "LiveRPG",
            "Description": """This is the API for the LiveRPG project.
            It is a project to create a live RPG game using
            FastAPI and WebSockets."""}


@app.post("/activateTestMode")
def activateTestMode():
    shutil.copyfile("Database.db", "ProductionDatabase.db")
    shutil.copyfile("TestDatabase.db", "Database.db")


@app.post("/deactivateTestMode")
def deactivateTestMode():
    shutil.copyfile("ProductionDatabase.db", "Database.db")


@app.get("/downloadDatabase")
def downloadDatabase():
    return FileResponse("/Database/Database.db", filename="Database.db", media_type="application/octet-stream")


@app.post("/uploadDatabase")
async def upload_file(file: UploadFile = File(...)):
    file_location = "/Database/Database.db"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"File '{file.filename}' saved as '{file_location}'"}


@app.post("/login")
async def login(request: Request):
    body = await request.json()

    if "username" not in body:
        return responseHandling.errorWrongFormatBody("Username not present")
    if "password" not in body:
        return responseHandling.errorWrongFormatBody("Password not present")

    username = body["username"]
    password = body["password"]

    if username == "root" and password == "root":
        return JSONResponse({
            "status": 200,
            "characterID": -1
        })

    ID = userConsults.getID("/Database/Database.db", username)
    if ID == 0:
        return responseHandling.errorWrongCredentials()

    savedPassword = userConsults.readPassword("/Database/Database.db", ID)

    if savedPassword == password:
        characterID = userConsults.readCharacter("/Database/Database.db", ID)
        return JSONResponse({
            "status": 200,
            "characterID": characterID
        })

    return responseHandling.errorWrongCredentials()


@app.get("/roll/{dice}")
def rollDice(dice: int):
    result = 0
    diceResults = []
    for i in range(dice):
        random.seed()
        diceResult = random.randint(1, 6)
        diceResults.append(diceResult)
        if diceResult >= 5:
            result += 1
    return JSONResponse({
        "status": 200,
        "diceResults": diceResults,
        "result": result
    })


# Function to run every 10 seconds
async def runEvery10Seconds():
    while True:
        if os.path.exists("/bombArmed"):
            file = open("/lastAccess", "r")
            value = int(file.read())
            file.close()
            currentTime = int(time.time())
            if currentTime - value > 10:
                ntfy.sendExplosionNtfy()
                os.system("touch /exploded")
                os.system("rm /bombArmed")
                os.system("rm /lastAccess")
        # Add your task logic here
        await asyncio.sleep(10)


# Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    task = asyncio.create_task(runEvery10Seconds())
    yield
    # Teardown logic
    task.cancel()
    await task

app.router.lifespan_context = lifespan


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
