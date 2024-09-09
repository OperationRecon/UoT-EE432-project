from models.student import Student
from models.admin import Admin
import utils.helpers
from services import subject_service, subject_group_service, grade_service


def enroll(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    student_id = user.id if isinstance(user, Student) else input("Enter student ID: ")
    subject_code = input("Enter subject code: ")
    subject_group_number = input("Enter subject group: ")
    semester = input("Enter current semester: ")

    try:
        subject = subject_service.get_subject(subject_code)
        if not subject:
            print("Subject not found.")
            return
        subject_group = subject_service.get_subject(subject_code, subject_group_number, semester)
        if not subject_group:
            print("Subject group not found.")
            return
        capacity = utils.helpers.get_capacity(subject_group)
        if not utils.helpers.check_prereq(student_id, subject_code) or not utils.helpers.check_coreq(student_id, subject_code):
            print("Can't enroll in this subject due to insufficient requirements")
        if int(capacity) >= int(subject_group.maximum_capacity):
            print("Subject capacity is full.")
            return
        grade_service.add_grade((subject_code, student_id, semester, None, None))
        #subject_service.update_subject(subject_code, {"capacity": str(int(subject.capacity) + 1)})
        print("Enrolled successfully!")
    except Exception as e:
        print(f"Error enrolling: {e}")


def show_available_subjects(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    student_id = user.id if isinstance(user, Student) else input("Enter student ID: ")
    try:
        subjects = subject_service.get_all_subjects()
        available_subjects = [[sg for sg in get_all_subject_groups(s.subject_code) if int(utils.helpers.get_capacity(sg)) < int(sg.maximum_capacity) and utils.helpers.check_prereq(student_id, s.code) and utils.helpers.check_coreq(student_id, s.code)] for s in subjects]
        for subject in available_subjects:
            for subject_group in subject:
                print(
                    f"Code: {subject.code}, Title: {subject.title}, Available Seats: {int(subject_group.maximum_capacity) - int(utils.helpers.get_capacity(s))}")
    except Exception as e:
        print(f"Error fetching available subjects: {e}")


def drop_out(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    #calls delete grade
    subject = input("Enter subject code: ")
    student = input("Enter student ID: ")
    sem = input("Enter semester: ")

    try:
        grade_service.delete_grade(student, subject, sem)
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
    sem = input("Enter semester: ")

    
    try:
        grade_service.add_grade((subject,student,sem,0,0))
        print("Student Enrolled successully!")

    except Exception as e:
        print(f"Error enrolling student: {e}")

