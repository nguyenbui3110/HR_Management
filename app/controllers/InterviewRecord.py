from flask import Flask,abort
from flask_restx import Api, Resource,Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user,get_jwt
from app.extensions import authorizations

from app.services.InterviewRecord import InterviewRecordService
from .api_model.InterviewRecord import interview_record_model,interview_record_input_model

interview_record_ns = Namespace('api/interview_record', description='Interview Record operations', authorizations=authorizations)

@interview_record_ns.route('/')
@interview_record_ns.response(200, 'Success')
@interview_record_ns.response(400, 'Bad request')
@interview_record_ns.response(401, 'Unauthorized')
@interview_record_ns.response(404, 'Not found')
@interview_record_ns.response(500, 'Internal Server Error')

class InterviewRecord(Resource):
    @interview_record_ns.doc(security='jsonWebToken')
    @interview_record_ns.marshal_list_with(interview_record_model)

    @interview_record_ns.doc(description='Get all interview records')
    @jwt_required()
    def get(self):
        return InterviewRecordService.get_all_interviewRecords()
    @interview_record_ns.expect(interview_record_input_model)
    @interview_record_ns.marshal_with(interview_record_model)
    @interview_record_ns.doc(security='jsonWebToken')
    @jwt_required()
    def post(self):
        return InterviewRecordService.create_interviewRecord(interview_record_ns.payload)
    
@interview_record_ns.route('/<int:id>')
class InterviewRecord(Resource):
    @interview_record_ns.marshal_with(interview_record_model)
    @interview_record_ns.doc(description='Get an interview record by ID')
    @interview_record_ns.doc(security='jsonWebToken')
    @jwt_required()
    def get(self, id):
        return InterviewRecordService.get_interviewRecord_by_id(id)

    @interview_record_ns.marshal_with(interview_record_model)
    @interview_record_ns.expect(interview_record_input_model)
    @interview_record_ns.doc(description='Update an interview record by ID')
    @interview_record_ns.doc(security='jsonWebToken')
    @jwt_required()
    def put(self, id):
        return InterviewRecordService.update_interviewRecord(id, interview_record_ns.payload)
    @interview_record_ns.doc(description='Delete an interview record by ID')
    @interview_record_ns.doc(security='jsonWebToken')
    @interview_record_ns.marshal_with(interview_record_model)
    @jwt_required()
    def delete(self, id):
        return InterviewRecordService.delete_interviewRecord(id)
