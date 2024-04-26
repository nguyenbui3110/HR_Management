from app.model import *
from app.extensions import db
from faker import Faker
from app.model.Enums import *
from faker.providers.python import Provider
class SeedDataService:
    def __init__(self):
        pass
    #seed data if the table is empty
    def seed_data():
        fake = Faker()
        fake.add_provider(Provider)
        if db.session.query(User).count() == 0:
            #seed user
            db.session.add(User('admin','admin','admin','admin'))
            db.session.add(User('laura','laura@gmail.com','Hr123','HR'))
            db.session.add(User('john','john@gmail.com','Hr123','HR'))
            db.session.add(User('jane','jane@gmail.com','Hr123','HR'))
            db.session.add(User('hau','Hau@gmail.com','Hr123','HR'))
            db.session.commit()
        if db.session.query(RecruitmentRequest).count() == 0:
            #get first 5 user
            users = db.session.query(User).limit(5).all()

            #seed recruitment request
            db.session.add(RecruitmentRequest('Software Engineer','Develop software','Hanoi','IT','Intern','Develop software','Bachelor degree in Computer Science','Salary 1000$','2021-09-01',5,users[0].Id,users[0].Id,'Recruiting'))
            db.session.add(RecruitmentRequest('Accountant','Accountant','Hanoi','Accounting','Full-time','Accountant','Bachelor degree in Accounting','Salary 1000$','2021-09-01',5,users[1].Id,users[1].Id,'Recruiting'))
            db.session.add(RecruitmentRequest('HR','HR','Hanoi','HR','Full-time','HR','Bachelor degree in HR','Salary 1000$','2021-09-01',5,users[2].Id,users[2].Id,'Not Recruiting'))
            db.session.add(RecruitmentRequest('Software Engineer','Develop software','Da nang','Full-time','Intern','Develop software','Bachelor degree in Computer Science','Salary 1000$','2021-09-01',5,users[3].Id,users[3].Id,'Recruiting'))
            db.session.commit()
        if db.session.query(RecruitmentProgress).count() == 0:
            #seed recruitment progress
            requests = db.session.query(RecruitmentRequest).limit(5).all()
            db.session.add(RecruitmentProgress(requests[0].Id,requests[0].Position,2,'','2021-09-01','2021-09-01',fake.enum(ProgressStatus)))
            db.session.add(RecruitmentProgress(requests[1].Id,requests[1].Position,3,'','2021-09-01','2021-09-01',fake.enum(ProgressStatus)))
            db.session.add(RecruitmentProgress(requests[2].Id,requests[2].Position,4,'','2021-09-01','2021-09-01',fake.enum(ProgressStatus)))
            db.session.commit()
        if db.session.query(CadidateInfo).count() == 0:
            #for each recruitment progress, seed candidate info
            recruitmentProgresses = db.session.query(RecruitmentProgress).limit(5).all()
            db.session.add(CadidateInfo(Name=fake.name(),RecruitmentProgressId=recruitmentProgresses[0].Id,ResumeEvaluation=fake.enum(ResumeEvaluation),InterviewProgress=fake.enum(InterviewProgress),OfferStatus=fake.enum(OfferStatus),HiringStatus=fake.enum(HiringStatus),SubmissionChannel=fake.enum(SubmissionChannel),Resume='Resume',AssigneeId=recruitmentProgresses[0].RecruitmentRequest.AssigneeId))
            db.session.add(CadidateInfo(Name=fake.name(),RecruitmentProgressId=recruitmentProgresses[1].Id,ResumeEvaluation=fake.enum(ResumeEvaluation),InterviewProgress=fake.enum(InterviewProgress),OfferStatus=fake.enum(OfferStatus),HiringStatus=fake.enum(HiringStatus),SubmissionChannel=fake.enum(SubmissionChannel),Resume='Resume',AssigneeId=recruitmentProgresses[1].RecruitmentRequest.AssigneeId))
            db.session.add(CadidateInfo(Name=fake.name(),RecruitmentProgressId=recruitmentProgresses[2].Id,ResumeEvaluation=fake.enum(ResumeEvaluation),InterviewProgress=fake.enum(InterviewProgress),OfferStatus=fake.enum(OfferStatus),HiringStatus=fake.enum(HiringStatus),SubmissionChannel=fake.enum(SubmissionChannel),Resume='Resume',AssigneeId=recruitmentProgresses[2].RecruitmentRequest.AssigneeId))
            db.session.commit()
        if db.session.query(InterviewRecord).count() == 0:
            #for each candidate info, seed interview record
            cadidateInfos = db.session.query(CadidateInfo).limit(5).all()
            db.session.add(InterviewRecord(cadidateInfos[0].Id,'2021-09-01',fake.enum(Stage),Result=fake.enum(InterviewResult),InterviewerId=cadidateInfos[0].AssigneeId,InterviewRecord='InterviewRecord',InterviewEvaluation='InterviewEvaluation'))
            db.session.add(InterviewRecord(cadidateInfos[1].Id,'2021-09-01',fake.enum(Stage),Result=fake.enum(InterviewResult),InterviewerId=cadidateInfos[1].AssigneeId,InterviewRecord='InterviewRecord',InterviewEvaluation='InterviewEvaluation'))
            db.session.add(InterviewRecord(cadidateInfos[2].Id,'2021-09-01',fake.enum(Stage),Result=fake.enum(InterviewResult),InterviewerId=cadidateInfos[2].AssigneeId,InterviewRecord='InterviewRecord',InterviewEvaluation='InterviewEvaluation'))
            db.session.commit()
        return 'seed data successfully',200

