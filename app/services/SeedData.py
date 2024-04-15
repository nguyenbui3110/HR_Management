from app.model import *
from app.extensions import db

class SeedDataService:
    def __init__(self):
        pass
    #seed data if the table is empty
    def seed_data():
        if db.session.query(User).count() == 0:
            #seed user
            db.session.add(User('admin','admin','admin','admin'))
            db.session.add(User('laura','laura@gmail.com','Hr123','HR'))
            db.session.add(User('john','john@gmail.com','Hr123','HR'))
            db.session.add(User('jane','jane@gmail.com','Hr123','HR'))
            db.session.add(User('hau','Hau@gmail.com','Hr123','HR'))
            db.session.commit()
        if db.session.query(RecruitmentRequest).count() == 0:
            #seed recruitment request
            db.session.add(RecruitmentRequest('Software Engineer','Develop software','Hanoi','IT','Intern','Develop software','Bachelor degree in Computer Science','Salary 1000$','2021-09-01',5,2,2,'Recruiting'))
            db.session.add(RecruitmentRequest('Accountant','Accountant','Hanoi','Accounting','Full-time','Accountant','Bachelor degree in Accounting','Salary 1000$','2021-09-01',5,2,2,'Recruiting'))
            db.session.add(RecruitmentRequest('HR','HR','Hanoi','HR','Full-time','HR','Bachelor degree in HR','Salary 1000$','2021-09-01',5,2,2,'Not Recruiting'))
            db.session.commit()

