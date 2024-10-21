from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_users.authentication import BearerTransport

from core.database import create_db_and_tables
from src.auth.routers import router as auth_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Not needed if you setup a migration system like Alembic

    print("Creating database tables")
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/auth")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
