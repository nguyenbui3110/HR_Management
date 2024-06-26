from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_jwt_extended import JWTManager
api = Api()
db = SQLAlchemy()
jwt=JWTManager()
ma = Marshmallow()
authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}