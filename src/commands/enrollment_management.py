from models.student import Student
from models.admin import Admin
import utils.helpers
from services import subject_service, subject_group_service, grade_service, enrollment_service



def enroll(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    student_id = user.id if isinstance(user, Student) else input("Enter student ID: ")
    show_available_subjects(student_id)
    subject_code = input("Enter subject code: ")
    show_available_subject_groups(subject_code)
    subject_group_number = input("Enter subject group: ")
    semester = enrollment_service.get_current_semester()

    try:
        subject = subject_service.get_subject(subject_code)
        if not subject:
            print("Subject not found.")
            return
        subject_group = subject_service.get_subject(subject_code, subject_group_number, semester)
        if not subject_group:
            print("Subject group not found.")
            return
        # if not utils.helpers.check_prereq(student_id, subject_code) or not utils.helpers.check_coreq(student_id, subject_code):
        if subject not in subject_service.get_available_subjects(student_id):
            print("Can't enroll in this subject due to insufficient requirements")
        if int(subject_group.capacity) >= int(subject_group.maximum_capacity):
            print("Subject capacity is full.")
            return
        grade_service.add_grade((subject_code, student_id, semester, None, None))
        #subject_service.update_subject(subject_code, {"capacity": int(subject.capacity) + 1})
        print("Enrolled successfully!")
    except Exception as e:
        print(f"Error enrolling: {e}")


def show_available_subjects(student_id):
    while True:
        show = input(r"Do you want to view available subject:(Y\N)")
        if show == "N":
            return
        elif show == "Y":
            break
    try:
        available_subjects = subject_service.get_available_subjects(student_id)
        for subject in available_subjects:
            subject = subject_service.get_subject(subject)
            print(
                    f"Code: {subject.code}, Title: {subject.title}")
    except Exception as e:
        print(f"Error fetching available subjects: {e}")


def show_available_subject_groups(subject_code):
    pass


def force_drop_out(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    subject = input("Enter subject code: ")
    student = input("Enter student ID: ")
    sem = enrollment_service.get_current_semester()

    try:
        grade_service.delete_grade(student, subject, sem)
        print("Student dropped out successfully!")
    except Exception as e:
        print(f"Error dropping student out: {e}")
    pass


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
        print(f"you have to drop enrolled {subject_code}'s co requisty {coreq}")
        return
    if enrollment_service.get_current_units(student) - subject.cr < 12:
        print("This subject will not be deleted for not reaching less than the minimum number of units.")
        return
    try:
        grade_service.delete_grade(subject_code,student,  sem,grade.subject_group)
        print("Student dropped out successfully!")
    except Exception as e:
        print(f"Error dropping student out: {e}")
    pass




def force_enroll(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    # calls add grade with none without check
    subject = input("Enter subject code: ")
    student = input("Enter student ID: ")
    sem = enrollment_service.get_current_semester()

    try:
        grade_service.add_grade((subject, student, sem, 0, 0))
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
