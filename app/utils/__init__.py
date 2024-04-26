from app.extensions import db, ma
from app.model import *
from flask import abort
from flask_restx import fields

def check_employee(Id):
    employee = User.query.get(Id)
    if employee is None:
        abort(404,f'Employee has {Id} not found')
