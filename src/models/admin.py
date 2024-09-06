from .user import User

class Admin(User):
    def __init__(self, id, name, password):
        super().__init__(id, name, password, "admin")

    def add_user(self, user_data):
        # Implementation for adding a new user
        pass

    def remove_user(self, user_id):
        # Implementation for removing a user
        pass
    