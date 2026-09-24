from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./hotel_booking.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


LocalSession = sessionmaker(
    bind=engine,
    autoflush=True
)

Base = declarative_base()