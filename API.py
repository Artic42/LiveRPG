import uvicorn
from fastapi import FastAPI
import routers.characterActions as characterActions
import routers.characterConsults as characterConsults
from fastapi.middleware.cors import CORSMiddleware
import shutil

app = FastAPI()

app.include_router(characterActions.router)
app.include_router(characterConsults.router)

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
            "AppName" : "LiveRPG",
            "Description": "This is the API for the LiveRPG project. It is a project to create a live RPG game using FastAPI and WebSockets."}

@app.post("/activateTestMode")
def activateTestMode():
    shutil.copyfile("Database.db", "ProductionDatabase.db")
    shutil.copyfile("TestDatabase.db", "Database.db")
    
@app.post("/deactivateTestMode")
def deactivateTestMode():
    shutil.copyfile("ProductionDatabase.db", "Database.db")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)