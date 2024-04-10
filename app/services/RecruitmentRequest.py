from app.extensions import db
from app.model import RecruitmentRequest, RecruitmentProgress
from app.extensions import ma
from flask_jwt_extended import jwt_required, get_jwt_identity,current_user


class RecruitmentRequestService:
    def __init__(self):
        pass

    def get_all_recruitmentRequests():
        recruitmentRequests = RecruitmentRequest.query.all()
        return recruitmentRequests

    def get_recruitmentRequest_by_id( id):
        recruitmentRequest = RecruitmentRequest.query.get(id)
        return recruitmentRequest

    def create_recruitmentRequest(payload):
        print(payload)
        position = payload['position']
        jobDescription = payload['jobDescription']
        city = payload['city']
        department = payload['department']
        recruitmentType = payload['recruitmentType']
        jobDuties = payload['jobDuties']
        requiredQualifications = payload['requiredQualifications']
        salaryAndBenefit = payload['salaryAndBenefit']
        expectedStartDate = payload['expectedStartDate']
        headCount = payload['headCount']
        
        current_user = get_jwt_identity()
        requesterId = current_user['id']
        hrId = requesterId
        status = payload['status']
        recruitmentRequest = RecruitmentRequest(position, jobDescription, city, department, recruitmentType, jobDuties, requiredQualifications, salaryAndBenefit, expectedStartDate, headCount, requesterId, hrId, status)
        print(recruitmentRequest)
        db.session.add(recruitmentRequest)
        db.session.commit()
        return recruitmentRequest

    def add_recruitmentRequest(recruitmentRequest):
        db.session.add(recruitmentRequest)
        db.session.commit()
        return recruitmentRequest

    def update_recruitmentRequest( id, recruitmentRequest):
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