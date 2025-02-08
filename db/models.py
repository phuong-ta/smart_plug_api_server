from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from db.db import DATABASE_URL
from datetime import datetime
import os


# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Base class for SQLAlchemy models
Base = declarative_base()

# Define the Booking model (table)
class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, index=True)
    charger_id = Column(String, index=True)  # Assuming charger_id is a string, can be Integer if needed
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # Create the table in the database
    def create_table():
        Base.metadata.create_all(bind=engine)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create CRUD operations

# 1. Create - Add a new booking
def create_booking(db_session, charger_id: str, start_time: datetime, end_time: datetime):
    new_booking = Booking(charger_id=charger_id, start_time=start_time, end_time=end_time)
    db_session.add(new_booking)
    db_session.commit()
    db_session.refresh(new_booking)
    return new_booking

# 2. Read - Get booking by ID
def get_booking_by_id(db_session, booking_id: int):
    return db_session.query(Booking).filter(Booking.id == booking_id).first()

# 3. Read - Get all bookings
def get_all_bookings(db_session):
    return db_session.query(Booking).all()

# 4. Update - Update an existing booking
def update_booking(db_session, booking_id: int, charger_id: str = None, start_time: datetime = None, end_time: datetime = None):
    booking = db_session.query(Booking).filter(Booking.id == booking_id).first()
    
    if charger_id:
        booking.charger_id = charger_id
    if start_time:
        booking.start_time = start_time
    if end_time:
        booking.end_time = end_time
    
    db_session.commit()
    db_session.refresh(booking)
    return booking

# 5. Delete - Delete a booking by ID
def delete_booking(db_session, booking_id: int):
    booking = db_session.query(Booking).filter(Booking.id == booking_id).first()
    if booking:
        db_session.delete(booking)
        db_session.commit()
        return True
    return False

