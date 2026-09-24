from fastapi import FastAPI
from database import Base, engine, LocalSession
from schemas import Customer, Room, Booking
import models


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/customers")
def add_customer(customer: Customer):
    db = LocalSession()

    new_customer = models.Customer(
        name = customer.name,
        phone = customer.phone,
        email = customer.email
    )

    db.add(new_customer)
    db.commit()
    db.close()

    return "Customer added successfully"


@app.get("/customers")
def get_customers():
    db = LocalSession()

    all_customers = db.query(models.Customer).all()

    db.close()

    return all_customers


@app.post("/rooms")
def create_room(room: Room):
    db = LocalSession()

    new_room = models.Room(
        room_number = room.room_number,
        room_type = room.room_type,
        price = room.price
    )

    db.add(new_room)
    db.commit()
    db.close()

    return "Room added successfully"


@app.get("/rooms")
def get_rooms():
    db = LocalSession()

    all_rooms = db.query(models.Room).all()

    db.close()

    return all_rooms


@app.post("/bookings")
def create_booking(booking: Booking):
    db = LocalSession()

    customer = db.query(models.Customer).filter(
        models.Customer.customer_id == booking.customer_id
    ).first()

    if customer == None:
        return "Customer Does not exist, enter valid customer ID"

    room = db.query(models.Room).filter(
        models.Room.room_id == booking.room_id
    ).first()

    if room == None:
        return "Room not exist, enter valid room ID"

    if room.is_available == False:
        return "Room not available"

    new_booking = models.Booking(
        customer_id = booking.customer_id,
        room_id = booking.room_id,
        check_in = booking.check_in,
        check_out =booking.check_out
    )

    db.add(new_booking)
    room.is_available = False
    db.commit()
    db.close()

    return "Booking added successfully"



@app.get("/bookings")
def get_bookings():
    db = LocalSession()

    all_bookings = db.query(models.Booking).all()

    db.close()

    return all_bookings