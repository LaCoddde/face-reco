#Service for developer account management
from models.user import User
from utils.db import get_session

def create_account(data):
    session = get_session()
    user = User(
        username=data['username'],
        email=data['email'],
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        company=data.get('company'),
        website=data.get('website')
    )
    user.set_password(data['password'])
    user.generate_api_key()
    session.add(user)
    session.commit()
    return {"status": "success", "message": "Account created"}

def generate_api_key(username):
    session = get_session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.generate_api_key()
        session.commit()
        return {"status": "success", "api_key": user.api_key}
    return {"status": "error", "message": "User not found"}

def revoke_api_key(username):
    session = get_session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.api_key = None
        session.commit()
        return {"status": "success", "message": "API key revoked"}
    return {"status": "error", "message": "User not found"}
