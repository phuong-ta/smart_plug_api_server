from typing import Optional

from fastapi import FastAPI
from routers.price_router import price_router
from routers.booking_router import booking_router
#from .routers import electric_price



app = FastAPI()
app.include_router(price_router)
app.include_router(booking_router)
#app.include_router(electric_price.price_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
