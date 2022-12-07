from pydantic import BaseModel


class Car(BaseModel):
    id: int
    name: str
    make: str
    horsepower: int
    color: str

    class Config:
        orm_mode = True
