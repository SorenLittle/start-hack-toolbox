from contextlib import asynccontextmanager
import os
from pathlib import Path

from beanie import init_beanie
from fastapi.staticfiles import StaticFiles
import motor
from fastapi import FastAPI

from .frontend.routes.home import router as home_router


async def configure_routing(app: FastAPI):
    """Configure routing for the application."""

    app.include_router(home_router)


async def configure_static(app: FastAPI):
    """Configure static files for the application."""

    static_directory = Path(__file__).parent / "frontend" / "static"
    app.mount("/static", StaticFiles(directory=static_directory), name="static")


async def configure_mongo():
    """Configure MongoDB connection."""

    database = os.getenv("MONGO_DB")

    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://mongodb:27017/{database}"
    )

    await init_beanie(
        database=client[database],
        document_models=[],  # 🚨 ADD YOUR BEANIE MODELS HERE
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager."""

    # This is everything that happens when the application starts
    await configure_mongo()
    await configure_static(app=app)
    await configure_routing(app=app)

    yield  # This is where the application runs

    # This is everything that happens when the application stops
    # your cleanup code here...


app = FastAPI(lifespan=lifespan)
