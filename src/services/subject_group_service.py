from database import get_connection
from models.subject_group import SubjectGroup

def add_subject_group(subject_group_data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO subject_groups (subject_code, teacher_id, subject_group, maximum_capacity, semester)
            VALUES (?, ?, ?, ?, ?)
        ''', subject_group_data)
        conn.commit()
    finally:
        conn.close()

def get_subject_group(subject_code, subject_group, semester):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT * FROM subject_groups
            WHERE subject_code = ? AND subject_group = ? AND semester = ?
        ''', (subject_code, subject_group, semester))
        data = cursor.fetchone()
        if data:
            return SubjectGroup(*data)
    finally:
        conn.close()

def update_subject_group(subject_code, subject_group, semester, update_data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        update_fields = ', '.join([f"{k} = ?" for k in update_data.keys()])
        query = f"UPDATE subject_groups SET {update_fields} WHERE subject_code = ? AND subject_group = ? AND semester = ?"
        cursor.execute(query, list(update_data.values()) + [subject_code, subject_group, semester])
        conn.commit()
    finally:
        conn.close()

def delete_subject_group(subject_code, subject_group, semester):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            DELETE FROM subject_groups
            WHERE subject_code = ? AND subject_group = ? AND semester = ?
        ''', (subject_code, subject_group, semester))
        conn.commit()
    finally:
        conn.close()

def get_available_seats(subject_code, subject_group, semester): # revision
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT sg.maximum_capacity - COUNT(e.student_id) as available_seats
            FROM subject_groups sg
            LEFT JOIN enrollments e ON sg.subject_code = e.subject_code 
                AND sg.subject_group = e.subject_group 
                AND sg.semester = e.semester
            WHERE sg.subject_code = ? AND sg.subject_group = ? AND sg.semester = ?
            GROUP BY sg.subject_code, sg.subject_group, sg.semester
        ''', (subject_code, subject_group, semester))
        result = cursor.fetchone()
        return result[0] if result else 0
    finally:
        conn.close()
