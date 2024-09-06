from database import get_connection

def enroll(student_id, subject_id):
    conn = get_connection()
    # Implementation for enrolling a student in a subject
    conn.close()

def drop_out(student_id, subject_id):
    conn = get_connection()
    # Implementation for dropping a student from a subject
    conn.close()

def check_prereq(student_id, subject_id):
    conn = get_connection()
    # Implementation for checking prerequisites
    conn.close()

def check_coreq(student_id, subject_id):
    conn = get_connection()
    # Implementation for checking corequisites
    conn.close()

def force_enroll(student_id, subject_id):
    conn = get_connection()
    # Implementation for force enrolling a student
    conn.close()