from app.database import base
from sqlalchemy import String, Integer, Column


class Car(base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    make = Column(String(255), nullable=True)
    horsepower = Column(Integer)
    color = Column(String(255))

    def __repr__(self):
        return f"Car name = {self.name}"
