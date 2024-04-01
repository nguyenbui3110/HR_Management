from flask import Flask
from flask_restx import Api, Resource,Namespace
from ..services.user import UserService
from .api_model.User import user_input_model, user_model


# Create a namespace for authentication
auth_ns = Namespace('auth', description='Authentication operations')

# Create a resource for login
@auth_ns.route('/login')
class Login(Resource):
    def post(self):
        # Implement your login logic here
        return {'message': 'Login successful'}

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
    def post(self):
        # Implement your register logic here
        username = auth_ns.payload['username']
        password = auth_ns.payload['password']
        email = auth_ns.payload['email']
        role = auth_ns.payload['role']
        return UserService.create_account(username, password, email, role)
