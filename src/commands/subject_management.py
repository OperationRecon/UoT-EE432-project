from models.admin import Admin
import utils.helpers
from services import subject_service
from models.subject import Subject


def add_subject(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return 
    code = input("Enter subject's code: ")
    title = input("Enter subject's title: ")
    preq = input("Enter subject's prerequisites (space separated): ") #.split() ???
    coreq = input("Enter subject's co-requisites (space separated): ") #.split() ???
    description = input("Enter subject's description: ")
    cr = input("Enter subject's credits: ")
    faculty = input("Enter subject's faculty: ")
    dept = input("Enter subject's department: ")
    branch = input("Enter subject's branch: ")
    capacity = input("Enter subject's capacity: ")
    maximum_capacity = input("Enter subject's maximum capacity: ")
    try:
        subject_service.add_subject((code, title, preq, coreq, description, cr,
                                     faculty, dept, branch, capacity, maximum_capacity))
        print("Subject added successfully")
    except Exception as e:
        print(f"Error adding subject: {e}")


def delete_subject(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subject_code = input("Enter subject code to delete: ")
    try:
        subject_service.delete_subject(subject_code)
        print("Subject deleted successfully")
    except Exception as e:
        print(f"Error deleting subject: {e}")


def update_subject(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subject_code = input("Enter subject code to update: ")
    subject = subject_service.get_subject(subject_code)
    if not subject:
        print("Subject not found.")
        return

    print("Leave field empty if you don't want to update it.")
    code = input(f"Enter new code ({subject.code}): ") or subject.code
    title = input(f"Enter new title ({subject.title}): ") or subject.title
    preq = input(f"Enter new prerequisites ({subject.preq}): ") or subject.preq
    coreq = input(f"Enter new co-requisites ({subject.coreq}): ") or subject.coreq
    description = input(f"Enter new description ({subject.description}): ") or subject.description
    cr = input(f"Enter new credits ({subject.cr}): ") or subject.cr
    faculty = input(f"Enter new faculty ({subject.faculty}): ") or subject.faculty
    dept = input(f"Enter new department ({subject.dept}): ") or subject.dept
    branch = input(f"Enter new branch ({subject.branch}): ") or subject.branch
    capacity = input(f"Enter new capacity ({subject.capacity}): ") or subject.capacity
    maximum_capacity = input(f"Enter new maximum_capacity ({subject.maximum_capacity}): ") or subject.maximum_capacity

    try:
        subject_service.update_subject(subject_code, {
            "code": code, "title": title, "preq": preq, "coreq": coreq,
            "description": description, "cr": cr, "faculty": faculty,
            "dept": dept, "branch": branch, "capacity": capacity, "maximum_capacity": maximum_capacity
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


def assign_teacher_to_subject(user): # Needs revision
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subject_id = input("Enter subject code: ")
    teacher_id = input("Enter teacher ID: ")
    try:
        subject_service.assign_teacher(subject_id, teacher_id)
        print("Teacher assigned to subject successfully")
    except Exception as e:
        print(f"Error assigning teacher to subject: {e}")
