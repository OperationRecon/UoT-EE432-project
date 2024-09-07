from models.admin import Admin
import utils.helpers
from services import subject_service


def add_subject(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return 
    code = input("Enter subject's code: ")
    title = input("Enter subject's title: ")
    preq = input("Enter subject's prequesites: ")
    coreq = input("Enter subject's co-requisites: ")
    description = input("Enter subject's description: ")
    cr = input("Enter subject's credits: ")
    faculty = input("Enter subject's faculty: ")
    dept = input("Enter subject's department: ")
    branch = input("Enter subject's branch: ")
    try:
        subject_service.add_subject((code, title, preq, coreq, description, cr, faculty, dept, branch, description))
    except Exception as e:
        print(e)
        return
    print("Subject added successfully")

