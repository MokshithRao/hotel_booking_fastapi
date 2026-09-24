from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey

class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, autoincrement=True)
    room_number = Column(Integer, unique=True, nullable=False)
    room_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String)


class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(
        Integer, 
        ForeignKey("customers.customer_id"),
        nullable=False
    )
    room_id = Column(
        Integer,
        ForeignKey("rooms.room_id"),
        nullable=False
    )
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    status = Column(String, default="Booked")




