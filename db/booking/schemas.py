from pydantic import BaseModel
from datetime import datetime

class BookingBase(BaseModel):
    charger_id: int
    start_time: datetime
    end_time: datetime

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True