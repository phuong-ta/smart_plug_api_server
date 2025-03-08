from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean
from ..database import Base, engine

# Define the Booking model (table)
class Booking(Base):
    __tablename__ = 'booking_database'

    id = Column(Integer, primary_key=True, index=True)
    charger_id = Column(Integer, index=True)  # Assuming charger_id is a string, can be Integer if needed
    booking_time = Column(DateTime)
    device_state = Column(Boolean)

# Create the table in the database
    def create_table():
        Base.metadata.create_all(bind=engine)