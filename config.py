import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    