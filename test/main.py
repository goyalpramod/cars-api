from fastapi import FastAPI
from pydantic import BaseModel
from database import session_local
from typing import List

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


@app.get("/cars",response_model=List[Car],status_code=200)
def get_all_cars():
    pass


@app.get("/car/{car_id}")
def get_a_car(item_id: int):
    pass


@app.post("cars")
def create_a_car():
    pass


@app.put("/item/{item_id}")
def update_a_car(item_id: int):
    pass


@app.delete("/item/{item_id}")
def delete_a_car(item_id: int):
    pass


# @app.put("/car/{car_id}")
# def update_car(car_id: int, car: Car):
#     return {
#         "name": car.name,
#         "make": car.make,
#         "horsepower": car.horsepower,
#         "color": car.color,
#     }
