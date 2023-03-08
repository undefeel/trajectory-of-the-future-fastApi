from fastapi import FastAPI
from database.config import engine, SessionLocal
from models import models
from utils import csv_to_database

models.Base.metadata.create_all(bind=engine)
csv_to_database.to_db('utils/data.csv', SessionLocal())

app = FastAPI(
    title='Trajectory of the future',
    version='1.0.0'
)


