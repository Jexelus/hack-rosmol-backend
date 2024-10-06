import json
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
DATABASE_URL = "postgresql://rosmol:rootroot@192.168.1.47:8001/rosmol"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Team(Base):
    __tablename__ = "team"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    leader_id = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.String)
    members = sqlalchemy.Column(sqlalchemy.JSON) # members = json.dumps(members) | {1: vk_id, 3: vk_id}
    projects = sqlalchemy.Column(sqlalchemy.JSON)
    last_project_id = sqlalchemy.Column(sqlalchemy.Integer)
    invites = sqlalchemy.Column(sqlalchemy.JSON)


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "team_lead_id": self.team_lead_id,
            "members": json.loads(self.members),
            "projects": json.loads(self.projects),
            "last_project_id": self.last_project_id,
            "invites": json.loads(self.invites)
        }

Base.metadata.create_all(engine)