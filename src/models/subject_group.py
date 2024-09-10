class SubjectGroup:
    def __init__(self, subject_code, teacher_id, subject_group, maximum_capacity, semester, capacity):
        self.subject_code = subject_code
        self.teacher_id = teacher_id
        self.subject_group = subject_group
        self.maximum_capacity = maximum_capacity
        self.semester = semester
        self.capacity = capacity

    def __repr__(self) -> str:
        return f'Group: {self.subject_group}.  Subject: {self.subject_code}.  Semester: {self.semester}.  Available Seats: {self.maximum_capacity-self.capacity}'
