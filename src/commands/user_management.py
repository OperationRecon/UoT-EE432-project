from services import user_service
import utils.helpers
from models.student import Student
from models.teacher import Teacher
from models.admin import Admin
import utils.validation
import random
from utils.validation import *



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
    user_type = validate_user_type()
    if not user_type:
        return
    if user_type == "student":
        enrollment_date = input("Enter user's enrollment_date (year): ")
    else:
        enrollment_date = None
    while True:
        has_id = input("Does the user have an ID?,if (N) A number will be generated automatically (Y/N)")
        if has_id in ["Y","N"]:
            break
    existing_ids = [str(i[0]) for i in user_service.get_specific_users(enrollment_date, user_type)]
    while has_id == "Y":
        id = input("Enter user's ID: ")
        if not Check_ID_standers(id,user_type):
            while True:
                has_id = input("Do you want to enter a different ID? (Y/N):")
                if has_id in ["Y", "N","exit"]:
                    break
            continue
        if id in existing_ids:
            print("The entry ID you provided is already in use. Enter exit to 'exit'.")
            while True:
                has_id = input("Do you want to enter a different ID? (Y/N):")
                if has_id in ["Y", "N", "exit"]:
                    break
            continue

        break
    if has_id == "exit":
        return
    if has_id == "N":
        id = create_id_user(enrollment_date, user_type)


    try:
        user_id = user_service.add_user([name,id,user_type,id,enrollment_date])
        print(f"The {user_type} added successfully, user's id : {user_id}")
    except Exception as e:
        print(f"Error adding {user_type}: {e}")


def create_id_user(enrollment_date, user_type):
    if user_type == "admin":
        ids = [i[0] for i in user_service.get_specific_users(None,user_type)]
        ids.sort()
        if ids[-1] == len(ids):
            return str(ids[-1] + 1)
        if 1 not in ids:
            return "1"
        for i in range(0,len(ids)-1):
            if ids[i+1] - ids[i] > 1:
                return str(ids[i] + 1)
        return str(ids[-1] + 1)

    if user_type == "student":
        year_str = str(enrollment_date)
        first_part = year_str[0] + year_str[2:]
        second_part = '020'
    else:
            first_part = '120'
            second_part = str(random.randint(0, 99999)).zfill(5)
    existing_ids = [i[0] for i in user_service.get_specific_users(enrollment_date,user_type)]
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
    user_type = validate_user_type()
    if not user_type:
        return
    user_id = input("Enter the user ID to delete: ")
    user_id = validate_user_data(user_id,user_type)
    if not user_id:
        return

    selected_user = user_service.get_user(user_id)
    if not selected_user:
        print(f"User with id: {user_id} doesn't exist")
        return
    if isinstance(selected_user,Admin):
        num_users = len(user_service.get_specific_users(None, 'admin'))
        if num_users <= 1:
            print("Cannot delete the last admin.")
            return False
    try:
        user_service.delete_user(user_id)
        print(f"The user {selected_user.name} with ID {user_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting user: {e}")


def update_user(user):
    if not utils.helpers.verify_role(type(user), [Admin]):
        return
    user_id = input("Enter the user ID to update: ")
    user_id = validate_student_data(user_id)
    if not user_id:
        return
    updated_user = user_service.get_user(user_id)
    if user_id == 1 and updated_user.id !=1:
        print("Only Admin 1 user can update its own")
        return
    print("Leave field empty if you don't want to update it.")
    password = input("Enter new Password: ")
    name = input(f"Enter new name ({updated_user.name}): ") or updated_user.name
    if updated_user.user_type == "student":
        enrollment_date = input(f"Enter new enrollment date ({updated_user.enrollment_date}): ") or updated_user.enrollment_date
    else:
        enrollment_date = None
    try:
        user_service.update_user(user_id, {"name": name, "enrollment_date": enrollment_date, "user_type": updated_user.user_type , "password": password})
        print(f"User with ID {user_id} updated successfully.")
    except Exception as e:
        print(f"Error updating user: {e}")


def update_password(user):
    user = user_service.get_user(user.id)
    while True:
        current_password = input("Enter your current password: ")
        if current_password == "exit":
            return
        if not user or not user_service.authenticate_user(user.id, current_password):
            print("Current password is incorrect. Try again or exit with 'exit'.")
            continue
        break
    print("When updating your password, please ensure it meets the following criteria:\n"
            "Contains at least one uppercase letter.\n"
            "Contains at least one lowercase letter.\n"
            "Includes at least one digit.\n"
            "Is between 8 and 20 characters in length.")
    new_password = input("Enter new password: ")
    while not is_strong_password(new_password):
        print("Password is not strong enough. Please try again, or type 'exit' to cancel")
        new_password = input("Enter new password: ")
        if new_password == "exit":
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
    while True:
        user_id = input("Enter the user ID to get: ")
        if user_id == "exit":
            return
        current_user = user_service.get_user(user_id)
        if not current_user:
            print(f"User with id: {user_id} doesn't exist")
            print("Enter another user ID or exit with 'exit': ")
            continue
        break
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

