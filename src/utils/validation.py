from services import grade_service, user_service, subject_group_service, subject_service


def validate_student_data(user_id):
    if user_id =="exit":
        return
    user = user_service.get_user(user_id)
    while not user or user.user_type != "student":
        print(f"Student with id: {user_id} doesn't exist.")
        user_id = input("Enter another student ID or exit with 'exit': ")
        if user_id == "exit":
            return None
        user = user_service.get_user(user_id)
        continue
    return user_id

def validate_teacher_data(user_id):
    if user_id =="exit":
        return
    user = user_service.get_user(user_id)
    while not user or user.user_type != "teacher":
        print(f"Student with id: {user_id} doesn't exist.")
        user_id = input("Enter another teacher ID or exit with 'exit': ")
        if user_id == "exit":
            return None
        user = user_service.get_user(user_id)
        continue
    return user_id



def validate_subject(subject_code):
    if subject_code =="exit":
        return
    subject = subject_service.get_subject(subject_code)
    while not subject:
        print(f"Subject with code: {subject_code} doesn't exist.")
        subject_code = input("Enter another subject or exit with 'exit': ")
        if subject_code == "exit":
            return None
        subject = subject_service.get_subject(subject_code)
        continue
    return subject_code


def validate_subject_group(grade_data):
    if not subject_group_service.get_subject_group(subject_code, subject_group, semester):
        print(f"Subject with code: {subject_code} doesn't exist")
        return
