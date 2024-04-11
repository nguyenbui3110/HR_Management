from flask import Flask,abort
from flask_restx import Api, Resource,Namespace
from ..services.RecruitmentRequest import RecruitmentRequestService
from .api_model.RecruitmentRequest import recruitment_request_model,recruitment_request_input_model
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user,get_jwt
from app.extensions import authorizations
recruitment_request_ns = Namespace('api/recruitment_request', description='Recruitment Request operations', authorizations=authorizations)

@recruitment_request_ns.route('/')
@recruitment_request_ns.response(200, 'Success')
@recruitment_request_ns.response(400, 'Bad request')
@recruitment_request_ns.response(401, 'Unauthorized')
@recruitment_request_ns.response(404, 'Not found')
@recruitment_request_ns.response(500, 'Internal Server Error')

class RecruitmentRequest(Resource):
    @recruitment_request_ns.doc(security='jsonWebToken')
    @recruitment_request_ns.marshal_list_with(recruitment_request_model)

    @recruitment_request_ns.doc(description='Get all recruitment requests')
    @jwt_required()
    def get(self):
        return RecruitmentRequestService.get_all_recruitmentRequests()
    @recruitment_request_ns.expect(recruitment_request_input_model)
    @recruitment_request_ns.marshal_with(recruitment_request_model)
    @recruitment_request_ns.doc(security='jsonWebToken')
    @jwt_required()
    def post(self):
        return RecruitmentRequestService.create_recruitmentRequest(recruitment_request_ns.payload)


@recruitment_request_ns.route('/<int:id>')
class RecruitmentRequest(Resource):
    @recruitment_request_ns.marshal_with(recruitment_request_model)
    @recruitment_request_ns.doc(description='Get a recruitment request by ID')
    @recruitment_request_ns.doc(security='jsonWebToken')
    @jwt_required()
    def get(self, id):
        return RecruitmentRequestService.get_recruitmentRequest_by_id(id)

    @recruitment_request_ns.marshal_with(recruitment_request_model)
    @recruitment_request_ns.expect(recruitment_request_input_model)
    @recruitment_request_ns.doc(description='Update a recruitment request by ID')
    @recruitment_request_ns.doc(security='jsonWebToken')
    @jwt_required()
    def put(self, id):
        return RecruitmentRequestService.update_recruitmentRequest(id, recruitment_request_ns.payload)
    @recruitment_request_ns.doc(description='Delete a recruitment request by ID')
    @recruitment_request_ns.doc(security='jsonWebToken')
    @recruitment_request_ns.marshal_with(recruitment_request_model)
    @jwt_required()
    def delete(self, id):
        return RecruitmentRequestService.delete_recruitmentRequest(id)