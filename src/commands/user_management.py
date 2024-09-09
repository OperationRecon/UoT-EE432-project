from services import user_service
import utils.helpers
from models.student import Student
from models.teacher import Teacher
from models.admin import Admin
import random



def login():
    ID = input("Enter your ID: ")
    password = input("Enter Password: ")

    user = user_service.authenticate_user(ID, password)

    if not user:
        print("Invalid Name or Password")
    else:
        print('Logged in sccuessfully!')
    
    return user

def add_user(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    name = input("Enter user's name: ")
    user_type = input("Enter user's type (student or teacher or admin) : ")
    if user_type not in ["student","admin","teacher"]:
        print(f"Error adding user: user type is not define")
        return
    if user_type == "student":
        enrollment_date = input("Enter user's enrollment_date (year) : ")
    else:
        enrollment_date = None
    id = create_id_user(enrollment_date, user_type)
    try:
        user_id = user_service.add_user([name,id,user_type,id,enrollment_date])
        print(f"The {user_type} added successfully, user's id : {user_id}")
    except Exception as e:
        print(f"Error adding {user_type}: {e}")


def create_id_user(enrollment_date, user_type):
    if user_type == "student":
        year_str = str(enrollment_date)
        first_part = year_str[0] + year_str[2:]
        second_part = '020'
    else:
            first_part = '120'
            second_part = str(random.randint(0, 99999)).zfill(5)
    existing_ids = user_service.get_specific_users(enrollment_date,user_type)
    if not existing_ids:
        existing_ids = [-1]
    third_part = str(random.randint(0, 9999)).zfill(4)
    user_id = first_part + second_part + third_part
    while True:
        if user_id not in existing_ids and len(set(third_part))>1:
            break
        else:
            third_part = str((int(third_part) + 1) % 10000).zfill(4)
            user_id = first_part + second_part + third_part
            if user_id not in existing_ids and len(set(third_part))>1:
                break

    return user_id


def delete_user(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    user_id = input("Enter the user ID to delete: ")
    selected_user = user_service.get_user(user_id)
    if utils.helpers.verify_role(type(selected_user), [Admin]):
        num_users = len(user_service.get_specific_users(None,'admin'))
        if num_users <= 1:
            print("Cannot delete the last admin.")
            return False
    try:
        deleted_user = user_service.delete_user(user_id)
        if deleted_user:
            print(f"The user {deleted_user.name} with ID {user_id} deleted successfully.")
        else:
            print(f"{user_id} id not exist")
    except Exception as e:
        print(f"Error deleting user: {e}")


def update_user(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    user_id = input("Enter the user ID to update: ")
    updated_user = user_service.get_user(user_id)
    if not updated_user:
        print("User not found!")
        return
    if user_id == 1 and updated_user.id !=1:
        print("Only Admin 1 user can update its own")
        return
    print("Leave field empty if you don't want to update it.")
    password = input("Enter new Password: ")
    name = input(f"Enter new name ({updated_user.name}): ") or updated_user.name
    user_type = input(f"Enter new user type (student, teacher, admin) ({updated_user.user_type}): ") or updated_user.user_type
    if user_type not in ["student", "admin", "teacher",""]:
        print(f"Error updating user: Invalid user type")
        return
    if updated_user.user_type == "student":
        enrollment_date = input(f"Enter new enrollment date ({updated_user.enrollment_date}): ") or updated_user.enrollment_date
    else:
        enrollment_date = None
    try:
        user_service.update_user(user_id, {"name": name, "enrollment_date": enrollment_date, "user_type": user_type , "password": password})
        print(f"User with ID {user_id} updated successfully.")
    except Exception as e:
        print(f"Error updating user: {e}")


def update_password(user):
    current_password = input("Enter your current password: ")
    user = user_service.get_user(user.id)
    if not user or not user_service.authenticate_user(user.id, current_password):
        print("Current password is incorrect.")
        return
    print("When updating your password, please ensure it meets the following criteria:\n"
            "Contains at least one uppercase letter.\n"
            "Contains at least one lowercase letter.\n"
            "Includes at least one digit.\n"
            "Is between 8 and 20 characters in length.")
    new_password = input("Enter new password: ")
    while not is_strong_password(new_password):
        print("Password is not strong enough. Please try again, or type 'back' to cancel")
        new_password = input("Enter new password: ")
        if new_password == "back":
            return
    try:
        user_service.update_user(user.id, {'password': new_password})
        print(f"Password for user ID {user.id} updated successfully.")
    except Exception as e:
        print(f"Error updating password: {e}")


def is_strong_password(password):
    if (len(password) >= 8 and len(password) <= 20 and
        (any(char.islower() for char in password)) and
        (any(char.isupper() for char in password)) and
        (any(char.isdigit() for char in password))):
        return True
    return False


def get_user(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    id = input("Enter the user ID to get: ")
    current_user = user_service.get_user(id)
    print(f"name : {current_user.name}")
    print(f"id : {current_user.id}")
    print(f"user type : {current_user.user_type}")


def get_all_users(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    try:
        users = user_service.get_all_users()
        for user in users:
            print(f"Name: {user.name}, ID: {user.id}, Type: {user.user_type}")
    except Exception as e:
        print(f"Error fetching users: {e}")
