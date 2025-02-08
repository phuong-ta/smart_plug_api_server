from models import Booking
from datetime import datetime


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
