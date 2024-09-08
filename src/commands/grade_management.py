import utils.helpers
from services import grade_service, user_service
from models.admin import Admin
from models.teacher import Teacher
from models.student import Student


def add_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subject = input("Enter subject code: ")
    student = input("Enter student ID: ")
    sem = input("Enter semester: ")
    yearwork = input("Enter yearwork grades: ")
    final = input("Enter Final Grade: ")

    
    try:
        grade_service.add_grade((subject,student,sem,yearwork,final))
        print("Grade Added successully!")

    except Exception as e:
        print(f"Error adding grade: {e}")
    



def get_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subject = input("Enter subject code: ")
    studentID = input("Enter student ID: ")
    sem = input("Enter semester: ")
    try:
        student = user_service.get_user(studentID)
        if not student:
            print("Error: Student doesn't exist!")
            return
    except Exception as e:
        print(f'Error fetching student data: {e}')
    try:
        grade = grade_service.get_grade(studentID,subject,sem)

        if not grade:
            print('No grade to find!')
            return
        
        print(f'Student: {student.name}\nID: {student.id}\n{grade}')

    except Exception as e:
        print(f"Error fetching grade: {e}")

def update_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    pass

def assign_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin, Teacher]):
        return
    pass


def delete_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    pass


def get_subject_grades(user):
    if not utils.helpers.verify_role(type(user), [Admin, Teacher]):
        return
    pass


def get_student_grades(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    pass
