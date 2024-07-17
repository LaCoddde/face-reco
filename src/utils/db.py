#Database utility functions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def init_db():
    from src.models.user import Base as UserBase
    from src.models.api_key import Base as APIKeyBase
    UserBase.metadata.create_all(engine)
    APIKeyBase.metadata.create_all(engine)
