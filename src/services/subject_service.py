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
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Get passed subjects
        cursor.execute('''SELECT code FROM subjects
                    WHERE (code IN 
                    (SELECT subject_code
                    FROM grades WHERE (yearwork + final) >= 50 AND student_id = (?)))''', (int(student_id),))
        
        passed = [x[0] for x in cursor.fetchall()]
        

        # Get currently studied subjects
        cursor.execute('''SELECT subject_code FROM grades WHERE student_id = (?) AND semester IN (SELECT * FROM current_semester)''', (int(student_id),))
        current = [x[0] for x in cursor.fetchall()]


        # Get other subjects
        cursor.execute('''SELECT code, preq, coreq FROM subjects
                    WHERE (code NOT IN 
                    (SELECT subject_code
                    FROM grades WHERE student_id = ?))''', (int(student_id),))
        
        potential = cursor.fetchall()

        # Get subjects whose prequesites and corequisites are satisfied and have
        available_subjects = [subject[0] for subject in potential if all(item in passed for item in subject[1].split()) and all(item in current for item in subject[2].split())]

        return available_subjects

    finally:
        cursor.close

