class Grade:
    def __init__(self, subject_code, student_id, semester, yearwork, final):
        self.subject_code = subject_code
        self.student_id = student_id
        self.semester = semester
        self.yearwork = yearwork
        self.final = final

    def __str__(self) -> str:
        return f'Subject: {self.subject_code}\nSemester: {self.semester}\nYearwork: {self.yearwork}\nFinal: {self.final}\nTotal: {self.yearwork+self.final}'

    def __repr__(self):
        return self.__str__()
