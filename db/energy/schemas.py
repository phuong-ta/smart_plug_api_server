from pydantic import BaseModel
from datetime import datetime

class EnergyReportBase(BaseModel):
    charger_id: int
    start_time: datetime
    end_time: datetime
    energy_consume: float
    price: float

class EnergyReportCreate(EnergyReportBase):
    pass

class EnergyReport(EnergyReportBase):
    id: int

    class Config:
        orm_mode = True