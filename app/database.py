from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:admin@localhost/cardb", echo=True)


base = declarative_base()
session_local = sessionmaker(bind=engine)
