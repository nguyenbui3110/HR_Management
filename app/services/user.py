from werkzeug.security import generate_password_hash
from app.extensions import db
from ..model.user import User

class UserService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        
        pass

    def logout(self):
        
        pass

    @staticmethod
    def create_account(username, password, email, role):
        # Hash the password before saving it
        hashed_password = generate_password_hash(password)
        user = User(username, email, hashed_password, role)
        db.session.add(user)
        db.session.commit()
        return user
        