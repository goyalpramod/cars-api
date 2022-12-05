from app.database import base,engine

print("Creating database")

base.metadata.create_all(engine)
