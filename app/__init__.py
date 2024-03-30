from flask import Flask, request, Blueprint
from .controllers.user import auth_ns

from .extensions import db, ma, api
from flask_restx import namespace



def create_app(config_file="config.py"):
    app = Flask(__name__)    
    app.config.from_pyfile(config_file)
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    api.add_namespace(auth_ns)

    
    return app