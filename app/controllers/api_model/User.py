from flask_restx import fields
from app.extensions import api

user_input_model = api.model('UserInput', {
    "username": fields.String(required=True, description="The username"),
    "password": fields.String(required=True, description="The password"),
    "email": fields.String(required=True, description="The email"),
    "role": fields.String(required=True, description="The role")
    })
user_model= api.model('User', {
    "id": fields.Integer(required=True, description="The user ID"),
    "username": fields.String(required=True, description="The username"),
    "email": fields.String(required=True, description="The email"),
    "role": fields.String(required=True, description="The role")
    })