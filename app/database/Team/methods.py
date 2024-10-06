import json
from database.database import new_session
from database.Team.model import Team
from database.User.model import User

def create_team(data):
    with new_session() as session:
        team = Team(**data)
        session.add(team)
        session.commit()
        session.refresh(team)
        return team.to_dict()
    
def new_member(team_id, user_id):
    with new_session() as session:
        team = session.query(Team).filter_by(id=team_id).first()
        members = json.loads(team.members)
        members.append(user_id)
        team.members = json.dumps(members)
        session.commit()
        return team.to_dict()

def get_team_by_id(team_id):
    with new_session() as session:
        team = session.query(Team).filter_by(id=team_id).first()
        if team is None:
            return None
        return team.to_dict()
    
def new_project_in_team(team_id, project_id):
    with new_session() as session:
        team = session.query(Team).filter_by(id=team_id).first()
        team.projects.append(project_id)
        session.commit()
        return team.to_dict()
    
def all_teams():
    with new_session() as session:
        teams = session.query(Team).all()
        if teams is None:
            return None
        return [team.to_dict() for team in teams]
    
def update_team(team_id, data):
    with new_session() as session:
        team = session.query(Team).filter_by(id=team_id).first()
        for key, value in data.items():
            if key in ["members", "projects", "invites"]:
                setattr(team, key, json.dumps(value))
            else:
                setattr(team, key, value)
        session.commit()
        return team.to_dict()
    
def delete_team(team_id):
    with new_session() as session:
        team = session.query(Team).filter_by(id=team_id).first()
        session.delete(team)
        session.commit()
        return team.to_dict()