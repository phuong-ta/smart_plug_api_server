from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from ..database import Base, engine

# Define the Booking model (table)
class EnergyReport(Base):
    __tablename__ = 'energy_report'

    id = Column(Integer, primary_key=True, index=True)
    charger_id = Column(String, index=True)  # Assuming charger_id is a string, can be Integer if needed
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    energy_consume = Column(Float)
    price = Column(Float)

# Create the table in the database
    def create_energy_table():
        Base.metadata.create_all(bind=engine)