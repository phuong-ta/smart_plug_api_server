from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from ..database import Base, engine

# Define the Booking model (table)
class Booking(Base):
    __tablename__ = 'booking_table'

    id = Column(Integer, primary_key=True, index=True)
    charger_id = Column(Integer, index=True)  # Assuming charger_id is a string, can be Integer if needed
    start_time = Column(DateTime)
    end_time = Column(DateTime)

# Create the table in the database
    def create_table():
        Base.metadata.create_all(bind=engine)