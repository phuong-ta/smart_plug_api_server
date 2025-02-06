from fastapi import APIRouter, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

# Define the APIRouter object
booking_router = APIRouter()

# Define a Pydantic model for the booking
class Booking(BaseModel):
    id: int
    charger_id: int
    user_id: int
    start_time: datetime
    end_time: datetime

# In-memory storage for bookings
bookings = []

# Create a new booking
@booking_router.post("/booking", response_model=Booking)
async def create_booking(booking: Booking):
    bookings.append(booking)
    return booking

# Read all bookings
@booking_router.get("/booking", response_model=List[Booking])
async def get_bookings():
    return bookings

# Read a specific booking by ID
@booking_router.get("/booking/{booking_id}", response_model=Booking)
async def get_booking(booking_id: int):
    for booking in bookings:
        if booking.id == booking_id:
            return booking
    raise HTTPException(status_code=404, detail="Booking not found")

# Update a booking by ID
@booking_router.put("/booking/{booking_id}", response_model=Booking)
async def update_booking(booking_id: int, updated_booking: Booking):
    for index, booking in enumerate(bookings):
        if booking.id == booking_id:
            bookings[index] = updated_booking
            return updated_booking
    raise HTTPException(status_code=404, detail="Booking not found")

# Delete a booking by ID
@booking_router.delete("/booking/{booking_id}", response_model=Booking)
async def delete_booking(booking_id: int):
    for index, booking in enumerate(bookings):
        if booking.id == booking_id:
            deleted_booking = bookings.pop(index)
            return deleted_booking
    raise HTTPException(status_code=404, detail="Booking not found")