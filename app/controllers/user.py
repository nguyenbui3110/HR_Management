from flask import Flask
from flask_restx import Api, Resource,Namespace
from ..services.user import UserService
from .api_model.User import user_input_model, user_model, login_model
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user,get_jwt
from datetime import datetime
from app.extensions import authorizations

# Create a namespace for authentication
auth_ns = Namespace('api/auth', description='Authentication operations', authorizations=authorizations)

# Create a resource for login
@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
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
        username = auth_ns.payload['Username']
        password = auth_ns.payload['Password']
        email = auth_ns.payload['Email']
        role = auth_ns.payload['Role']
        return UserService.create_account(username, password, email, role)
@auth_ns.route('/test-current-user')
@auth_ns.response(200, 'Success')
@auth_ns.response(401, 'Unauthorized')
@auth_ns.doc(security='jsonWebToken')
class TestCurrentUser(Resource):
    @jwt_required()
    def get(self):
        jwt=get_jwt()
        print(jwt)
        current_user = get_jwt_identity()
        #print expiring time
        print(current_user)

        return {'current_user': current_user}, 200