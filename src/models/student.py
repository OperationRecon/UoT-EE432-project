from .user import User

class Student(User):
    def __init__(self, id, name, password, enrollment_date):
        super().__init__(id, name, password, "student")
        self.enrollment_date = enrollment_date

    def enroll(self, subject):
        # Implementation for enrolling in a subject
        pass

    def drop_out(self, subject):
        # Implementation for dropping out of a subject
        pass

    def get_grades(self):
        # Implementation for retrieving grades
        pass