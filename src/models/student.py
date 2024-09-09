from .user import User


class Student(User):
    def __init__(self, id, name, password, enrollment_date):
        super().__init__(id, name, password, "student")
        self.enrollment_date = enrollment_date
