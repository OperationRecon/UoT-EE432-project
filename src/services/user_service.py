from database import get_connection
from utils.helpers import hash_password, verify_password
from models.student import Student
from models.teacher import Teacher
from models.admin import Admin


def add_user(user_data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        hashed_password = hash_password(user_data[1])
        user_data[1] = hashed_password
        cursor.execute('''
            INSERT INTO users (name, password_hash, user_type,id,enrollment_date)
            VALUES (?, ?, ?, ?, ?)
        ''', user_data)
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
                return Student(user_data[0], user_data[1], user_data[2], user_data[4])
            elif user_data[3] == 'teacher':
                return Teacher(user_data[0], user_data[1], user_data[2], None)  # Add cert
            elif user_data[3] == 'admin':
                return Admin(user_data[0], user_data[1], user_data[2])
        return None
    finally:
        conn.close()


def authenticate_user(ID, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM users WHERE id = ?', (ID,))
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
        if not user_data["password"]:
            user_data.pop("password")
        if "password" in user_data.keys():
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
        deleted_user = get_user(user_id)
        if not deleted_user:
            return None
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        return deleted_user
    finally:
        conn.close()

def get_specific_users(enrollment_date,users_type):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if enrollment_date:
            cursor.execute('SELECT id FROM users WHERE enrollment_date = ? AND  user_type = ?', (enrollment_date,users_type))
        else:
            cursor.execute('SELECT id FROM users WHERE enrollment_date IS NULL AND  user_type = ?', (users_type,))
        ids = cursor.fetchall()
    finally:
        conn.close()
    return ids

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM users')
        users_data = cursor.fetchall()
        users = []
        for user_data in users_data:
            if user_data[3] == 'student':
                user = Student(user_data[0], user_data[1], user_data[2], None)  # Add enrollment_date
            elif user_data[3] == 'teacher':
                user = Teacher(user_data[0], user_data[1], user_data[2], None)  # Add cert
            elif user_data[3] == 'admin':
                user = Admin(user_data[0], user_data[1], user_data[2])
            users.append(user)
        return users
    finally:
        conn.close()
