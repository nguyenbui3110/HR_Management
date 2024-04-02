from sqlalchemy import Column, Integer, String,Date,Text
from app.extensions import db, ma
class RecruitmentRequest(db.Model):
    __tablename__ = 'recruitmentRequest'
    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String(255), nullable=False)
    jobDescription = Column(Text, nullable=True)
    city = Column(String(255), nullable=False)
    department = Column(String(255), nullable=False)
    recruitmentType = Column(String(50), nullable=False)
    jobDuties = Column(Text, nullable=False)
    requiredQualifications = Column(Text, nullable=True)
    salaryAndBenefit = Column(Text, nullable=False)
    expectedStartDate = Column(Date, nullable=False)
    headCount = Column(Integer, nullable=False)
    requesterId = Column(Integer, db.ForeignKey('users.id'), nullable=False)
    hrId = Column(Integer, db.ForeignKey('users.id'), nullable=False)
    status = Column(String(50), nullable=False)#enum
    recruitmentProgressId = Column(String(50), nullable=False)

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

