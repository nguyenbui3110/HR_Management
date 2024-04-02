from flask import Flask
from flask_restx import Api, Resource,Namespace
from ..services.RecruitmentRequest import RecruitmentRequestService

recruitment_request_ns = Namespace('api/recruitment_request', description='Recruitment Request operations')

@recruitment_request_ns.route('/')
class RecruitmentRequest(Resource):
    def get(self):
        return {'message': 'Get all recruitment requests'}


@recruitment_request_ns.route('/<int:id>')
class RecruitmentRequest(Resource):
    def get(self, id):
        return {'message': 'Get a recruitment request by ID'}

    def put(self, id):
        return {'message': 'Update a recruitment request by ID'}

    def delete(self, id):
        return {'message': 'Delete a recruitment request by ID'}