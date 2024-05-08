from app.extensions import db
from app.model import RecruitmentRequest, RecruitmentProgress,User
from app.extensions import ma
from flask_jwt_extended import jwt_required, get_jwt_identity,current_user
from flask import abort
from app.utils import check_employee


class RecruitmentRequestService:
    def __init__(self):
        pass

    def get_all_recruitmentRequests(args):

        pageIndex = args['PageIndex']
        pageSize = args['PageSize']
        print(pageSize)
        print(pageIndex)
        recruitmentRequests = RecruitmentRequest.query.paginate(page=pageIndex,per_page=pageSize,error_out=False).items
        print(recruitmentRequests)

        return recruitmentRequests

    def get_recruitmentRequest_by_id(id):
        recruitmentRequest = RecruitmentRequest.query.get(id)
        if recruitmentRequest is None:
            abort(404,f'Recruitment Request {id} not found')
        return recruitmentRequest

    def create_recruitmentRequest(payload):

        print(payload)
        check_employee(payload['RequesterId'])
        check_employee(payload['AssigneeId'])
        current_user = get_jwt_identity()
        requesterId = current_user['id']
        hrId = payload['AssigneeId']
        recruitmentRequest = RecruitmentRequest(position=payload["Position"],
                                        jobDescription=payload["JobDescription"],
                                        city=payload["City"],
                                        department=payload["Department"],
                                        recruitmentType=payload["RecruitmentType"],
                                        jobDuties=payload["JobDuties"],
                                        requiredQualifications=payload["RequiredQualifications"],
                                        salaryAndBenefit=payload["SalaryAndBenefit"],
                                        expectedStartDate=payload["ExpectedStartDate"],
                                        headCount=payload["HeadCount"],
                                        requesterId=requesterId,
                                        AssigneeId=hrId,
                                        status=payload["Status"])
        db.session.add(recruitmentRequest)
        db.session.commit()
        return recruitmentRequest


    def update_recruitmentRequest( id, recruitmentRequest):
        recruitmentRequest_to_update = RecruitmentRequest.query.get(id)
        if recruitmentRequest_to_update is None:
            abort(404,f'Recruitment Request {id} not found')
        check_employee(recruitmentRequest['RequesterId'])
        check_employee(recruitmentRequest['AssigneeId'])
        
        recruitmentRequest_to_update.Position = recruitmentRequest['Position']
        recruitmentRequest_to_update.JobDescription = recruitmentRequest['JobDescription']
        recruitmentRequest_to_update.City = recruitmentRequest['City']
        recruitmentRequest_to_update.Department = recruitmentRequest['Department']
        recruitmentRequest_to_update.RecruitmentType = recruitmentRequest['RecruitmentType']
        recruitmentRequest_to_update.JobDuties = recruitmentRequest['JobDuties']
        recruitmentRequest_to_update.RequiredQualifications = recruitmentRequest['RequiredQualifications']
        recruitmentRequest_to_update.SalaryAndBenefit = recruitmentRequest['SalaryAndBenefit']
        recruitmentRequest_to_update.ExpectedStartDate = recruitmentRequest['ExpectedStartDate']
        recruitmentRequest_to_update.HeadCount = recruitmentRequest['HeadCount']
        recruitmentRequest_to_update.Status = recruitmentRequest['Status']
        recruitmentRequest_to_update.RequesterId = recruitmentRequest['RequesterId']
        recruitmentRequest_to_update.AssigneeId = recruitmentRequest['AssigneeId']
        
        try:
            db.session.commit()
        except Exception as e:
            abort(400,f'An error occurred while updating the recruitment request {e}')
        return recruitmentRequest_to_update

    def delete_recruitmentRequest( id):
        recruitmentRequest = RecruitmentRequest.query.get(id)
        if recruitmentRequest is None:
            abort(404, f'Recruitment Request {id} not found')
        try:
            db.session.delete(recruitmentRequest)
            db.session.commit()
        except Exception as e:
            abort(400,f'An error occurred while deleting the recruitment request {e}')
        return recruitmentRequest