from database import get_connection
from models.subject import Subject


def add_subject(subject_data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO subjects (code, title, preq, coreq, description, cr, faculty, dept, branch) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", subject_data)
    conn.commit()
    conn.close()


def get_subject(subject_code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects WHERE code = ?", (subject_code,))
    subject_data = cursor.fetchone()
    conn.close()
    if subject_data:
        return Subject(*subject_data)
    return None


def update_subject(subject_code, subject_data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        update_fields = ', '.join([f"{k} = ?" for k in subject_data.keys()])
        query = f"UPDATE subjects SET {update_fields} WHERE code = ?"
        cursor.execute(query, list(subject_data.values()) + [subject_code])
        conn.commit()
        
    finally:
        conn.close()


def delete_subject(subject_code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subjects WHERE code = ?", (subject_code,))
    conn.commit()
    conn.close()


def get_all_subjects():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM subjects")
        subjects = cursor.fetchall()
        return [Subject(*subject[:]) for subject in subjects]
    finally:
        conn.close()


def assign_teacher_to_subject_group(subject_code, teacher_id, subject_group, semester):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE subject_groups
            SET teacher_id = ?
            WHERE subject_code = ? AND subject_group = ? AND semester = ?
        ''', (teacher_id, subject_code, subject_group, semester))
        conn.commit()
    finally:
        conn.close()