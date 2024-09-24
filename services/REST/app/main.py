from fastapi import FastAPI
from web.routes import router
from data.database import init_db

app = FastAPI()

init_db()

app.include_router(router)
