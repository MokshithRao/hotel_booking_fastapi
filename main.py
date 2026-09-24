from fastapi import FastAPI
from database import Base, engine, LocalSession
from schemas import Customer
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

