from models.student import Student
from models.admin import Admin
import utils.helpers
from services import subject_service, subject_group_service, grade_service, enrollment_service


def enroll(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    student_id = user.id if isinstance(user, Student) else input("Enter student ID: ")
    try:
        available_subjects_codes = subject_service.get_available_subjects(student_id)
        available_subjects = [subject_service.get_subject(subject) for subject in available_subjects_codes]
    except Exception as e:
        print(f"Error fetching available subjects: {e}")
        return
    show_available_subjects(available_subjects)
    while True:
        subject_code = input("Enter subject code: ")
        if subject_code == 'exit':
            return
        if subject_code not in available_subjects_codes:
            print("Can't enroll in this subject due to insufficient requirements. Enter another or exit with 'exit'.")
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
        try:
            subject = subject_service.get_subject(subject_code)
            if not subject:
                print("Subject not found.")
                return
            subject_group = subject_group_service.get_subject_group(subject_code, subject_group_number, semester)
            if not subject_group:
                print("Subject group not found.")
                continue
            if subject_group_number not in [group.subject_group for group in available_groups]:
                print("Subject capacity is full.")
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
    for group in available_groups:
        print(group)


def force_drop_out(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    subject_code = input("Enter subject code: ")
    student = input("Enter student ID: ")
    sem = enrollment_service.get_current_semester()

    try:
        grade_service.delete_grade(subject_code, student, sem)
        print("Student dropped out successfully!")
    except Exception as e:
        print(f"Error dropping student out: {e}")


def drop_out(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    subject_code = input("Enter subject code: ")
    student = user.id if isinstance(user, Student) else input("Enter student ID: ")
    sem = enrollment_service.get_current_semester()
    coreq = enrollment_service.check_coreq_to_drop_out(student,subject_code)
    subject = subject_service.get_subject(subject_code)
    grade = grade_service.get_grade(student,subject_code,sem)
    if coreq:
        print(f"you have to drop enrolled {subject_code}'s co-requisites {coreq}")
        return
    if enrollment_service.get_current_units(student) - subject.cr < 12:
        print("This subject will not be deleted for not reaching less than the minimum number of units.")
        return
    try:
        grade_service.delete_grade(subject_code, student, sem, grade.subject_group)
        print("Student dropped out successfully!")
    except Exception as e:
        print(f"Error dropping student out: {e}")
    pass


def force_enroll(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    # calls add grade with none without check
    subject_code = input("Enter subject code: ")
    student = input("Enter student ID: ")
    subject_group = input("Enter subject group: ")
    sem = enrollment_service.get_current_semester()
    try:
        grade_service.add_grade((subject_code, student, sem, None, None, subject_group))
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
