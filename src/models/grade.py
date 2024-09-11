class Grade:
    def __init__(self, subject_code, student_id, semester, yearwork, final, group):
        self.subject_code = subject_code
        self.student_id = student_id
        self.semester = semester
        self.yearwork = yearwork
        self.final = final
        self.subject_group = group

    def __str__(self) -> str:
        if not self.yearwork: # Error None when display
            self.yearwork = ""
        if not self.final:
            self.final = ""
        return f'Subject: {self.subject_code}.  Group: {self.subject_group}.  Semester: {self.semester}.  Yearwork: {self.yearwork}.  Final: {self.final}.  Total: {self.yearwork+self.final}'

    def __repr__(self):
        return self.__str__()
