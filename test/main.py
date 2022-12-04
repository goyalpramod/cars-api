from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import session_local
from typing import List
import models

app = FastAPI()


class Car(BaseModel):
    id: int
    name: str
    make: str
    horsepower: int
    color: str

    class Config:
        orm_mode = True


db = session_local()


@app.get("/cars", response_model=List[Car], status_code=200)
def get_all_cars():
    cars = db.query(models.Car).all()
    return cars


@app.get("/car/{car_id}", response_model=Car, status_code=200)
def get_a_car(car_id: int):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    return car


@app.post("/cars", response_model=Car, status_code=201)
def create_a_car(car: Car):
    new_car = models.Car(
        id=car.id,
        name=car.name,
        make=car.make,
        horsepower=car.horsepower,
        color=car.color,
    )

    db_item = db.query(models.Car).filter(car.name == new_car.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Car already exists")

    db.add(new_car)
    db.commit()

    return new_car


@app.put("/car/{car_id}", response_model=Car, status_code=200)
def update_a_car(car_id: int,car:Car):
    car_to_update = db.query(models.Car).filter(models.Car.id == car_id).first()
    car_to_update.name = car.name
    car_to_update.make = car.make
    car_to_update.horsepower = car.horsepower
    car_to_update.color = car.color

    db.commit()

    return car_to_update



@app.delete("/car/{car_id}")
def delete_a_car(car_id: int):
    pass
