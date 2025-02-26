from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from ..database import Base, engine

Base = declarative_base()

# Define the EnergyReport model (table)
class EnergyReport(Base):
    __tablename__ = 'energy_report'

    id = Column(Integer, primary_key=True, index=True)
    charger_id = Column(String, index=True)  # Assuming charger_id is a string
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    energy_consume = Column(Float)  # Correct declaration
    price = Column(Float)

# Function to create table
def create_energy_table():
    Base.metadata.create_all(bind=engine)
