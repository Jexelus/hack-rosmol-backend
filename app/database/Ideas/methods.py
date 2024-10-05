from database.Ideas.model import Idea
from database.database import new_session
import time
import json


def get_idea_by_id(idea_id):
    with new_session() as session:
        return session.query(Idea).filter_by(id=idea_id).first
    
def get_ideas_by_author_id_with_pagination(author_id, page_size=10, page=1):
    with new_session() as session:
        data = session.query(Idea).filter_by(author_id=author_id).limit(page_size).offset((page - 1) * page_size).all()
        resp = []
        for idea in data:
            resp.append(idea.to_dict())
        return resp
    
def new_idea(
    author_id,
):
    with new_session() as session:
        session.add(Idea(
            author_id=author_id,
            creation_time_unix=time.time(),
        ))
        session.commit()

def delete_idea(idea_id):
    with new_session() as session:
        idea = session.query(Idea).filter_by(id=idea_id)
        idea.delete()
        session.commit()
        return idea.id 
    
def update_idea(idea_id, data):
    with new_session() as session:
        idea = session.query(Idea).filter_by(id=idea_id)
        for key, value in data.items():
            if key in ["roles", "mentors", "expireance_of_ideas"]:
                setattr(idea, key, json.dumps(value))
            else:
                setattr(idea, key, value)
        session.commit()
        return idea.to_dict()

def get_ideas_with_pagination(page_size=10, page=1):
    with new_session() as session:
        data = session.query(Idea).limit(page_size).offset((page - 1) * page_size).all()
        resp = []
        for idea in data:
            resp.append(idea.to_dict())
        return resp