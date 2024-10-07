from sqlalchemy import distinct
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

        if len(resp) == 0:
            return None

        return resp
    
def new_Project(data):
    with new_session() as session:
        roles = json.dumps(data["roles"])
        mentors = json.dumps(data["mentors"])
        expireance_of_projects = json.dumps(data["expireance_of_projects"])
        del data["roles"]
        del data["mentors"]
        del data["expireance_of_projects"]
        proj = Project(
            **data,
            creation_time_unix=time.time(),
            roles=roles,
            mentors=mentors,
            expireance_of_projects=expireance_of_projects
        )
        session.add(proj)
        session.commit()
    return proj.to_dict()

def delete_Project(Project_id):
    with new_session() as session:
        project = session.query(Project).filter_by(id=Project_id)
        project.delete()
        session.commit()
        return project.to_dict()
    
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
        for proj in data:
            resp.append(proj.to_dict())

        if len(resp) == 0:
            return None

        return resp
    
def get_Projects_by_category_with_pagination(category, page_size=10, page=1):
    with new_session() as session:
        data = session.query(Project).filter_by(category=category).limit(page_size).offset((page - 1) * page_size).all()
        resp = []
        for proj in data:
            resp.append(proj.to_dict())

        if len(resp) == 0:
            return None

        return resp
    
def get_all_projects():
    with new_session() as session:
        data = session.query(Project).all()
        resp = []
        for proj in data:
            resp.append(proj.to_dict())

        if len(resp) == 0:
            return None

        return resp
    
def get_projects_by_category(category):
    with new_session() as session:
        data = session.query(Project).filter_by(category=category).all()
        resp = []
        for proj in data:
            resp.append(proj.to_dict())

        if len(resp) == 0:
            return None
        
        return resp
    
def get_projects_by_category_with_pagination(category, page_size=10, page=1):
    with new_session() as session:
        data = session.query(Project).filter_by(category=category).limit(page_size).offset((page - 1) * page_size).all()
        resp = []
        for proj in data:
            resp.append(proj.to_dict())
        if len(resp) == 0:
            return None
        return resp
    
def get_projects_by_author_id(author_id):
    with new_session() as session:
        data = session.query(Project).filter_by(author_id=author_id).all()
        resp = []
        for proj in data:
            resp.append(proj.to_dict())
        if len(resp) == 0:
            return None
        return resp
    
def get_categories():
    with new_session() as session:
        categories = session.query(Project.category).distinct().all()
        return [category[0] for category in categories]