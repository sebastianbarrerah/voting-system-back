
from app.config import database_url
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


database = database_url()

engine = create_engine(database)
Base = declarative_base()




