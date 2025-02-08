from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from db.models import Booking, SessionLocal, create_booking, get_booking_by_id, get_all_bookings, update_booking, delete_booking

# Initialize the APIRouter for bookings
booking_router = APIRouter()

# Dependency to get the database session
def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

# 1. Create a new booking
@booking_router.post("/bookings/", response_model=Booking)
def create_booking_endpoint(charger_id: str, start_time: datetime, end_time: datetime, db: Session = Depends(get_db)):
    new_booking = create_booking(db, charger_id, start_time, end_time)
    return new_booking

# 2. Get a booking by ID
@booking_router.get("/bookings/{booking_id}", response_model=Booking)
def get_booking_endpoint(booking_id: int, db: Session = Depends(get_db)):
    booking = get_booking_by_id(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

# 3. Get all bookings
@booking_router.get("/bookings/", response_model=List[Booking])
def get_all_bookings_endpoint(db: Session = Depends(get_db)):
    bookings = get_all_bookings(db)
    return bookings

# 4. Update a booking by ID
@booking_router.put("/bookings/{booking_id}", response_model=Booking)
def update_booking_endpoint(booking_id: int, charger_id: str = None, start_time: datetime = None, end_time: datetime = None, db: Session = Depends(get_db)):
    updated_booking = update_booking(db, booking_id, charger_id, start_time, end_time)
    if not updated_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return updated_booking

# 5. Delete a booking by ID
@booking_router.delete("/bookings/{booking_id}")
def delete_booking_endpoint(booking_id: int, db: Session = Depends(get_db)):
    success = delete_booking(db, booking_id)
    if not success:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted successfully"}
