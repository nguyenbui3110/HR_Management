from flask import Flask, request, Blueprint
from .controllers.user import auth_ns
from .controllers.RecruitmentRequest import recruitment_request_ns

from .extensions import db, ma, api, jwt
from flask_restx import namespace
from flask_migrate import Migrate
from .model import *


def create_app(config_file="config.py"):
    app = Flask(__name__)    
    app.config.from_pyfile(config_file)
    print(app.config)
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)
    api.add_namespace(recruitment_request_ns)
    api.add_namespace(auth_ns)

    
    return app