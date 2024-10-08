import utils.helpers
from services import grade_service, user_service, subject_group_service, enrollment_service, subject_service
from models.admin import Admin
from models.teacher import Teacher
from models.student import Student
from utils.validation import *


def add_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    student = input("Enter student ID: ")
    student = validate_student_data(student)
    if not student:
        return
    while True:
        subject_code = input("Enter subject code: ")
        subject_code = validate_subject(subject_code)
        if not subject_code:
            return
        sem = validate_semester(input("Enter semester (e.g SPRING-2024): "))
        if not sem:
            return
        current_grades = grade_service.get_semester_grades(student, sem)
        current_subjects = [i.subject_code for i in current_grades]
        if subject_code in current_subjects:
            print(f"Subject: {subject_code} has already been added to the student with ID: {student} in {sem}.\nEnter another subject, or exit with 'exit'." )
            continue
        break
    subject_group_number = validate_subject_group(subject_code,input("Enter subject group: "),sem)
    if not subject_group_number:
        return
    yearwork = input("Enter yearwork grades: ")
    final = input("Enter Final Grade: ")

    try:
        grade_service.add_grade((subject_code, student, sem, yearwork, final, subject_group_number))
        print("Grade Added successully!")
    except Exception as e:
        print(f"Error adding grade: {e}")


def get_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    
    studentID = validate_student_data(input("Enter student ID: "))
    if not studentID:
        return
    
    subject_code = validate_subject(input("Enter subject code: "))
    if not subject_code:
        return

    sem = validate_semester(input("Enter semester (e.g SPRING-2024): "))
    if not sem:
        return
    
    try:
        grade = grade_service.get_grade(studentID,subject_code,sem)

        if not grade:
            print('No grade to find!')
            return
    
        student = user_service.get_user(studentID)
        print(f'Student: {student.name}\nID: {student.id}\n{grade}')

    except Exception as e:
        print(f"Error fetching grade: {e}")


def update_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subject = validate_subject(input("Enter subject code: "))
    if not subject:
        return
    sID = validate_student_data(input("Enter student ID: "))
    if not sID:
        return
    sem = validate_semester(input("Enter semester (e.g SPRING-2024): "))
    if not sem:
        return
    grade = grade_service.get_grade(sID, subject, sem)
    if not grade:
        print("Grade not found.")
        return
    print("Leave field empty if you don't want to update it.")
    subject_code = validate_subject(input(f"Enter new code ({grade.subject_code}): ") or grade.subject_code)
    if not subject_code:
        return
    student_ID = validate_student_data(input(f"Enter new student ID ({grade.student_id}): ") or grade.student_id)
    if not student_ID:
        return
    semester = validate_semester(input(f"Enter new semester ({grade.semester}): ") or grade.semester)
    if not semester:
        return
    subject_group = validate_subject_group(subject_code, input(f"Enter new group ({grade.subject_group}): ") or grade.subject_group, semester)
    if not subject_group:
        return
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
    subject_code = validate_subject(input("Enter subject code: "))
    if not subject_code:
        return
    student_id = validate_student_data(input("Enter student ID: "))
    if not student_id:
        return
    sem = validate_semester(input("Enter semester (e.g SPRING-2024): "))
    if not sem:
        return
    subject_group_number = validate_subject_group(subject_code, input("Enter subject group: "), sem)
    if not subject_group_number:
        return
    if user.user_type == "teacher" and user.id != subject_group_service.get_subject_group(subject_code, subject_group_number, sem).teacher_id:
        print("You are not allowed to assign a grade to this subject group!.")
        return
    print("Leave field empty if you don't want to assign it.")
    try:
        grade = grade_service.get_grade(student_id,subject_code,sem)
    except Exception as e:
        print(f"Error fetching grade: {e}")
        return
    if not grade:
        print('Student has not enrolled in this subject to assign a grade to. Enroll student to subject first to assign a grade.')
        return
    yearwork = input("Enter yearwork grades: ") or grade.yearwork
    final = input("Enter Final Grade: ") or grade.final
    try:
        grade_service.update_grade((subject_code, student_id, sem),
                                   {'subject_code': subject_code, 'student_ID': student_id,
                                    'semester': sem, 'yearwork': yearwork, 'final': final,})
        print("Grade assigned successfully!")

    except Exception as e:
        print(f"Error assigning grade: {e}")


def delete_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    subject_code = validate_subject(input("Enter subject code: "))
    if not subject_code:
        return
    student_id = validate_student_data(input("Enter student ID: "))
    if not student_id:
        return
    sem = validate_semester(input("Enter semester (e.g SPRING-2024): "))
    if not sem:
        return
    try:
        grade_service.delete_grade(student_id, subject_code, sem)
        print("Grade deleted successfully!")
    except Exception as e:
        print(f"Error deleting grade: {e}")


def get_subject_grades(user):
    if not utils.helpers.verify_role(type(user), [Admin, Teacher]):
        return
    
    subject_code = validate_subject(input("Enter subject code: "))
    if not subject_code:
        return

    sem = validate_semester(input("Enter semester (e.g SPRING-2024): "))
    if not sem:
        return

    subject_group = validate_subject_group(subject_code, input("Enter subject group: "), sem)
    if not subject_group:
        return

    try:
        grades = grade_service.get_subject_grades(subject_code, sem, subject_group)
        for grade in grades:
            student = user_service.get_user(grade.student_id)
            print(f'Student: {student.name} ID: {student.id} {grade}\n')
    except Exception as e:
        print(f"Error fetching subject grades: {e}")


def get_student_grades(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    student_id = user.id if isinstance(user, Student) else validate_student_data(input("Enter student ID: "))
    if not student_id:
        return

    try:
        grades = grade_service.get_student_grades(student_id)
        for grade in grades:
            print(grade)
        print(f"The total passed units : {enrollment_service.get_all_passed_units(student_id)}")
        print(f"The academic percentage : {get_academic_percentage(student_id)}")
    except Exception as e:
        print(f"Error fetching student grades: {e}")


def show_semester_grades(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    student_id = user.id if isinstance(user, Student) else validate_student_data(input("Enter student ID: "))
    if not student_id:
        return
    semester = input("Enter semester: ")
    try:
        grades = grade_service.get_semester_grades(student_id, semester)
        for grade in grades:
            print(f'\n{grade}\n')

    except Exception as e:
        print(f"Error fetching student grades: {e}")
    pass


def update_capacity(subject_code, student_id, semester, diff, group):
    capacity = int(subject_group_service.get_subject_group(subject_code, group, semester).capacity)
    subject_group_service.update_subject_group(subject_code, group, semester, {"capacity": capacity + diff})


def get_academic_percentage(student_id):
    grades = grade_service.get_student_grades(student_id)
    total_grade = 0
    student_grade = 0
    for grade in grades:
        subject = subject_service.get_subject(grade.subject_code)
        student_grade += int(subject.cr) * (int(grade.yearwork) + int(grade.final))
        total_grade += int(subject.cr) * 100

    return (student_grade/total_grade) * 100 if total_grade != 0 else 0
