from flask_restx import fields
from app.extensions import api
from app.model.Enums import *

interview_record_input_model = api.model('InterviewRecordInput', {
    "CandidateId": fields.Integer(required=True, description="The interviewer ID"),
    "InterviewDate": fields.Date(required=True, description="The interviewee ID"),
    "InterviewStage": fields.String(enum=[e.name for e in Stage],required=True, description="The position"),
    "Result": fields.String(enum=[e.name for e in InterviewResult],required=True, description="The date of the interview"),
    "InterviewerId": fields.Integer(required=True, description="The interview type"),
    "InterviewRecord": fields.String(required=True, description="The feedback of the interview"),
    "InterviewEvaluation": fields.String(required=True, description="The status of the interview"),
    })
interview_record_model = api.model('InterviewRecord', {
    'Id': fields.Integer(required=True, description='ID of the interview record'),
    'CandidateId': fields.Integer(description='ID of the candidate'),
    'InterviewDate': fields.Date(description='Date of the interview'),
    "InterviewStage": fields.String( enum=[e.name for e in Stage],description="The position"),
    "Result": fields.String(enum=[e.name for e in InterviewResult], description="The date of the interview"),
    'InterviewerId': fields.Integer(description='ID of the interviewer'),
    'InterviewRecord': fields.String(description='Feedback of the interview'),
    'InterviewEvaluation': fields.String(description='Evaluation of the interview'),
})