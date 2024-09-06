class Subject:
    def __init__(self, code, title, preq, coreq, description, cr, faculty, dept, branch):
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

    def add_teacher(self, teacher):
        # Implementation for adding a teacher
        pass

    def remove_teacher(self, teacher):
        # Implementation for removing a teacher
        pass


