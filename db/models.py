from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from db.db import DATABASE_URL
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


