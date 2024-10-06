import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_to_pydantic import sqlalchemy_to_pydantic

Base = declarative_base()

DATABASE_URL = "postgresql://rosmol:rootroot@192.168.1.47:8001/rosmol"

from database.User.model import User
from database.Project.model import Project
from database.Team.model import Team

pdUser = sqlalchemy_to_pydantic(User, exclude=['role'])
pdProject = sqlalchemy_to_pydantic(Project)
pdTeam = sqlalchemy_to_pydantic(Team)


engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
new_session = sessionmaker(engine, expire_on_commit=False)