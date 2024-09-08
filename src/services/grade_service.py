from database import get_connection
from models.grade import Grade

def add_grade(grade_data):
    # Implementation for retrieving a grade from the database
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO grades (subject_code, student_id, semester, yearwork, final) 
                       VALUES (?, ?, ?, ?, ?)''', grade_data)
        conn.commit()
        
    finally:
        conn.close()

def get_grade(student_id, subject_code, semester):
    # Implementation for retrieving a grade from the database
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
                         SELECT * FROM grades WHERE
                         subject_code = ? AND student_id = ? AND semester = ? 
                         ''',
                        (subject_code, student_id, semester)
                         )
        data = cursor.fetchone()
        if data:
            return Grade(data[0],data[1],data[2],data[3],data[4])
    

    finally:
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