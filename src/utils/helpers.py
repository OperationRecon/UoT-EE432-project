import bcrypt


def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def verify_password(stored_hash, provided_password):
    # Check if the provided password matches the stored hash
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_hash)
