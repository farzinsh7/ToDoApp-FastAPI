from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.database import engine
from tasks.models import Todos


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Up... .")
    yield
    print("Shouting Down... .")


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}