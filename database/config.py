from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


SQLALCHEMY_DATABESE_URL = 'sqlite:///undefeel.db' or config(
    "DATABASE_URL"
)

engine = create_engine(SQLALCHEMY_DATABESE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

class Base(DeclarativeBase): pass

