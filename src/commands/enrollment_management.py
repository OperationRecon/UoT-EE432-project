from models.student import Student
from models.admin import Admin
import utils.helpers


def enroll(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    # calls add grade with none
    pass


def show_available_subjects(user):
    pass


def drop_out(user):
    if not utils.helpers.verify_role(type(user), [Admin, Student]):
        return
    #calls delete grade
    pass


def force_enroll(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    # calls add grade with none without check
    pass
