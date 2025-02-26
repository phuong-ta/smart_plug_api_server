from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers.price_router import price_router
from routers.booking_router import booking_router
#from routers.energy_report_router import energy_router
from db.database import database
from db.energy.models import EnergyReport
from db.booking.models import Booking


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Connect to the database asynchronously
        await database.connect()
        #Booking.create_table()
        #EnergyReport.create_energy_table()
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
#app.include_router(energy_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}