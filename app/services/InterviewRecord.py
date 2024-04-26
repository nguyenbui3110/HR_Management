from app.extensions import db
from app.model import *
from app.extensions import ma
from flask_jwt_extended import jwt_required, get_jwt_identity,current_user
from flask import abort
from app.utils import check_employee

def modify_record(records):
    if len(records) == 0:
        return None
    modified_records = []
    for record in records:
        modified_record = {
            "Id": record.Id,
            "CandidateId": record.CandidateId,
            "InterviewDate": record.InterviewDate,
            "InterviewStage": record.InterviewStage.name,  
            "Result": record.Result.name,
            "InterviewerId": record.InterviewerId,
            "InterviewRecord": record.InterviewRecord,
            "InterviewEvaluation": record.InterviewEvaluation
        }
        modified_records.append(modified_record)
    return modified_records

def modify_1_record(record):
    modified_record = {
        "Id": record.Id,
        "CandidateId": record.CandidateId,
        "InterviewDate": record.InterviewDate,
        "InterviewStage": record.InterviewStage.name,  
        "Result": record.Result.name,
        "InterviewerId": record.InterviewerId,
        "InterviewRecord": record.InterviewRecord,
        "InterviewEvaluation": record.InterviewEvaluation
    }
    return modified_record
class InterviewRecordService:
    def __init__(self):
        pass
    def get_all_interviewRecords():
        interviewRecords = InterviewRecord.query.all()
        return modify_record(interviewRecords)
    
    def get_interviewRecord_by_id(id):
        interviewRecord = InterviewRecord.query.get(id)
        if interviewRecord is None:
            abort(404,f'Interview Record {id} not found')
        return modify_1_record(interviewRecord)
    
    def create_interviewRecord(payload):
        check_employee(payload['InterviewerId'])
        interviewRecord = InterviewRecord(CandidateId=payload["CandidateId"],
                                        InterviewDate=payload["InterviewDate"],
                                        InterviewStage=payload["InterviewStage"],
                                        Result=payload["Result"],
                                        InterviewRecord=payload["InterviewRecord"],
                                        InterviewEvaluation=payload["InterviewEvaluation"],
                                        InterviewerId=payload["InterviewerId"])
        db.session.add(interviewRecord)
        db.session.commit()
        return modify_1_record(interviewRecord)
    
    def update_interviewRecord( id, interviewRecord):
        print(interviewRecord)
        interviewRecord_to_update = InterviewRecord.query.get(id)
        check_employee(interviewRecord['InterviewerId'])
        if interviewRecord_to_update is None:
            abort(404,f'Interview Record {id} not found')
        interviewRecord_to_update.CandidateId = interviewRecord['CandidateId']
        interviewRecord_to_update.InterviewDate = interviewRecord['InterviewDate']
        interviewRecord_to_update.InterviewStage = interviewRecord['InterviewStage']
        interviewRecord_to_update.Result = interviewRecord['Result']
        interviewRecord_to_update.InterviewRecord = interviewRecord['InterviewRecord']
        interviewRecord_to_update.InterviewEvaluation = interviewRecord['InterviewEvaluation']
        interviewRecord_to_update.InterviewerId = interviewRecord['InterviewerId']
        db.session.commit()
        print(interviewRecord_to_update)

        return modify_1_record(interviewRecord_to_update)
    def delete_interviewRecord(id):
        interviewRecord = InterviewRecord.query.get(id)
        if interviewRecord is None:
            abort(404,f'Interview Record {id} not found')
        db.session.delete(interviewRecord)
        db.session.commit()
        return modify_1_record(interviewRecord)
    