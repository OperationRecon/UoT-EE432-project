from database import get_connection
from models.subject_group import SubjectGroup

def add_subject_group(subject_group_data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO subject_groups (subject_code, teacher_id, subject_group, maximum_capacity, semester, capacity)
            VALUES (?, ?, ?, ?, ?, ?)
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


def get_available_subject_groups(subject):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT * FROM subject_groups
            WHERE subject_code = ? AND semester IN (SELECT * FROM current_semester) AND maximum_capacity > capacity
        ''', (subject,))

        data = cursor.fetchall()
        return [SubjectGroup(*group) for group in data] if data else None

    finally:
        conn.close()


def get_subject_groups(subject, semester):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if semester == "*":
            cursor.execute('''
                    SELECT * FROM subject_groups
                    WHERE subject_code = ?''', (subject,))
        else:
            cursor.execute('''
                                SELECT * FROM subject_groups
                                WHERE subject_code = ? AND semester = ?''', (subject, semester,))

        data = cursor.fetchall()
        return [SubjectGroup(*group) for group in data] if data else None

    finally:
        conn.close()
    
