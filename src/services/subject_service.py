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


def get_available_subjects(student_id):
    # return [[sg for sg in get_all_subject_groups(s.subject_code) if int(sg.capacity) < int(sg.maximum_capacity) and utils.helpers.check_prereq(student_id, s.code) and utils.helpers.check_coreq(student_id, s.code)] for s in subjects]
    pass
