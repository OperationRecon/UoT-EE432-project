from database import get_connection
from utils.helpers import hash_password, verify_password
from models.student import Student
from models.teacher import Teacher
from models.admin import Admin


def add_user(user_data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        hashed_password = hash_password(user_data['password'])
        cursor.execute('''
            INSERT INTO users (name, password_hash, user_type)
            VALUES (?, ?, ?)
        ''', (user_data['name'], hashed_password, user_data['user_type']))
        user_id = cursor.lastrowid
        conn.commit()
        return user_id
    finally:
        conn.close()


def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user_data = cursor.fetchone()
        if user_data:
            if user_data[3] == 'student':
                return Student(user_data[0], user_data[1], user_data[2], None)  # Add enrollment_date
            elif user_data[3] == 'teacher':
                return Teacher(user_data[0], user_data[1], user_data[2], None)  # Add cert
            elif user_data[3] == 'admin':
                return Admin(user_data[0], user_data[1], user_data[2])
        return None
    finally:
        conn.close()


def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM users WHERE name = ?', (username,))
        user_data = cursor.fetchone()
        if user_data and verify_password(user_data[2], password):
            return get_user(user_data[0])
        return None
    finally:
        conn.close()


def update_user(user_id, user_data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if 'password' in user_data:
            user_data['password_hash'] = hash_password(user_data.pop('password'))

        update_fields = ', '.join([f"{k} = ?" for k in user_data.keys()])
        query = f"UPDATE users SET {update_fields} WHERE id = ?"

        cursor.execute(query, list(user_data.values()) + [user_id])
        conn.commit()
    finally:
        conn.close()


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
    finally:
        conn.close()