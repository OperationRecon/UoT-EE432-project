import bcrypt


def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def verify_password(stored_hash, provided_password):
    # Check if the provided password matches the stored hash
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hash)


def verify_role(user_role, allowed_roles):
    # verfifies if the user has access levels equal to or higher than the allowed role
    if user_role not in allowed_roles:
        print("Unauthorised Command!")
        return False
    
    return True


def check_prereq(student_id, subject_id):
    pass


def check_coreq(student_id, subject_id):
    pass
