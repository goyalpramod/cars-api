from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Car(BaseModel):
    id: int
    name: str
    make: str
    horsepower: int
    color: str


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.put("/car/{car_id}")
def update_car(car_id: int, car: Car):
    return {
        "name": car.name,
        "make": car.make,
        "horsepower": car.horsepower,
        "color": car.color,
    }
