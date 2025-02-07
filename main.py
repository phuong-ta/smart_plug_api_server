from typing import Optional
from contextlib import asynccontextmanager
import asyncio
import os

from fastapi import FastAPI
from databases import Database

from routers.price_router import price_router
from routers.booking_router import booking_router
#from .db.db import database

from.db.models import Booking


DATABASE_URL = os.getenv("DB_INTERNAL_URL")
database = Database(DATABASE_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Connect to the database asynchronously
        await database.connect()
        Booking.create_table()
        print("Connected to the database")
        yield
    except Exception as e:
        print(f"Error while connecting: {e}")
    finally:
        # Disconnect from the database asynchronously
        await database.disconnect()
        print("Disconnected from the database")


app = FastAPI(lifespan=lifespan)

app.include_router(price_router)
app.include_router(booking_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}