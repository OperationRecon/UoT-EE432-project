from models.student import Student
from models.admin import Admin
import utils.helpers
from services import subject_service, subject_group_service, grade_service, enrollment_service
from utils.validation import *
from commands.grade_management import get_academic_percentage


def enroll(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    student_id = user.id if isinstance(user, Student) else input("Enter student ID: ")
    student_id = validate_student_data(student_id)
    if not student_id:
        return
    try:
        available_subjects_codes = subject_service.get_available_subjects(student_id)
        available_subjects = [subject_service.get_subject(subject) for subject in available_subjects_codes]
    except Exception as e:
        print(f"Error fetching available subjects: {e}")
        return
    show_available_subjects(available_subjects)
    while True:
        subject_code = input("Enter subject code: ")
        subject_code = validate_subject(subject_code)
        if not subject_code:
            return
        maximum_units = 21 if get_academic_percentage(student_id) >= 75 else 18
        subject = subject_service.get_subject(subject_code)
        if enrollment_service.get_current_units(student_id) + subject.cr > maximum_units:
            print(f"Can't enroll more than {maximum_units}.  Enter another subject or exit with 'exit'.")
            continue
        if subject_code not in available_subjects_codes:
            print("Can't enroll in this subject due to insufficient requirements. Enter another subject or exit with 'exit'.")
            continue
        break
    try:
        available_groups = subject_group_service.get_available_subject_groups(subject_code)
    except Exception as e:
        print(f"Error fetching available subject Groups: {e}")
        return
    show_available_subject_groups(available_groups)
    semester = enrollment_service.get_current_semester()
    while True:
        subject_group_number = input("Enter subject group: ")
        if subject_group_number == "exit":
            return
        try:
            subject_group = subject_group_service.get_subject_group(subject_code, subject_group_number, semester)
            if not subject_group:
                print("Subject group not found. Enter another subject group or exit with 'exit'.")
                continue
            if subject_group_number not in [group.subject_group for group in available_groups]:
                print("Subject capacity is full. Enter another subject group or exit with 'exit'.")
                continue
            grade_service.add_grade((subject_code, student_id, semester, None, None, subject_group_number))
            print("Enrolled successfully!")
            return
        except Exception as e:
            print(f"Error enrolling: {e}")


def show_available_subjects(available_subjects):
    while True:
        show = input(r"Do you want to view available subject:(Y\N)")
        if show == "N":
            return
        elif show == "Y":
            break
    for subject in available_subjects:
        print(subject)
    

def show_available_subject_groups(available_groups):
    while True:
        show = input(r"Do you want to view available groups:(Y\N)")
        if show == "N":
            return
        elif show == "Y":
            break
    if not available_groups:
        print("There are not groups yet")
        return
    for group in available_groups:
        print(group)


def force_drop_out(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    student_id = input("Enter student ID: ")
    student_id = validate_student_data(student_id)
    if not student_id:
        return
    sem = enrollment_service.get_current_semester()
    current_grades = grade_service.get_semester_grades(student_id, sem)
    current_subjects = [i.subject_code for i in current_grades]
    while True:
        subject_code = input("Enter subject code: ")
        subject_code = validate_subject(subject_code)
        if not subject_code:
            return
        if subject_code not in current_subjects:
            print(f"{subject_code} has not been enrolled.   Enter another subject or exit with 'exit'.")
            continue
        break

    try:
        grade_service.delete_grade(subject_code, student_id, sem)
        print("Student dropped out successfully!")
    except Exception as e:
        print(f"Error dropping student out: {e}")


def drop_out(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return

    student_id = user.id if isinstance(user, Student) else input("Enter student ID: ")
    student_id = validate_student_data(student_id)
    if not student_id:
        return
    sem = enrollment_service.get_current_semester()
    current_grades = grade_service.get_semester_grades(student_id, sem)
    current_subjects = [i.subject_code for i in current_grades]
    while True:
        subject_code = input("Enter subject code: ")
        subject_code = validate_subject(subject_code)
        if not subject_code:
            return
        coreq = enrollment_service.check_coreq_to_drop_out(student_id, subject_code)
        subject = subject_service.get_subject(subject_code)
        if coreq:
            print(f"you have to drop enrolled corequisty subject. Enter another subject or exit with 'exit'.")
            continue
        if enrollment_service.get_current_units(student_id) - subject.cr < 12:
            print("This subject will not be deleted for not reaching less than the minimum number of units.  Enter another subject or exit with 'exit'.")
            continue
        if subject_code not in current_subjects:
            print(f"{subject_code} has not been enrolled. Enter another subject or exit with 'exit'.")
            continue
        break
    try:
        grade_service.delete_grade(subject_code, student_id,  sem)
        print("Student dropped out successfully!")
    except Exception as e:
        print(f"Error dropping student out: {e}")
    pass


def force_enroll(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    # calls add grade with none without check
    student_id = input("Enter student ID: ")
    student_id = validate_student_data(student_id)
    if not student_id:
        return
    sem = enrollment_service.get_current_semester()
    current_grades = grade_service.get_semester_grades(student_id, sem)
    current_subjects = [i.subject_code for i in current_grades]
    while True:
        subject_code = input("Enter subject code: ")
        subject_code = validate_subject(subject_code)
        if not subject_code:
            return
        if subject_code in current_subjects:
            print(f"{subject_code} already has been enrolled.  Enter another subject group or exit with 'exit'.")
            continue
        break
    while True:
        subject_group_number = input("Enter subject group: ")
        if subject_group_number == "exit":
            return
        try:
            subject_group = subject_group_service.get_subject_group(subject_code, subject_group_number, sem)
            if not subject_group:
                print("Subject group not found. Enter another subject group or exit with 'exit'.")
                continue
        except Exception as e:
            print(f"Error enrolling: {e}")
        break
    try:
        grade_service.add_grade((subject_code, student_id, sem, None, None, subject_group_number))
        print("Student Enrolled successully!")

    except Exception as e:
        print(f"Error enrolling student: {e}")


def set_current_semester(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    current_semester = input("Enter current semester (e.g: SPRING-2024): ")
    try:
        enrollment_service.set_current_semester(current_semester)
        print("Current semester was set successully!")

    except Exception as e:
        print(f"Error setting current semester: {e}")


def get_current_semester(user):
    try:
        current_semester = enrollment_service.get_current_semester()
        print(f"Current Semester is: {current_semester}")
    except Exception as e:
        print(f"Error fetching current semester: {e}")
