from database import base,engine
from models import Car

print("Creating database")

base.metadata.create_all(engine)
