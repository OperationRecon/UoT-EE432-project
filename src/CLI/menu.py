from commands.subject_management import *
from commands.user_management import *
from models.user import User
from services import user_service, subject_service, enrollment_service, grade_service


def command_help(user):
    for i in commands.keys():
        if i == "login":
            print(i, " (With a different user)")
            continue
        print(i)


def display_main_menu():
    print("\nUniversity Administration System")
    print("Login by entering 'login' or close using 'exit'.")


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
                commands[command](current_user)

        else:
            print("Invalid command!")


def run_cli():
    handle_user_input()


# List of commands available to all users
commands = {"login": "", "help": command_help, "exit": "", "add subject": add_subject, "remove subject": remove_subject}