from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,Date,Text,Enum
from app.extensions import db, ma
from .Enums import *

class CadidateInfo(db.Model):
    __tablename__ = 'cadidateInfo'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    RecruitmentProgressId = db.Column(Integer, db.ForeignKey('recruitmentProgress.Id'), nullable=True)
    RecruitmentProgress = db.relationship('RecruitmentProgress',back_populates='CadidateInfos', lazy=True)

    ResumeEvaluation = db.Column(Enum(ResumeEvaluation))#enum
    InterviewProgress = db.Column(Enum(InterviewProgress))#enum
    OfferStatus = db.Column(Enum(OfferStatus))#enum
    HiringStatus = db.Column(Enum(HiringStatus))#enum
    SubmissionChannel = db.Column(Enum(SubmissionChannel))#enum
    Resume = db.Column(db.String(255))
    AssigneeId = db.Column(Integer, db.ForeignKey('users.Id'), nullable=True)
    Assignee = db.relationship('User', lazy=True, back_populates='CadidateInfos')
    InterviewRecords = db.relationship('InterviewRecord', back_populates='Candidate', lazy=True)
