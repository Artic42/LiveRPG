import uvicorn
from fastapi import FastAPI
import routers.characterActions as characterActions
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.include_router(characterActions.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)