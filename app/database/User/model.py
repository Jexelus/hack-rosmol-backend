import json
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
DATABASE_URL = "postgresql://rosmol:rootroot@192.168.1.47:8001/rosmol"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    vk_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, primary_key=True)
    last_project_id = sqlalchemy.Column(sqlalchemy.Integer) 
    email = sqlalchemy.Column(sqlalchemy.String)
    fio = sqlalchemy.Column(sqlalchemy.String)
    competencies = sqlalchemy.Column(sqlalchemy.String)
    role = sqlalchemy.Column(sqlalchemy.String, default="user") # admin, expert, user
    complited_projects = sqlalchemy.Column(sqlalchemy.JSON, default="[]")
    invites = sqlalchemy.Column(sqlalchemy.JSON, default="[]")
    team_id = sqlalchemy.Column(sqlalchemy.Integer)

    def to_dict(self):
        return {
            "vk_id": self.vk_id,
            "last_project_id": self.last_project_id,
            "fio": self.fio,
            "email": self.email,
            "competencies": self.competencies,
            "complited_projects": json.loads(self.complited_projects),
            "role": self.role,
            "invites": json.loads(self.invites),
            "team_id": self.team_id
        }

Base.metadata.create_all(engine)