from enum import Enum

class InterviewProgressEnum(Enum):
    PASSED_1 = "Passed the first interview"
    FAIL_1 = "Failed the first interview"
    PASSED_2 = "Passed the second interview"
    FAIL_2 = "Failed the second interview"
    WAITING_1 = "Waiting for the first interview"
    WAITING_2 = "Waiting for the second interview"