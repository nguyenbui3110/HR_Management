"""empty message

Revision ID: b80f43bfaec4
Revises: 
Create Date: 2024-04-04 10:20:42.811807

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text
from app.extensions import db


# revision identifiers, used by Alembic.
revision = 'b80f43bfaec4'
down_revision = None
branch_labels = None
depends_on = None

def drop_type_if_exists():
    # Connect to the database
    conn = db.engine.connect()

    # SQL statement to drop the type if it exists
    sql_statement = text("""
        DROP TYPE IF EXISTS progressstatus, resumeevaluation, interviewprogress, offerstatus, hiringstatus, submissionchannel, stage, interviewresult CASCADE;
    """)

    # Execute the SQL statement
    conn.execute(sql_statement)

    # Close the database connection
    conn.close()

def upgrade():
    drop_type_if_exists()
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('Id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Username', sa.String(length=50), nullable=False),
    sa.Column('Email', sa.String(length=50), nullable=False),
    sa.Column('Password', sa.String(length=255), nullable=True),
    sa.Column('Role', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('Email'),
    sa.UniqueConstraint('Username')
    )
    op.create_table('recruitmentRequest',
    sa.Column('Id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Position', sa.String(length=255), nullable=True),
    sa.Column('JobDescription', sa.Text(), nullable=True),
    sa.Column('City', sa.String(length=255), nullable=True),
    sa.Column('Department', sa.String(length=255), nullable=True),
    sa.Column('RecruitmentType', sa.String(length=50), nullable=True),
    sa.Column('JobDuties', sa.Text(), nullable=True),
    sa.Column('RequiredQualifications', sa.Text(), nullable=True),
    sa.Column('SalaryAndBenefit', sa.Text(), nullable=True),
    sa.Column('ExpectedStartDate', sa.Date(), nullable=True),
    sa.Column('HeadCount', sa.Integer(), nullable=True),
    sa.Column('RequesterId', sa.Integer(), nullable=True),
    sa.Column('AssigneeId', sa.Integer(), nullable=True),
    sa.Column('Status', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['AssigneeId'], ['users.Id'], ),
    sa.ForeignKeyConstraint(['RequesterId'], ['users.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('recruitmentProgress',
    sa.Column('Id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('RecruitmentRequestId', sa.Integer(), nullable=True),
    sa.Column('Position', sa.String(length=50), nullable=True),
    sa.Column('NumberOfNewHire', sa.Integer(), nullable=True),
    sa.Column('NewHires', sa.Text(), nullable=True),
    sa.Column('RecruitmentStartDate', sa.Date(), nullable=True),
    sa.Column('RecruitmentCompleteDate', sa.Date(), nullable=True),
    sa.Column('Status', sa.Enum('INPROGRESS', 'COMPLETE', name='progressstatus'), nullable=True),
    sa.ForeignKeyConstraint(['RecruitmentRequestId'], ['recruitmentRequest.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('cadidateInfo',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=255), nullable=True),
    sa.Column('RecruitmentProgressId', sa.Integer(), nullable=True),
    sa.Column('ResumeEvaluation', sa.Enum('PASSED', 'REJECTED', 'EVALUATED', name='resumeevaluation'), nullable=True),
    sa.Column('InterviewProgress', sa.Enum('PASSED_1', 'FAIL_1', 'PASSED_2', 'FAIL_2', 'WAITING_1', 'WAITING_2', name='interviewprogress'), nullable=True),
    sa.Column('OfferStatus', sa.Enum('ISSUED', 'REJECTED', name='offerstatus'), nullable=True),
    sa.Column('HiringStatus', sa.Enum('HIRED', 'NOT_HIRED', name='hiringstatus'), nullable=True),
    sa.Column('SubmissionChannel', sa.Enum('COMPANY_WEBSITE', 'INTERNALLY_REFERRED', 'LINKEDIN', name='submissionchannel'), nullable=True),
    sa.Column('Resume', sa.String(length=255), nullable=True),
    sa.Column('AssigneeId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['AssigneeId'], ['users.Id'], ),
    sa.ForeignKeyConstraint(['RecruitmentProgressId'], ['recruitmentProgress.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('interviewRecord',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('CandidateId', sa.Integer(), nullable=True),
    sa.Column('InterviewDate', sa.Date(), nullable=True),
    sa.Column('InterviewStage', sa.Enum('FIRST', 'SECOND', name='stage'), nullable=True),
    sa.Column('Result', sa.Enum('PASS', 'REJECT', name='interviewresult'), nullable=True),
    sa.Column('InterviewerId', sa.Integer(), nullable=True),
    sa.Column('InterviewRecord', sa.Text(), nullable=True),
    sa.Column('InterviewEvaluation', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['CandidateId'], ['cadidateInfo.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interviewRecord')
    op.drop_table('cadidateInfo')
    op.drop_table('recruitmentProgress')
    op.drop_table('recruitmentRequest')
    op.drop_table('users')
    # ### end Alembic commands ###
