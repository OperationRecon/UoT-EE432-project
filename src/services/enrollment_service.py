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
