from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api

api = Api()
db = SQLAlchemy()

ma = Marshmallow()