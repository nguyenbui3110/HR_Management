from flask import Flask
from flask_restx import Api, Resource,Namespace
from ..services.user import UserService
from .api_model.User import user_input_model, user_model, login_model

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}
# Create a namespace for authentication
auth_ns = Namespace('api/auth', description='Authentication operations', authorizations=authorizations)

# Create a resource for login
@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    @auth_ns.marshal_with(user_model)
    @auth_ns.response(200, 'Success')
    @auth_ns.response(401, 'Unauthorized')
    def post(self):
        username = auth_ns.payload['username']
        password = auth_ns.payload['password']
        return UserService.login(username, password)

# Create a resource for logout
@auth_ns.route('/logout')
class Logout(Resource):
    def post(self):
        # Implement your logout logic here
        return {'message': 'Logout successful'}
    
@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.expect(user_input_model)
    @auth_ns.marshal_with(user_model)
    @auth_ns.response(201, 'User created successfully')
    @auth_ns.response(400, 'Bad request')
    def post(self):
        # Implement your register logic here
        username = auth_ns.payload['username']
        password = auth_ns.payload['password']
        email = auth_ns.payload['email']
        role = auth_ns.payload['role']
        return UserService.create_account(username, password, email, role)
