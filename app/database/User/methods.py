from database.User.model import User
from database.database import new_session

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
    
