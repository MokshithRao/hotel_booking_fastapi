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