from sqlalchemy.orm import Session
from sqlalchemy import DateTime, desc, asc

from . import models
from . import schemas
from datetime import datetime, timezone
import pytz



def get_booking_by_id(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.id == booking_id).first()

def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    finland_tz = pytz.timezone("Europe/Helsinki")  # Define Finland timezone
    current_time = datetime.now(finland_tz)  # Get current local time in Finland
    return (
        db.query(models.Booking)
        .filter(models.Booking.booking_time > current_time)
        .order_by(asc(models.Booking.booking_time))  # Order by soonest bookings first
        .offset(skip)
        .limit(limit)
        .all()
    )

def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def update_booking(db: Session, booking_id: int, booking: schemas.BookingCreate):
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if db_booking:
        db_booking.charger_id = booking.charger_id
        db_booking.booking_time = booking.booking_time
        db_booking.device_state = booking.device_state
        db.commit()
        db.refresh(db_booking)
    return db_booking

def delete_booking(db: Session, booking_id: int):
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if db_booking:
        db.delete(db_booking)
        db.commit()
    return db_booking
