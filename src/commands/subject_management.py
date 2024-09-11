from models.admin import Admin
import utils.helpers
from services import subject_service
from models.subject import Subject
from utils.validation import *


def add_subject(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return 
    
    code = input("Enter subject's code: ")
    title = input("Enter subject's title: ")
    try:
        preq = " ".join([validate_subject(subject) for subject in input("Enter subject's prerequisites (space separated): ").split()])
        coreq = " ".join([validate_subject(subject) for subject in input("Enter subject's co-requisites (space separated): ").split()])
    except:
        return
    description = input("Enter subject's description: ")
    cr = validate_int(input("Enter subject's credits: "))
    if not cr:
        return
    faculty = input("Enter subject's faculty: ")
    dept = input("Enter subject's department: ")
    branch = input("Enter subject's branch: ")
    try:
        subject_service.add_subject((code, title, preq, coreq, description, cr,
                                     faculty, dept, branch))
        print("Subject added successfully")
    except Exception as e:
        print(f"Error adding subject: {e}")


def delete_subject(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return

    subject_code = validate_subject(input("Enter subject code to delete: "))
    if not subject_code:
        return

    try:
        subject_service.delete_subject(subject_code)
        print("Subject deleted successfully")
    except Exception as e:
        print(f"Error deleting subject: {e}")


def update_subject(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return

    subject_code = validate_subject(input("Enter subject code to update: "))
    if not subject_code:
        return

    subject = subject_service.get_subject(subject_code)
    print("Leave field empty if you don't want to update it.")
    code = input(f"Enter new code ({subject.code}): ") or subject.code
    title = input(f"Enter new title ({subject.title}): ") or subject.title
    try:
        preq = input(f"Enter new prerequisites ({subject.preq}): ") or subject.preq
        preq = " ".join([validate_subject(subject) for subject in preq.split()])
        coreq = input(f"Enter new co-requisites ({subject.coreq}): ") or subject.coreq
        coreq = " ".join([validate_subject(subject) for subject in coreq.split()])
    except:
        return
    description = input(f"Enter new description ({subject.description}): ") or subject.description
    cr = input(f"Enter new credits ({subject.cr}): ") or subject.cr
    cr = validate_int(cr)
    if not cr:
        return
    faculty = input(f"Enter new faculty ({subject.faculty}): ") or subject.faculty
    dept = input(f"Enter new department ({subject.dept}): ") or subject.dept
    branch = input(f"Enter new branch ({subject.branch}): ") or subject.branch

    try:
        subject_service.update_subject(subject_code, {
            "code": code, "title": title, "preq": preq, "coreq": coreq,
            "description": description, "cr": cr, "faculty": faculty,
            "dept": dept, "branch": branch
        })
        print("Subject updated successfully")
    except Exception as e:
        print(f"Error updating subject: {e}")


def list_subjects(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subjects = subject_service.get_all_subjects()
    if not subjects:
        print("No subjects found.")
        return
    for subject in subjects:
        print(subject)
