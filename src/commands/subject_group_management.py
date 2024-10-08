from models.admin import Admin
from utils.validation import *
from utils.helpers import *
from services import subject_group_service, enrollment_service
from models.subject_group import SubjectGroup


def add_subject_group(user):
    if not verify_role(type(user), [Admin]):
        return
        
    subject_code = validate_subject(input("Enter subject's code: "))
    if not subject_code:
        return

    semester = validate_semester(input("Enter semester (e.g SPRING-2024): "))
    if not semester:
        return
    subject_group = input("Enter subject group: ")
    maximum_capacity = input("Enter maximum capacity: ")
    teacher_id = input("Enter teacher ID: ")
    if teacher_id:
        teacher_id = validate_teacher_data(teacher_id)
        if not teacher_id: return

    try:
        subject_group_service.add_subject_group((subject_code, teacher_id, subject_group, maximum_capacity, semester, 0))
        print("Subject Group added successfully")
    except Exception as e:
        print(f"Error adding subject group: {e}")


def update_subject_group(user):
    if not verify_role(type(user), [Admin]):
        return
    subject_code = validate_subject(input("Enter subject code to update: "))
    if not subject_code:
        return
    semester = validate_semester(input("Enter semester (e.g SPRING-2024): "))
    if not semester:
        return
    subject_group_number = validate_subject_group(subject_code, input("Enter subject group to update: "), semester)
    if not subject_group_number:
        return
    try:
        subject_group = subject_group_service.get_subject_group(subject_code,subject_group_number,semester)
    
    except Exception as e:
        print(f"Error fetching Group: {e}")

    print("Leave field empty if you don't want to update it.")
    teacher_id = input(f"Enter new teacher ID ({subject_group.teacher_id}): ") or subject_group.teacher_id
    if teacher_id:
        teacher_id = validate_teacher_data(teacher_id)
        if not teacher_id: return
    maximum_capacity = input(f"Enter new maximum capacity ({subject_group.maximum_capacity}): ") or subject_group.maximum_capacity
    
    try:
        subject_group_service.update_subject_group(subject_code, subject_group_number, semester, {
            "maximum_capacity": maximum_capacity, "teacher_id": teacher_id})
        print("Subject Group updated successfully")
    
    except Exception as e:
        print(f"Error updating subject group: {e}")


def delete_subject_group(user):
    if not verify_role(type(user), [Admin]):
        return
    
    subject_code = validate_subject(input("Enter subject code: "))
    if not subject_code:
        return
    semester = validate_semester(input("Enter semester (e.g SPRING-2024): "))
    if not semester:
        return
    subject_group_number = validate_subject_group(subject_code, input("Enter subject group: "),semester)
    if not subject_group_number:
        return
    try:
        subject_group = subject_group_service.get_subject_group(subject_code, subject_group_number, semester)
        if not subject_group:
            print("Subject not found.")
            return
        
        subject_group_service.delete_subject_group(subject_code, subject_group_number, semester)
        print("Subject Group deleted successfully")
        
    except Exception as e:
        print(f"Error deleting subject group: {e}")


def list_subject_groups(user):
    if not verify_role(type(user), [Admin]):
        return

    subject_code = validate_subject(input("Enter subject code: "))
    if not subject_code:
        return

    try:
        semester = enrollment_service.get_current_semester()
        try:
            subject_groups = subject_group_service.get_subject_groups(subject_code, semester)
        except Exception as e:
            print(f"Error fetching current subject groups: {e}")
            return

        if not subject_groups:
            print("No subject groups found in the current semester.")
        else:
            print(f"\n{subject_code} has {str(len(subject_groups))} subject groups in the current semester {semester}:")
            for group in subject_groups:
                print(group)
    except Exception as e:
        print(f"Error fetching current semester: {e}")

    previous = input("Do you want to show groups of previous semester?(Y/N): ")
    if previous == "Y":
        try:
            subject_groups = subject_group_service.get_subject_groups(subject_code, "*")
        except Exception as e:
            print(f"Error fetching previous subject groups: {e}")
            return
        if not subject_groups:
            print("No subject groups found in previous semesters.")
        else:
            print(f"\n{subject_code} has {str(len(subject_groups))} subject groups in the previous semesters:")
            for group in subject_groups:
                print(group)


