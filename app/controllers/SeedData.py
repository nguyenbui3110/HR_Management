from flask import abort
from flask_restx import Api, Resource,Namespace
from ..services.SeedData import SeedDataService

SeedData_ns = Namespace('api/seed_data', description='Seed Data operations')

@SeedData_ns.route('/')
@SeedData_ns.response(200, 'Success')
@SeedData_ns.response(400, 'Bad request')
@SeedData_ns.response(401, 'Unauthorized')
@SeedData_ns.response(404, 'Not found')
@SeedData_ns.response(500, 'Internal Server Error')
class SeedData(Resource):
    @SeedData_ns.doc(description='Seed data')
    def get(self):
        return SeedDataService.seed_data()
    