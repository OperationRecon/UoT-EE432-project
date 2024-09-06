from utils.helpers import verify_password, hash_password


class User:
    def __init__(self, id, name, password_hash, user_type):
        self.id = id
        self.name = name
        self.password = password_hash
        self.user_type = user_type

    def authenticate(self, password):
        return verify_password(self.password_hash, password)

    def change_password(self, new_password):
        self.password_hash = hash_password(new_password)
