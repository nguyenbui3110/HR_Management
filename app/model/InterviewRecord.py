from ..extensions import db, ma
from sqlalchemy import Column, Integer, String,Date,Text,Enum
from .Enums import *

class InterviewRecord(db.Model):
    __tablename__ = 'interviewRecord'
    Id = db.Column(Integer, primary_key=True)
    CandidateId = db.Column(Integer, db.ForeignKey('cadidateInfo.Id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True)
    Candidate = db.relationship('CadidateInfo', lazy=True, back_populates='InterviewRecords')
    InterviewDate = db.Column(Date)
    InterviewStage = db.Column(Enum(Stage))
    Result = db.Column(Enum(InterviewResult))
    InterviewerId = db.Column(Integer, db.ForeignKey('users.Id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True)
    Intervewer = db.relationship('User', lazy=True, back_populates='InterviewRecords')
    InterviewRecord = db.Column(Text)
    InterviewEvaluation = db.Column(Text)
    def __init__(self, CandidateId, InterviewDate, InterviewStage, Result, InterviewerId, InterviewRecord, InterviewEvaluation):
        self.CandidateId = CandidateId
        self.InterviewDate = InterviewDate
        self.InterviewStage = InterviewStage
        self.Result = Result
        self.InterviewerId = InterviewerId
        self.InterviewRecord = InterviewRecord
        self.InterviewEvaluation = InterviewEvaluation
    def __str__(self):
        return f"InterviewRecord(CandidateId='{self.CandidateId}', InterviewDate='{self.InterviewDate}', InterviewStage='{self.InterviewStage}', Result='{self.Result}', InterviewerId='{self.InterviewerId}', InterviewRecord='{self.InterviewRecord}', InterviewEvaluation='{self.InterviewEvaluation}')"
    def __repr__(self):
        return f"<InterviewRecord(CandidateId='{self.CandidateId}', InterviewDate='{self.InterviewDate}', InterviewStage='{self.InterviewStage}', Result='{self.Result}', InterviewerId='{self.InterviewerId}', InterviewRecord='{self.InterviewRecord}', InterviewEvaluation='{self.InterviewEvaluation}')"
