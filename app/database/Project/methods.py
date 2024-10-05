from database.Project.model import Project
from database.database import new_session
import time
import json


def get_Project_by_id(Project_id):
    with new_session() as session:
        return session.query(Project).filter_by(id=Project_id).first
    
def get_Projects_by_author_id_with_pagination(author_id, page_size=10, page=1):
    with new_session() as session:
        data = session.query(Project).filter_by(author_id=author_id).limit(page_size).offset((page - 1) * page_size).all()
        resp = []
        for Project in data:
            resp.append(Project.to_dict())
        return resp
    
def new_Project(
    author_id,
):
    with new_session() as session:
        session.add(Project(
            author_id=author_id,
            creation_time_unix=time.time(),
        ))
        session.commit()

def delete_Project(Project_id):
    with new_session() as session:
        Project = session.query(Project).filter_by(id=Project_id)
        Project.delete()
        session.commit()
        return Project.id 
    
def update_Project(Project_id, data):
    with new_session() as session:
        Project = session.query(Project).filter_by(id=Project_id)
        for key, value in data.items():
            if key in ["roles", "mentors", "expireance_of_Projects"]:
                setattr(Project, key, json.dumps(value))
            else:
                setattr(Project, key, value)
        session.commit()
        return Project.to_dict()

def get_Projects_with_pagination(page_size=10, page=1):
    with new_session() as session:
        data = session.query(Project).limit(page_size).offset((page - 1) * page_size).all()
        resp = []
        for Project in data:
            resp.append(Project.to_dict())
        return resp