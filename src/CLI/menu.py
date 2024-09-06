from commands.subject_management import *
from commands.user_management import *
from models.user import User
from services import user_service, subject_service, enrollment_service, grade_service

def command_help(user):
    for i in commands.keys():
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

        command = input()
        if command and command not in commands:
            if command == "exit":
                break

            if command == 'login': 
                current_user = login()
                if current_user:
                    display_user_menu(current_user)

                continue

            print("Invalid command!")

        else:
            commands[command](current_user)

def run_cli():
    handle_user_input()

# List of commands available to all users
commands = {"help":command_help, "add subject":add_subject}