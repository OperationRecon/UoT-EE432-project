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
    print("\nAvailable commands:")

    categories = {
        "General": ["help", "exit", "login", "update password", "get current semester", "set current semester"],
        "User Management": ["add user", "delete user", "update user", "get user", "list users"],
        "Subject Management": ["add subject", "update subject", "delete subject", "list subjects"],
        "Subject Group Management": ["add subject group", "update subject group", "delete subject group",
                                     "list subject groups"],
        "Grade Management": ["add grade", "get grade", "update grade", "assign grade", "delete grade",
                             "show subject grades", "show student grades", "show semester grades"],
        "Enrollment Management": ["force enroll", "drop out", "force drop out", "enroll"]
    }

    for category, cmd_list in categories.items():
        if category = "User Management" and isinstance(user, [Student, Teacher]):
            continue
        print(f"\n{category}:")
        for cmd in cmd_list:
            if cmd in commands and isinstance(user, commands[cmd][1]):
                if cmd == "login":
                    print(f"  {cmd} - Log in with a different user")
                else:
                    print(f"  {cmd}")

    print("\nFor more information on a specific command, type 'help <command>'")


def command_help_detail(user, command):
    if not isinstance(user, commands[command][1]):
        print(f"Command '{command}' is not available for your user role.")
        return
    elif command not in commands:
        print(f"Command '{command}' does not exist.")
        return

    command_details = {
        "login": "Log in with a different user account",
        "help": "Display available commands or get help on a specific command",
        "exit": "Exit the application",
        "update password": "Change your current password",
        "get current semester": "Display the current academic semester",
        "add user": "Create a new user (admin, teacher, or student)",
        "delete user": "Remove a user from the system",
        "update user": "Modify user information",
        "get user": "Retrieve information about a specific user",
        "list users": "Display a list of all users",
        "add subject": "Create a new subject",
        "update subject": "Modify subject information",
        "delete subject": "Remove a subject from the system",
        "list subjects": "Display a list of all subjects",
        "add subject group": "Create a new subject group",
        "update subject group": "Modify subject group information",
        "delete subject group": "Remove a subject group",
        "list subject groups": "Display a list of all subject groups of a specific subject",
        "add grade": "Add a new grade for a student",
        "get grade": "Retrieve a specific grade",
        "update grade": "Modify an existing grade",
        "assign grade": "Assign a grade to a student for a subject",
        "delete grade": "Remove a grade from the system",
        "show subject grades": "Display grades for a specific subject",
        "show student grades": "Show grades for a specific student",
        "show semester grades": "Display grades and enrollments of a specific student for a semester",
        "force enroll": "Enroll a student in a subject group, bypassing restrictions",
        "drop out": "Remove a student from a subject group",
        "force drop out": "Remove a student from a subject group, bypassing restrictions",
        "enroll": "Enroll a student in a subject group",
        "set current semester": "Set the current academic semester"
    }

    print(f"\nCommand: {command}")
    print(f"Description: {command_details.get(command, 'No detailed description available.')}")
    print("Usage: Just type the command and follow the prompts.")


def detailed_help(user):
    command = input("Enter the command you need help with: ")
    command_help_detail(user, command)


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
        if command.startswith("help "):
            detailed_help(current_user)
        elif command and command in commands:
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
    "help <command>": (detailed_help, (Admin, Student, Teacher)),

    "exit": ("",(Admin,Student,Teacher)),

    "add subject": (add_subject,Admin),
    "update subject": (update_subject,Admin),
    "delete subject": (delete_subject,Admin),
    "list subjects": (list_subjects,Admin),

    "add subject group": (add_subject_group,Admin),
    "update subject group": (update_subject_group,Admin),
    "delete subject group": (delete_subject_group,Admin),
    "list subject groups":(list_subject_groups,Admin),

    "add grade": (add_grade,Admin),
    "get grade": (get_grade,Admin),
    "update grade": (update_grade,Admin),
    "assign grade": (assign_grade,(Admin,Teacher)),
    "delete grade": (delete_grade,Admin),
    "show subject grades": (get_subject_grades,(Admin,Teacher)),
    "show student grades": (get_student_grades,(Admin,Student)),
    "show semester grades" : (show_semester_grades,(Admin,Student)),

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
