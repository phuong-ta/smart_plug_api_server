from sqlalchemy.orm import Session
from sqlalchemy import DateTime, desc, asc

from . import models
from . import schemas
from datetime import datetime


def get_booking_by_id(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.id == booking_id).all()

def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()

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
        db_booking.start_time = booking.start_time
        db_booking.end_time = booking.end_time
        db.commit()
        db.refresh(db_booking)
    return db_booking

def delete_booking(db: Session, booking_id: int):
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if db_booking:
        db.delete(db_booking)
        db.commit()
    return db_booking

def get_newest_booking_by_id(db: Session, charger_id: int):
    return db.query(models.Booking).filter(models.Booking.charger_id == charger_id).order_by(desc(models.Booking.start_time)).first()

def get_nearest_booking_by_charger_id(db: Session, charger_id: int):
    return db.query(models.Booking)\
        .filter(models.Booking.charger_id == charger_id, models.Booking.start_time >= datetime.now())\
        .order_by(asc(models.Booking.start_time))\
        .first()