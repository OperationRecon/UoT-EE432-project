from database import get_connection
from models.grade import Grade
from commands.grade_management import update_capacity


def add_grade(grade_data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO grades (subject_code, student_id, semester, yearwork, final, subject_group) 
                       VALUES (?, ?, ?, ?, ?, ?)''', grade_data)
        conn.commit()
        update_capacity(grade_data[0], grade_data[1], grade_data[2], 1, grade_data[5])
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


def delete_grade(subject_code, student_id, semester):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        group = get_grade(student_id, subject_code, semester).subject_group
        cursor.execute('''
            DELETE FROM grades
            WHERE subject_code = ? AND student_id = ? AND semester = ?
        ''', (subject_code, student_id, semester,))
        conn.commit()
        update_capacity(subject_code, student_id, semester, -1, group)
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


def get_semester_grades(student_id, semester):
    # Fetches the frades of the student in the given semseter
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
