import utils.helpers
from models.admin import Admin
from models.teacher import Teacher
from models.student import Student

def add_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    pass


def get_grade(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    pass


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
