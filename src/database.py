import sqlite3

from models.admin import Admin
from utils.helpers import hash_password

DATABASE_NAME = r'..\data\university.db'


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   password_hash BLOB NOT NULL,
                   user_type TEXT NOT NULL)''')
    
    admin = Admin(1,'admin', 'admin')
    p_hash = hash_password(admin.password)

    cursor.execute('''INSERT OR REPLACE INTO users (id ,name, password_hash, user_type)
                   Values (?, ?, ? ,"admin") ''', (admin.id,admin.name,p_hash))
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                subject_code TEXT NOT NULL,
                subject_title TEXT,
                student_id INTEGER NOT NULL,
                student_name TEXT,
                semester TEXT,
                yearwork REAL,
                final REAL)''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS subjects (
                code TEXT,
                title TEXT,
                preq BLOB,
                coreq BLOB,
                cr INTEGER,
                faculty TEXT,
                dept TEXT,
                branch TEXT,
                description TEXT)''')

    conn.commit()
    conn.close()
