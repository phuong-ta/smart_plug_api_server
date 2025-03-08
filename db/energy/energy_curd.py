from sqlalchemy.orm import Session
from datetime import datetime, timezone
from sqlalchemy import func, extract, cast, String, Integer

from . import models, schemas


def create_energy_report(db: Session, report: schemas.EnergyReportCreate):
    new_report = models.EnergyReport(**report.dict())
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report


def get_energy_reports(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.EnergyReport).offset(skip).limit(limit).all()


def get_energy_report_by_id(db: Session, report_id: int):
    return db.query(models.EnergyReport).filter(cast(models.EnergyReport.id, Integer) == int(report_id)).all()


def update_energy_report(db: Session, report_id: int, report: schemas.EnergyReportCreate):
    db_report = db.query(models.EnergyReport).filter(cast(models.EnergyReport.id, Integer) == int(report_id)).first()
    if db_report:
        db_report.charger_id = report.charger_id
        db_report.start_time = report.start_time
        db_report.end_time = report.end_time
        db_report.energy_consume = report.energy_consume
        db_report.price = report.price
        db.commit()
        db.refresh(db_report)
    return db_report


def delete_energy_report(db: Session, report_id: int):
    report = db.query(models.EnergyReport).filter(cast(models.EnergyReport.id, Integer) == int(report_id)).first()
    if report:
        db.delete(report)
        db.commit()
    return report


# cast(models.EnergyReport.id, Integer) == int(report_id)

def get_reports_by_charger_id(db: Session, charger_id: int):
    return db.query(models.EnergyReport).filter(cast(models.EnergyReport.charger_id, String) == str(charger_id)).all()


def get_monthly_energy_consumption_by_id(db: Session, charger_id: int):
    # Get the current year and month
    current_year = datetime.now(timezone.utc).year
    current_month = datetime.now(timezone.utc).month

    total_energy = (
        db.query(func.sum(models.EnergyReport.energy_consume))
        .filter(
            cast(models.EnergyReport.charger_id, String) == str(charger_id),
            extract("year", models.EnergyReport.start_time) == current_year,
            extract("month", models.EnergyReport.start_time) == current_month
        )
        .scalar()
    )
    return total_energy if total_energy else 0.0
