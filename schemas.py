from pydantic import BaseModel
from typing import Optional
from datetime import date

class Room(BaseModel):
    room_number: int
    room_type: str
    price: float

class Customer(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None

class Booking(BaseModel):
    customer_id: int
    room_id: int
    check_in: date
    check_out: date