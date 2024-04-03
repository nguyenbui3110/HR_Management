from flask_restx import fields
from app.extensions import api

user_input_model = api.model('UserInput', {
    "Username": fields.String(required=True, description="The username"),
    "Password": fields.String(required=True, description="The password"),
    "Email": fields.String(required=True, description="The email"),
    "Role": fields.String(required=True, description="The role")
    })
user_model= api.model('User', {
    "Id": fields.Integer(required=True, description="The user ID"),
    "Username": fields.String(required=True, description="The username"),
    "Email": fields.String(required=True, description="The email"),
    "Role": fields.String(required=True, description="The role")
    })
login_model = api.model('Login', {
    "username": fields.String(required=True, description="The username"),
    "password": fields.String(required=True, description="The password")
    })