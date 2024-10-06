import json
from database.User.model import User
from database.database import new_session
from database.Team.model import Team
from database.Team.methods import new_member

def create_user(vk_id, email, fio, competencies, role="user"):
    with new_session() as session:
        user = User(vk_id=vk_id,
                    email=email,
                    fio=fio,
                    competencies=competencies,
                    role=role)
        session.add(user)
        session.commit()
        return user

def update_last_project_id(user_id, project_id):
    with new_session() as session:
        user = session.query(User).filter_by(vk_id=user_id).first()
        user.last_project_id = project_id
        session.commit()

def get_user_by_vk_id(vk_id):
    with new_session() as session:
        user = session.query(User).filter_by(vk_id=vk_id).first()
        if user is None:
            return None
        return session.query(User).filter_by(vk_id=vk_id).first().to_dict()
    
def accept_invite(user_id, project_id, team_id):
    with new_session() as session:
        user = session.query(User).filter_by(vk_id=user_id).first()
        invites = json.loads(user.invites)
        if project_id in invites:
            invites.remove(project_id)
            user.invites = json.dumps(invites)
        session.commit()
    
    with new_session() as session:
        team = session.query(Team).filter_by(id=team_id).first()
        members = json.loads(team.members)
        members.append(user_id)
        team.members = json.dumps(members)
        session.commit()
    return team.to_dict()

def new_invite(user_id, project_id):
    with new_session() as session:
        user = session.query(User).filter_by(vk_id=user_id).first()
        invites = json.loads(user.invites)
        invites.append(project_id)
        user.invites = json.dumps(invites)
        session.commit()

def leave_team(user_id, team_id):
    with new_session() as session:
        user = session.query(User).filter_by(vk_id=user_id).first()
        user.team_id = None
        session.commit()
    with new_session() as session:
        team = session.query(Team).filter_by(id=team_id).first()
        members = json.loads(team.members)
        members.remove(user_id)
        team.members = json.dumps(members)
        session.commit()
    return user.to_dict()