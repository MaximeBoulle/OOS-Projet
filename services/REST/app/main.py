from fastapi import FastAPI
import sys
sys.path.append("services/REST/app")
from web.routes import router
from data.database import init_db

app = FastAPI()

init_db()

app.include_router(router)

@app.get("/")
async def root():
    return {"Welcome to the FastAPI Library!"}