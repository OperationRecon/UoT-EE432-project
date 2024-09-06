from services import user_service, subject_service, enrollment_service, grade_service

def display_main_menu():
    print("\nUniversity Administration System")
    print("1. Login")
    print("2. Exit")

def display_user_menu(user):
    print(f"\nWelcome, {user.name}")
    if user.user_type == 'admin':
        print("1. User Management")
        print("2. Subject Management")
    elif user.user_type == 'teacher':
        print("1. Grade Management")
    elif user.user_type == 'student':
        print("1. View Grades")
        print("2. Enroll in Subject")
    print("3. Logout")

def handle_user_input():
    current_user = None
    while True:
        if current_user is None:
            display_main_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                current_user = user_service.authenticate_user(username, password)
                if current_user is None:
                    print("Invalid credentials. Please try again.")
            elif choice == '2':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            display_user_menu(current_user)
            choice = input("Enter your choice: ")
            if choice == '3':
                current_user = None
                print("Logged out successfully.")
            else:
                # Handle other menu options based on user type
                pass

def run_cli():
    handle_user_input()