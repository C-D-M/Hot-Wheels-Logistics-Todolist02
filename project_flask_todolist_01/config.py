import os

# base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# database
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'todolist.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False