from database import get_connection


def check_prereq(student_id, subject_code):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT subject_code FROM subjects
                    WHERE (subject_code IN 
                    (SELECT subject_code
                    FROM grades WHERE yearwork + final >= 50 AND student_id = {student_id}))''')

    finally:
        cursor.close


def check_coreq(student_id, subject_code):
    pass


def set_current_semester(current_semester):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE current_semester SET semester = ?", (current_semester,))
        conn.commit()

    finally:
        conn.close()


def get_current_semester():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM current_semester")
        return cursor.fetchone()[0]
    finally:
        conn.close()
