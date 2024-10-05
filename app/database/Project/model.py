import json
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import datetime

DATABASE_URL = "postgresql://rosmol:rootroot@192.168.1.47:8001/rosmol"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Project(Base):

    __tablename__ = "projects"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    author_id = sqlalchemy.Column(sqlalchemy.Integer)
    creation_time_unix = sqlalchemy.Column(sqlalchemy.Integer) # дата создания в unix
    name = sqlalchemy.Column(sqlalchemy.String) # название
    category = sqlalchemy.Column(sqlalchemy.String) # категория
    region = sqlalchemy.Column(sqlalchemy.String) # регион
    logo = sqlalchemy.Column(sqlalchemy.String) # логотип
    contact_info = sqlalchemy.Column(sqlalchemy.String) # контактная информация
    project_scale = sqlalchemy.Column(sqlalchemy.String) # масштаб идеи
    project_start_time = sqlalchemy.Column(sqlalchemy.String) # начало реализации
    project_end_time = sqlalchemy.Column(sqlalchemy.String) # окончание реализации
    video_preview = sqlalchemy.Column(sqlalchemy.String) # превью видео
    roles = sqlalchemy.Column(sqlalchemy.JSON) # {{"1": "user", "2": "expert", "3": "user"}}
    mentors = sqlalchemy.Column(sqlalchemy.JSON) # { ["1", "2", "3"] } # id of Users
    description = sqlalchemy.Column(sqlalchemy.String) # описание
    issue_description = sqlalchemy.Column(sqlalchemy.String) # описание проблемы
    project_people_group_target = sqlalchemy.Column(sqlalchemy.String) # целевая группа людей
    project_target = sqlalchemy.Column(sqlalchemy.String) # целевое направление
    expireance_of_projects = sqlalchemy.Column(sqlalchemy.JSON) # { ["1", "2", "3"] } # id of projects
    perspective_of_project = sqlalchemy.Column(sqlalchemy.String) # основа идеи и её перспективы
    project_state = sqlalchemy.Column(sqlalchemy.String) # статус идеи

    def to_dict(self):
        dt_object = datetime.datetime.fromtimestamp(self.creation_time_unix)
        return {
            "id": self.id,
            "author_id": self.author_id,
            "creation_time": dt_object.strftime("%Y-%m-%d %H:%M:%S"),
            "name": self.name,
            "category": self.category,
            "region": self.region,
            "logo": self.logo,
            "contact_info": self.contact_info,
            "project_scale": self.project_scale,
            "project_start_time": self.project_start_time,
            "project_end_time": self.project_end_time,
            "video_preview": self.video_preview,
            "roles": json.loads(self.roles),
            "mentors": json.loads(self.mentors),
            "description": self.description,
            "issue_description": self.issue_description,
            "project_people_group_target": self.project_people_group_target,
            "project_target": self.project_target,
            "expireance_of_projects": self.expireance_of_projects,
            "perspective_of_project": self.perspective_of_project,
            "project_state": self.project_state
        }
    

Base.metadata.create_all(engine)