from services import grade_service, user_service, subject_group_service, subject_service


def validate_user_data(user_id):
    if not user_service.get_user(user_id):
        print(f"User with id: {user_id} doesn't exist")
        return


def validate_subject(subject_code):
    if not user_service.get_user(subject_code):
        print(f"Subject with code: {subject_code} doesn't exist")
        return


def validate_subject_group(grade_data):
    if not subject_group_service.get_subject_group(subject_code, subject_group, semester):
        print(f"Subject with code: {subject_code} doesn't exist")
        return
