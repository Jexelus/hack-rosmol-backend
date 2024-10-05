import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_to_pydantic import sqlalchemy_to_pydantic

Base = declarative_base()

DATABASE_URL = "postgresql://rosmol:rootroot@192.168.1.47:8001/rosmol"

from database.User.model import User
from database.Ideas.model import Idea

pdUser = sqlalchemy_to_pydantic(User, exclude=['role'])
pdIdea = sqlalchemy_to_pydantic(Idea)


engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
new_session = sessionmaker(engine, expire_on_commit=False)