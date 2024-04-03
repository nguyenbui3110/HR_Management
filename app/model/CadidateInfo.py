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

    ResumeEvaluation = db.Column(Enum(ResumeEvaluationEnum))#enum
    InterviewProgress = db.Column(Enum(InterviewProgressEnum))#enum
    OfferStatus = db.Column(Enum(OfferStatusEnum))#enum
    HiringStatus = db.Column(Enum(HiringStatusEnum))#enum
    SubmissionChannel = db.Column(Enum(SubmissionChannelEnum))#enum
    Resume = db.Column(db.String(255))
    AssigneeId = db.Column(Integer, db.ForeignKey('users.Id'), nullable=True)
    Assignee = db.relationship('User', lazy=True, back_populates='CadidateInfos')
