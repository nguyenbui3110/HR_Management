from sqlalchemy import Column, Integer, String
from app.extensions import db, ma
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    role = Column(String(50))

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        # Hash the password before saving it
        hashed_password = generate_password_hash(password)
        self.password = hashed_password
        self.role = role
    
    def __str__(self):
        return f"User(name='{self.name}', email='{self.email}', role='{self.role}')"
    
    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}', role='{self.role}')>"
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'role')
user_schema = UserSchema()
users_schema = UserSchema(many=True)
