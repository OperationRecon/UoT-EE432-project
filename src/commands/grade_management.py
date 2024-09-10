import utils.helpers
from services import grade_service, user_service, subject_group_service, enrollment_service
from models.admin import Admin
from models.teacher import Teacher
from models.student import Student


def add_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subject_code = input("Enter subject code: ")
    student = input("Enter student ID: ")
    group = input('Enter student\'s group: ')
    sem = input("Enter semester: ")
    yearwork = input("Enter yearwork grades: ")
    final = input("Enter Final Grade: ")
    try:
        grade_service.add_grade((subject_code, student, sem, yearwork, final, group))
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
    
    subject = input("Enter subject code: ")
    sID = input("Enter student ID: ")
    sem = input("Enter semester: ")

    grade = grade_service.get_grade(sID, subject, sem)
    if not grade:
        print("Grade not found.")
        return

    print("Leave field empty if you don't want to update it.")
    subject_code = input(f"Enter new code ({grade.subject_code}): ") or grade.subject_code
    student_ID = input(f"Enter new student ID ({grade.student_id}): ") or grade.student_id
    semester = input(f"Enter new semester ({grade.semester}): ") or grade.semester
    subject_group = input(f"Enter new group ({grade.subject_group}): ") or grade.subject_group
    yearwork = input(f"Enter new yearwork grade ({grade.yearwork}): ") or grade.yearwork
    final = input(f"Enter new final exam grade ({grade.final}): ") or grade.final
    try:
        grade_service.update_grade((subject, sID, sem),
                                    {'subject_code':subject_code, 'student_ID':student_ID,
                                    'semester':semester,'yearwork':yearwork,'final':final,
                                    "subject_group": subject_group})
        if grade.subject_group != subject_group:
            update_capacity(subject_code, student_ID, semester, -1, group=grade.subject_group)
            update_capacity(subject_code, student_ID, semester, +1, group=subject_group)
        print("Grade updated successfully")
    except Exception as e:
        print(f"Error updating grade: {e}")


def assign_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin, Teacher]):
        return
    subject = input("Enter subject code: ")
    student = input("Enter student ID: ")
    sem = input("Enter semester: ")
    print("Leave field empty if you don't want to assign it.")
    yearwork = input("Enter yearwork grades: ")
    final = input("Enter Final Grade: ")

    try:
        group = grade_service.get_grade(student,subject,sem).subject_group
        grade_service.update_grade((subject, student, sem),
                                   {'subject_code': subject, 'student_ID': student,
                                    'semester': sem, 'yearwork': yearwork, 'final': final,
                                    'subject_group': group,})
        print("Grade assigned successfully!")
    except Exception as e:
        print(f"Error assigning grade: {e}")


def delete_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subject = input("Enter subject code: ")
    student = input("Enter student ID: ")
    sem = input("Enter semester: ")

    try:
        grade_service.delete_grade(student, subject, sem)
        print("Grade deleted successfully!")
    except Exception as e:
        print(f"Error deleting grade: {e}")


def get_subject_grades(user):
    if not utils.helpers.verify_role(type(user), [Admin, Teacher]):
        return
    subject = input("Enter subject code: ")
    sem = input("Enter semester: ")
    subject_group = input("Enter subject group: ")

    try:
        grades = grade_service.get_subject_grades(subject, sem, subject_group)
        for grade in grades:
            student = user_service.get_user(grade.student_id)
            print(f'Student: {student.name} ID: {student.id} {grade}\n')
    except Exception as e:
        print(f"Error fetching subject grades: {e}")


def get_student_grades(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    student_id = user.id if isinstance(user, Student) else input("Enter student ID: ")

    try:
        grades = grade_service.get_student_grades(student_id)
        for grade in grades:
            print(f'\n{grade}\n')
        print(f"The total passed units : {enrollment_service.get_all_passed_units(student_id)}")
    except Exception as e:
        print(f"Error fetching student grades: {e}")


def show_semester(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    student_id = user.id if isinstance(user, Student) else input("Enter student ID: ")
    semester = input("Enter semester: ")

    try:
        grades = grade_service.get_semester(student_id,semester)
        for grade in grades:
            print(f'\n{grade}\n')
    except Exception as e:
        print(f"Error fetching student grades: {e}")
    pass


def update_capacity(subject_code, student_id, semester, diff, group):
    capacity = int(subject_group_service.get_subject_group(subject_code, group, semester).capacity)
    subject_group_service.update_subject_group(subject_code, group, semester, {"capacity": capacity + diff})
