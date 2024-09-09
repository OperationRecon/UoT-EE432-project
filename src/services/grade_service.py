from database import get_connection
from models.grade import Grade


def add_grade(grade_data):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO grades (subject_code, student_id, semester, yearwork, final, subject_group) 
                       VALUES (?, ?, ?, ?, ?, ?)''', grade_data)
        conn.commit()

    finally:
        conn.close()


def get_grade(student_id, subject_code, semester):
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
            return Grade(*data)

    finally:
        conn.close()


def update_grade(grade_identifiers, grade_data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        update_fields = ', '.join([f"{k} = ?" for k in grade_data.keys()])
        query = f"UPDATE grades SET {update_fields} WHERE subject_code = ? AND student_id = ? AND semester = ?"
        cursor.execute(query, tuple(grade_data.values()) + grade_identifiers)
        conn.commit()

    finally:
        conn.close()


def delete_grade(subject_code, student_id, semester, subject_group):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            DELETE FROM grades
            WHERE subject_code = ? AND student_id = ? AND semester = ? AND subject_group = ?
        ''', (subject_code, student_id, semester, subject_group))
        conn.commit()
    finally:
        conn.close()


def get_subject_grades(subject_code, semester, subject_group):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT * FROM grades
            WHERE subject_code = ? AND semester = ? AND subject_group = ?
        ''', (subject_code, semester, subject_group))
        grades = cursor.fetchall()
        return [Grade(*grade) for grade in grades]
    finally:
        conn.close()


def get_student_grades(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT * FROM grades
            WHERE student_id = ?
            AND yearwork IS NOT NULL
            AND final IS NOT NULL
        ''', (student_id,))
        grades = cursor.fetchall()
        return [Grade(*grade) for grade in grades]
    finally:
        conn.close()


def get_semester(student_id, semester):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
                SELECT * FROM grades
                WHERE student_id = ? And semester = ?
            ''', (student_id, semester))
        grades = cursor.fetchall()
        return [Grade(*grade) for grade in grades]
    finally:
        conn.close()
