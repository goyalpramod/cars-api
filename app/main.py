from fastapi import FastAPI, HTTPException
from app.database import session_local
from typing import List
from app.models import db_models
from app.models.models import Car
import uvicorn

app = FastAPI()

db = session_local()


@app.get("/cars", response_model=List[Car], status_code=200)
async def get_all_cars() -> List[Car]:
    cars = db.query(db_models.Car).all()
    return cars


@app.get("/car/{car_id}", response_model=Car, status_code=200)
async def get_a_car(car_id: int) -> Car:
    car = db.query(db_models.Car).filter(db_models.Car.id == car_id).first()
    return car


@app.post("/cars", response_model=Car, status_code=201)
async def create_a_car(car: Car) -> Car:
    db_item = db.query(db_models.Car).filter(db_models.Car.name == car.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Car already exists")

    new_car = db_models.Car(
        id=car.id,
        name=car.name,
        make=car.make,
        horsepower=car.horsepower,
        color=car.color,
    )

    db.add(new_car)
    db.commit()

    return new_car


@app.put("/car/{car_id}", response_model=Car, status_code=200)
async def update_a_car(car_id: int, car: Car) -> Car:
    car_to_update = db.query(db_models.Car).filter(db_models.Car.id == car_id).first()
    car_to_update.name = car.name
    car_to_update.make = car.make
    car_to_update.horsepower = car.horsepower
    car_to_update.color = car.color

    db.commit()

    return car_to_update


@app.delete("/car/{car_id}", status_code=202)
async def delete_a_car(car_id: int) -> dict:
    car_to_delete = db.query(db_models.Car).filter(db_models.Car.id == car_id).first()

    if car_to_delete is None:
        raise HTTPException(status_code=404, detail="Resources not found")

    db.delete(car_to_delete)
    db.commit()

    return {"message": "data successfully deleted"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8080, reload=True, debug=True, workers=3)