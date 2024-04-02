from sqlalchemy import Column, Integer, String
from app.extensions import db, ma
from werkzeug.security import  check_password_hash
# import jwt

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50),nullable=False, unique=True)
    email = Column(String(50),nullable=False, unique=True)
    password = Column(String(255))
    role = Column(String(50))

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        # Hash the password before saving it
        self.password = password
        self.role = role
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __str__(self):
        return f"User(name='{self.username}', email='{self.email}', role='{self.role}')"
    
    def __repr__(self):
        return f"<User(name='{self.username}', email='{self.email}', role='{self.role}')>"
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'role')
user_schema = UserSchema()
users_schema = UserSchema(many=True)
