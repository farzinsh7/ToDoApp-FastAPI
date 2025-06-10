from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.database import engine
from tasks.models import Todos
from tasks.routes import router as todos_list


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Up... .")
    yield
    print("Shouting Down... .")


app = FastAPI()

app.include_router(todos_list)



@app.get("/")
async def root():
    return {"message": "Hello World"}