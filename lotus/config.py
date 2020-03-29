import os
basedir = os.path.abspath(os.path.dirname(__file__))

CORS_ORIGINS = ['http://127.0.0.1:5000', 'http://82.148.17.124/', 'http://applotus.ru']
CORS_METHODS = ['GET', 'POST']
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'lotus.db')