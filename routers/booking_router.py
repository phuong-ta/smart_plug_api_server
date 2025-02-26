from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.booking import schemas
from db.booking import booking_crud
from db.database import get_db

booking_router = APIRouter(prefix="/bookings", tags=["bookings"])

# Create a new booking
@booking_router.post("/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return booking_crud.create_booking(db=db, booking=booking)

# Get all bookings
@booking_router.get("/", response_model=list[schemas.Booking])
def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = booking_crud.get_bookings(db, skip=skip, limit=limit)
    return bookings

# Get a specific booking by ID
@booking_router.get("/{booking_id}", response_model=list[schemas.Booking])
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = booking_crud.get_booking_by_id(db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

# Update a booking
@booking_router.put("/{booking_id}", response_model=schemas.Booking)
def update_booking(booking_id: int, booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    db_booking = booking_crud.update_booking(db, booking_id=booking_id, booking=booking)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

# Delete a booking
@booking_router.delete("/{booking_id}", response_model=schemas.Booking)
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = booking_crud.delete_booking(db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

# Get a newest booking by ID
@booking_router.get("/newest/{charger_id}", response_model=schemas.Booking)
def read_booking(charger_id: int, db: Session = Depends(get_db)):
    booking = booking_crud.get_newest_booking_by_id(db, charger_id=charger_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@booking_router.get("/nearest/{charger_id}", response_model=schemas.Booking)
def get_nearest_booking(charger_id: int, db: Session = Depends(get_db)):
    booking = booking_crud.get_nearest_booking_by_charger_id(db, charger_id=charger_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

