from contextlib import asynccontextmanager
import os

from beanie import init_beanie
import motor
from fastapi import FastAPI


async def configure_routing(app: FastAPI):
    """Configure routing for the application."""

    # app.include_router(your_router)  # 🚨 ADD YOUR ROUTERS HERE
    ...


async def configure_mongo():
    """Configure MongoDB connection."""

    database = os.getenv("MONGO_DATABASE")

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
    await configure_routing(app=app)

    yield  # This is where the application runs

    # This is everything that happens when the application stops
    # your cleanup code here...


app = FastAPI(lifespan=lifespan)
