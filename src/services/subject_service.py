from database import get_connection


def add_subject(subject_data):
    conn = get_connection()
    # Implementation for adding a subject to the database
    conn.close()


def get_subject(subject_id):
    conn = get_connection()
    # Implementation for retrieving a subject from the database
    conn.close()


def update_subject(subject_id, subject_data):
    conn = get_connection()
    # Implementation for updating a subject in the database
    conn.close()


def delete_subject(subject_id):
    conn = get_connection()
    # Implementation for deleting a subject from the database
    conn.close()


def assign_teacher(subject_id, teacher_id):
    conn = get_connection()
    # Implementation for assigning a teacher to a subject
    conn.close()