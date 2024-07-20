# src/ config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost:5432/face_reco_db'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/face_reco_mongo'
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    UPLOAD_FOLDER = '/Users/grey/Desktop/Github/face-reco/src/upload'
