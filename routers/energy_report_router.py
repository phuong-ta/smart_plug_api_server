from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from db.energy import energy_curd
from db.energy import schemas

from datetime import datetime


energy_router = APIRouter(prefix="/energy_reports", tags=["energy_reports"])

# Create a new energy report
@energy_router.post("/", response_model=schemas.EnergyReport)
def create_energy_report(report: schemas.EnergyReportCreate, db: Session = Depends(get_db)):
    return energy_curd.create_energy_report(db=db, report=report)

# Get all energy reports
@energy_router.get("/", response_model=list[schemas.EnergyReport])
def read_energy_reports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reports = energy_curd.get_energy_reports(db, skip=skip, limit=limit)
    return reports
    # get_energy_reports(db, skip=skip, limit=limit)


# Get a specific energy report by ID
@energy_router.get("/{report_id}", response_model=list[schemas.EnergyReport])
def read_energy_report(report_id: int, db: Session = Depends(get_db)):
    db_report = energy_curd.get_energy_report_by_id(db, report_id=report_id)
    if db_report is None:
        raise HTTPException(status_code=404, detail="Energy Report not found")
    return db_report



# Get reports by charger ID
@energy_router.get("/charger/{charger_id}", response_model=list[schemas.EnergyReport])
def read_reports_by_charger_id(charger_id: int, db: Session = Depends(get_db)):
    return energy_curd.get_reports_by_charger_id(db, charger_id=charger_id)


# Get a specific energy report by ID
@energy_router.get("/energy_consumption/{charger_id}", response_model=list[schemas.EnergyReport])
def read_reports_by_charger_id(charger_id: int, db: Session = Depends(get_db)):
    charger_report = energy_curd.get_reports_by_charger_id(db, charger_id=charger_id)
    if charger_report is None:
        raise HTTPException(status_code=404, detail="Energy Report not found")

    # Get the current month and year
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Initialize total energy consumption for the current month
    total_energy_current_month = 0

    # Iterate over each record in the data
    for record in charger_report:
        # Parse the start time to a datetime object
        start_time = datetime.fromisoformat(record["start_time"])

        # Check if the record is in the current month and year
        if start_time.year == current_year and start_time.month == current_month:
            # Add the energy consumption to the total
            total_energy_current_month += record["energy_consume"]

    return total_energy_current_month