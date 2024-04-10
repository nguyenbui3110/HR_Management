from flask_restx import fields
from app.extensions import api
from app.model.Enums import *
recruitment_request_input_model = api.model('RecruitmentRequestInput', {
    "Position": fields.String(required=True, description="The position"),
    "JobDescription": fields.String(required=True, description="The job description"),
    "City": fields.String(required=True, description="The city"),
    "Department": fields.String(required=True, description="The department"),
    "RecruitmentType": fields.String(enum=[e.value for e in RecruitmentType],required=True, description="The recruitment type"),
    "JobDuties": fields.String(required=True, description="The job duties"),
    "RequiredQualifications": fields.String(required=True, description="The required qualifications"),
    "SalaryAndBenefit": fields.String(required=True, description="The salary and benefit"),
    "ExpectedStartDate": fields.Date(required=True, description="The expected start date"),
    "HeadCount": fields.Integer(required=True, description="The head count"),
    "Status": fields.String(enum=[e.value for e in RequestStatus],required=True, description="The status"),
    })
recruitment_request_model = api.model('RecruitmentRequest', {
    'Id': fields.Integer(required=True, description='ID of the recruitment request'),
    'Position': fields.String(description='Position for the job'),
    'JobDescription': fields.String(description='Description of the job'),
    'City': fields.String(description='City for the job'),
    'Department': fields.String(description='Department for the job'),
    'RecruitmentType': fields.String(description='Type of recruitment'),
    'JobDuties': fields.String(description='Duties for the job'),
    'RequiredQualifications': fields.String(description='Required qualifications for the job'),
    'SalaryAndBenefit': fields.String(description='Salary and benefits for the job'),
    'ExpectedStartDate': fields.Date(description='Expected start date for the job'),
    'HeadCount': fields.Integer(description='Headcount for the job'),
    'RequesterId': fields.Integer(description='ID of the requester'),
    'AssigneeId': fields.Integer(description='ID of the assignee'),
    'Status': fields.String(description='Status of the request'),
})

# Optionally, you can include nested models for relationships
user_model = api.model('User', {
    'Id': fields.Integer(description='User ID'),
    'Username': fields.String(description='Username'),
    # Include other fields as needed
})

recruitment_progress_model = api.model('RecruitmentProgress', {
    'Id': fields.Integer(description='Recruitment progress ID'),
    'Position': fields.String(description='Position for the job'),
    # Include other fields as needed
})

# Nest the nested models into the main model
recruitment_request_model['Requester'] = fields.Nested(user_model)
recruitment_request_model['Assignee'] = fields.Nested(user_model)
recruitment_request_model['RecruitmentProgress'] = fields.List(fields.Nested(recruitment_progress_model))