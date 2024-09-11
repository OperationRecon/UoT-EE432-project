from commands.enrollment_management import *
from commands.subject_management import *
from commands.user_management import *
from commands.grade_management import *
from commands.subject_group_management import *
from models.user import User
from models.admin import Admin
from models.student import Student
from models.teacher import Teacher
import services.enrollment_service as enrollment_service


def command_help(user):
    for i in commands.keys():
        if i == "login":
            print(i, " (With a different user)")
            continue
        if isinstance(user,commands[i][1]):
            print(i)


def display_main_menu():
    print("\nUniversity Administration System")
    print("Login by entering 'login' or close using 'exit'.")
    current_semester = enrollment_service.get_current_semester()
    if not current_semester:
        print("The semester hasn't started yet.")
    else:
        print(f"Current semester is: {current_semester}")


def display_user_menu(user):
    print(f"\nWelcome, {user.name}")
    print("Use 'help' to get a list of available commands.")


def handle_user_input():
    command = False
    current_user = None

    while True:
        if not current_user:
            display_main_menu()

        command = input(">>")
        if command and command in commands:
            if command == "exit":
                break

            elif command == 'login':
                current_user = login()
                if current_user:
                    display_user_menu(current_user)
                continue

            else:
                commands[command][0](current_user)

        else:
            print("Invalid command!")


def run_cli():
    handle_user_input()


# List of commands available to all users
commands = {
    "login": ("",(Admin,Student,Teacher)),
    "help": (command_help,(Admin,Student,Teacher)),
    "exit": ("",(Admin,Student,Teacher)),

    "add subject": (add_subject,Admin),
    "update subject": (update_subject,Admin),
    "delete subject": (delete_subject,Admin),
    "list subjects": (list_subjects,Admin),

    "add subject group": (add_subject_group,Admin),
    "update subject group": (update_subject_group,Admin),
    "delete subject group": (delete_subject_group,Admin),

    "add grade": (add_grade,Admin),
    "get grade": (get_grade,Admin),
    "update grade": (update_grade,Admin),
    "assign grade": (assign_grade,(Admin,Teacher)),
    "delete grade": (delete_grade,Admin),
    "get subject grades": (get_subject_grades,(Admin,Teacher)),
    "get student grades": (get_student_grades,(Admin,Student)),
    "show semester" : (show_semester_grades,(Admin,Student)),

    "add user": (add_user,Admin),
    "delete user": (delete_user,Admin),
    "update user": (update_user,Admin),
    "update password": (update_password,(Admin,Teacher,Student)),
    "get user": (get_user,Admin),
    "list users": (get_all_users,Admin),

    "force enroll": (force_enroll,Admin),
    "drop out": (drop_out,(Student,Admin)),
    "force drop out" : (force_drop_out,(Admin)),
    "enroll": (enroll,(Admin,Student)),

    "set current semester": (set_current_semester,Admin),
    "get current semester": (get_current_semester,(Admin,Student,Teacher))
}
