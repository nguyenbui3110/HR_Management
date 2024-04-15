from werkzeug.security import generate_password_hash
from app.extensions import db
from ..model import User
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user,create_refresh_token
import datetime
from flask import abort
class UserService:

    def login(username, password):
        user=User.query.filter_by(Username=username).first()
        print(user)
        print(user.check_password(password))
        if user and user.check_password(password):
            return {"access token":create_access_token(user.to_dict(),expires_delta=datetime.timedelta(days=1),fresh=True),
                    "refresh token":create_refresh_token(user.to_dict())}, 200
        return{'message':'Invalid username or password'}, 401

    def refresh_token():
        current_user = get_jwt_identity()
        return {"access token":create_access_token(current_user)}, 200
    def logout(self):
        

        pass

    @staticmethod
    def create_account(username, password, email, role):
        # Hash the password before saving it
        # hashed_password = generate_password_hash(password)
        user = User.query.filter_by(Username=username).first()
        if user:
            abort(400, 'Username already exists')
        user = User(username, email, password, role)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            abort(500, str(e))
        return user
        