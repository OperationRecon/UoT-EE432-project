class Subject:
    def __init__(self, code, title, preq, coreq, description, cr, faculty, dept, branch, capacity, maximum_capacity):
        self.id = None
        self.code = code
        self.title = title
        self.preq = preq
        self.coreq = coreq
        self.description = description
        self.cr = cr
        self.faculty = faculty
        self.dept = dept
        self.branch = branch
        self.capacity = capacity
        self.maximum_capacity = maximum_capacity

    def __str__(self):
        return f"Code: {self.code}, Title: {self.title}, Credits: {str(self.cr)}"

    def __repr__(self):
        return self.__str__()

    def add_teacher(self, teacher):
        # Implementation for adding a teacher
        pass

    def remove_teacher(self, teacher):
        # Implementation for removing a teacher
        pass


