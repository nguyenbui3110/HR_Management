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
    RecruitmentProgressId = Column(String(50), nullable=True)

    def __init__(self, position, jobDescription, city, department, recruitmentType, jobDuties, requiredQualifications, salaryAndBenefit, expectedStartDate, headCount, requesterId, hrId, status, recruitmentProgressId):
        self.position = position
        self.jobDescription = jobDescription
        self.city = city
        self.department = department
        self.recruitmentType = recruitmentType
        self.jobDuties = jobDuties
        self.requiredQualifications = requiredQualifications
        self.salaryAndBenefit = salaryAndBenefit
        self.expectedStartDate = expectedStartDate
        self.headCount = headCount
        self.requesterId = requesterId
        self.hrId = hrId
        self.status = status
        self.recruitmentProgressId = recruitmentProgressId
    def __str__(self):
        return f"RecruitmentRequest(position='{self.position}', jobDescription='{self.jobDescription}', city='{self.city}', department='{self.department}', recruitmentType='{self.recruitmentType}', jobDuties='{self.jobDuties}', requiredQualifications='{self.requiredQualifications}', salaryAndBenefit='{self.salaryAndBenefit}', expectedStartDate='{self.expectedStartDate}', headCount='{self.headCount}', requesterId='{self.requesterId}', hrId='{self.hrId}', status='{self.status}', recruitmentProgressId='{self.recruitmentProgressId}')"
    def __repr__(self):
        return f"<RecruitmentRequest(position='{self.position}', jobDescription='{self.jobDescription}', city='{self.city}', department='{self.department}', recruitmentType='{self.recruitmentType}', jobDuties='{self.jobDuties}', requiredQualifications='{self.requiredQualifications}', salaryAndBenefit='{self.salaryAndBenefit}', expectedStartDate='{self.expectedStartDate}', headCount='{self.headCount}', requesterId='{self.requesterId}', hrId='{self.hrId}', status='{self.status}', recruitmentProgressId='{self.recruitmentProgressId}')"
    

class RecruitmentRequestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'position', 'jobDescription', 'city', 'department', 'recruitmentType', 'jobDuties', 'requiredQualifications', 'salaryAndBenefit', 'expectedStartDate', 'headCount', 'requesterId', 'hrId', 'status', 'recruitmentProgressId')
recruitmentRequest_schema = RecruitmentRequestSchema()
recruitmentRequests_schema = RecruitmentRequestSchema(many=True)

