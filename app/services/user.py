from werkzeug.security import generate_password_hash
from app.extensions import db
from ..model import User

class UserService:

    def login(username, password):
        user=User.query.filter_by(Username=username).first()
        print(user)
        print(user.check_password(password))
        if user and user.check_password(password):
            return user
        return{'message':'Invalid username or password'}, 401

    def logout(self):
        
        pass

    @staticmethod
    def create_account(username, password, email, role):
        # Hash the password before saving it
        hashed_password = generate_password_hash(password)
        user = User(username, email, hashed_password, role)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return {'message': 'An error occurred while creating the user'}, 400
        return user
        