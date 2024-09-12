class Grade:
    def __init__(self, subject_code, student_id, semester, yearwork, final, group):
        self.subject_code = subject_code
        self.student_id = student_id
        self.semester = semester
        self.yearwork = yearwork
        self.final = final
        self.subject_group = group

    def __str__(self) -> str:
        return f'Subject: {self.subject_code}.  Group: {self.subject_group}.  Semester: {self.semester}.  Yearwork: {str(self.yearwork)}.  Final: {str(self.final)}.  Total: {str(self.yearwork)+str(self.final)}.'

    def __repr__(self):
        return self.__str__()
