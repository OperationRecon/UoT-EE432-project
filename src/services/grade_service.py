from database import get_connection

def add_grade(grade_data):
    conn = get_connection()
    # Implementation for adding a grade to the database
    conn.close()

def get_grade(student_id, subject_id):
    conn = get_connection()
    # Implementation for retrieving a grade from the database
    conn.close()

def update_grade(grade_id, grade_data):
    conn = get_connection()
    # Implementation for updating a grade in the database
    conn.close()

def delete_grade(grade_id):
    conn = get_connection()
    # Implementation for deleting a grade from the database
    conn.close()

def get_subject_grades(subject_id):
    conn = get_connection()
    # Implementation for retrieving all grades for a subject
    conn.close()

def get_student_grades(student_id):
    conn = get_connection()
    # Implementation for retrieving all grades for a student
    conn.close()