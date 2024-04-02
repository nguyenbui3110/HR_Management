from app.extensions import db
from app.model import RecruitmentRequest
from app.extensions import ma

class RecruitmentRequestService:
    def __init__(self):
        pass

    def get_all_recruitmentRequests(self):
        recruitmentRequests = RecruitmentRequest.query.all()
        return recruitmentRequests

    def get_recruitmentRequest_by_id(self, id):
        recruitmentRequest = RecruitmentRequest.query.get(id)
        return recruitmentRequest

    def add_recruitmentRequest(self, recruitmentRequest):
        db.session.add(recruitmentRequest)
        db.session.commit()
        return recruitmentRequest

    def update_recruitmentRequest(self, id, recruitmentRequest):
        recruitmentRequest_to_update = RecruitmentRequest.query.get(id)
        recruitmentRequest_to_update.position = recruitmentRequest.position
        recruitmentRequest_to_update.jobDescription = recruitmentRequest.jobDescription
        recruitmentRequest_to_update.city = recruitmentRequest.city
        recruitmentRequest_to_update.department = recruitmentRequest.department
        recruitmentRequest_to_update.recruitmentType = recruitmentRequest.recruitmentType
        recruitmentRequest_to_update.jobDuties = recruitmentRequest.jobDuties
        recruitmentRequest_to_update.requiredQualifications = recruitmentRequest.requiredQualifications
        recruitmentRequest_to_update.salaryAndBenefit = recruitmentRequest.salaryAndBenefit
        recruitmentRequest_to_update.expectedStartDate = recruitmentRequest.expectedStartDate
        recruitmentRequest_to_update.headCount = recruitmentRequest.headCount
        recruitmentRequest_to_update.requesterId = recruitmentRequest.requesterId
        recruitmentRequest_to_update.hrId = recruitmentRequest.hrId
        recruitmentRequest_to_update.status = recruitmentRequest.status
        recruitmentRequest_to_update.recruitmentProgressId = recruitmentRequest.recruitmentProgressId
        db.session.commit()
        return recruitmentRequest_to_update

    def delete_recruitmentRequest(self, id):
        recruitmentRequest = RecruitmentRequest.query.get(id)
        db.session.delete(recruitmentRequest)
        db.session.commit()
        return recruitmentRequest