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


    def __str__(self):
        return f"Code: {self.code}. Title: {self.title}. Credits: {str(self.cr)}. Prequesites: {self.preq}.  Corequesites: {self.coreq}.  Faculty: {self.faculty}.  Department: {self.dept}.  Branch: {self.branch}.  Description: {self.description}"

    def __repr__(self):
        return self.__str__()
