from pydantic import BaseModel
from datetime import datetime

class BookingBase(BaseModel):
    charger_id: int
    booking_time: datetime
    device_state: bool

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True