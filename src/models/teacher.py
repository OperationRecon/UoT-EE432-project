from .user import User

class Teacher(User):
    def __init__(self, id, name, password, cert):
        super().__init__(id, name, password, "teacher")
        self.cert = cert
