from sqlalchemy import Column, Integer, String
from app.extensions import db, ma
from werkzeug.security import  check_password_hash
# import jwt

class User(db.Model):
    __tablename__ = 'users'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String(50), nullable=False, unique=True)
    Email = Column(String(50), nullable=False, unique=True)
    Password = Column(String(255))
    Role = Column(String(50))
    # Define requests relationship with custom foreign key
    Requests = db.relationship('RecruitmentRequest', foreign_keys="[RecruitmentRequest.RequesterId]", back_populates='Requester', lazy=True)
    
    # Define assigns relationship with custom foreign key
    Assigns = db.relationship('RecruitmentRequest', foreign_keys="[RecruitmentRequest.AssigneeId]", back_populates='Assignee', lazy=True)
    # Define CadidateInfos relationship 
    CadidateInfos = db.relationship('CadidateInfo', back_populates='Assignee', lazy=True)
    # Define InterviewRecords relationship
    InterviewRecords = db.relationship('InterviewRecord', back_populates='Intervewer', lazy=True)

    def __init__(self, username, email, password, role):
        self.Username = username
        self.Email = email
        self.Password = password
        self.Role = role   
    def check_password(self, password):
        return check_password_hash(self.Password, password)
    
    def __str__(self):
        return f"User(username='{self.Username}', email='{self.Email}', role='{self.Role}')"
    def __repr__(self):
        return f"<User(username='{self.Username}', email='{self.Email}', role='{self.Role}')"
    def to_dict(self):
        return {
            'username': self.Username,
            'email': self.Email,
            'role': self.Role
        }
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'role')
user_schema = UserSchema()
users_schema = UserSchema(many=True)
