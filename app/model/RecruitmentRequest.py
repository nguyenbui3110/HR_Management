from sqlalchemy import Column, Integer, String,Date,Text
from app.extensions import db, ma

class RecruitmentRequest(db.Model):
    __tablename__ = 'recruitmentRequest'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Position = Column(String(255), nullable=True)
    JobDescription = Column(Text, nullable=True)
    City = Column(String(255), nullable=True)
    Department = Column(String(255), nullable=True)
    RecruitmentType = Column(String(50), nullable=True)
    JobDuties = Column(Text, nullable=True)
    RequiredQualifications = Column(Text, nullable=True)
    SalaryAndBenefit = Column(Text, nullable=True)
    ExpectedStartDate = Column(Date, nullable=True)
    HeadCount = Column(Integer, nullable=True)
    RequesterId = Column(Integer, db.ForeignKey('users.Id'))
    Requester = db.relationship('User', foreign_keys=[RequesterId], back_populates='Requests', lazy=True)
    AssigneeId = Column(Integer, db.ForeignKey('users.Id'))
    Assignee  = db.relationship('User', foreign_keys=[AssigneeId],back_populates='Assigns', lazy=True)
    Status = Column(String(50), nullable=True)#enum
    RecruitmentProgress = db.relationship("RecruitmentProgress", overlaps="RecruitmentProgress")

    def __init__(self, position, jobDescription, city, department, recruitmentType, jobDuties, requiredQualifications, salaryAndBenefit, expectedStartDate, headCount, requesterId, AssigneeId, status):
        self.Position = position
        self.JobDescription = jobDescription
        self.City = city
        self.Department = department
        self.RecruitmentType = recruitmentType
        self.JobDuties = jobDuties
        self.RequiredQualifications = requiredQualifications
        self.SalaryAndBenefit = salaryAndBenefit
        self.ExpectedStartDate = expectedStartDate
        self.HeadCount = headCount
        self.RequesterId = requesterId
        self.AssigneeId = AssigneeId
        self.Status = status

    def __str__(self):
        return f"RecruitmentRequest(Position='{self.Position}', JobDescription='{self.JobDescription}', City='{self.City}', Department='{self.Department}', RecruitmentType='{self.RecruitmentType}', JobDuties='{self.JobDuties}', RequiredQualifications='{self.RequiredQualifications}', SalaryAndBenefit='{self.SalaryAndBenefit}', ExpectedStartDate='{self.ExpectedStartDate}', HeadCount='{self.HeadCount}', RequesterId='{self.RequesterId}', AssigneeId='{self.AssigneeId}', Status='{self.Status}')"
    def __repr__(self):
        return f"<RecruitmentRequest(Position='{self.Position}', JobDescription='{self.JobDescription}', City='{self.City}', Department='{self.Department}', RecruitmentType='{self.RecruitmentType}', JobDuties='{self.JobDuties}', RequiredQualifications='{self.RequiredQualifications}', SalaryAndBenefit='{self.SalaryAndBenefit}', ExpectedStartDate='{self.ExpectedStartDate}', HeadCount='{self.HeadCount}', RequesterId='{self.RequesterId}', AssigneeId='{self.AssigneeId}', Status='{self.Status}')"

class RecruitmentRequestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'position', 'jobDescription', 'city', 'department', 'recruitmentType', 'jobDuties', 'requiredQualifications', 'salaryAndBenefit', 'expectedStartDate', 'headCount', 'requesterId', 'AssigneeId', 'status')
recruitmentRequest_schema = RecruitmentRequestSchema()
recruitmentRequests_schema = RecruitmentRequestSchema(many=True)

