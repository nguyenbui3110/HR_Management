from sqlalchemy import Column, Integer, String,Date,Text,Enum
from app.extensions import db, ma
from .Enums import *
class RecruitmentProgress(db.Model):
    __tablename__ = 'recruitmentProgress'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    RecruitmentRequestId = Column(Integer, db.ForeignKey('recruitmentRequest.Id', onupdate="CASCADE", ondelete="CASCADE"), nullable=True)
    RecruitmentRequest = db.relationship("RecruitmentRequest")
    Position = Column(String(50), nullable=True)
    NumberOfNewHire = Column(Integer, nullable=True)
    NewHires = Column(Text, nullable=True)
    RecruitmentStartDate = Column(Date, nullable=True)
    RecruitmentCompleteDate = Column(Date, nullable=True)
    CadidateInfos = db.relationship('CadidateInfo', back_populates='RecruitmentProgress', lazy=True)
    Status = Column(Enum(ProgressStatus))#enum
    def __init__(self,RecruitmentRequestId, Position, NumberOfNewHire, NewHires, RecruitmentStartDate, RecruitmentCompleteDate, Status):
        self.RecruitmentRequestId = RecruitmentRequestId
        self.Position = Position
        self.NumberOfNewHire = NumberOfNewHire
        self.NewHires = NewHires
        self.RecruitmentStartDate = RecruitmentStartDate
        self.RecruitmentCompleteDate = RecruitmentCompleteDate
        self.Status = Status
    def __str__(self):
        return f"RecruitmentProgress(Position='{self.Position}', NumberOfNewHire='{self.NumberOfNewHire}', NewHires='{self.NewHires}', RecruitmentStartDate='{self.RecruitmentStartDate}', RecruitmentCompleteDate='{self.RecruitmentCompleteDate}', Status='{self.Status}')"
    def __repr__(self):
        return f"<RecruitmentProgress(Position='{self.Position}', NumberOfNewHire='{self.NumberOfNewHire}', NewHires='{self.NewHires}', RecruitmentStartDate='{self.RecruitmentStartDate}', RecruitmentCompleteDate='{self.RecruitmentCompleteDate}', Status='{self.Status}')"
    