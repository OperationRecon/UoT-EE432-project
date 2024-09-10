from database import get_connection


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

def check_coreq_to_drop_out(student_id,subject_code):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
                       SELECT subject_code FROM grades
                       WHERE (yearwork IS NULL OR final IS NULL)
                       AND student_id = ?
                       ''',(student_id,))
        student_subject = [i[0] for i in cursor.fetchall()]
        coreq = []
        for i in student_subject:
            cursor.execute('SELECT coreq FROM subjects WHERE code = ?',(i,))
            coreqs = cursor.fetchone()[0].split(" ")
            for j in coreqs:
                coreq.append(j)

        if subject_code in coreq:
            return True
        return None

    finally:
        conn.close()

def get_current_units(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
                SELECT subject_code FROM grades 
                WHERE student_id = ? AND 
                (yearwork  IS NULL OR final IS NULL) 
                ''', (student_id,))
        subject = [i[0] for i in cursor.fetchall()]
        units = 0
        for i in subject:
            cursor.execute('SELECT cr FROM subjects WHERE code = ? ', (i,))
            units += int(cursor.fetchone()[0])
        return units
    finally:
        conn.close()
