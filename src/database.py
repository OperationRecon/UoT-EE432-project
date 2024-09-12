import sqlite3
import json
from utils.helpers import hash_password


def get_connection():
    with open('src\sys_env.json', 'r') as file:
        data = json.load(file)

    return sqlite3.connect(data['database'])


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    with open('src\sys_env.json', 'r') as file:
        data = json.load(file)

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY NOT NULL,
                   name TEXT NOT NULL,
                   password_hash BLOB NOT NULL,
                   user_type TEXT NOT NULL,
                   enrollment_date INTEGER)''')
    
    p_hash = hash_password(data["password"])

    cursor.execute('''INSERT OR IGNORE INTO users (id ,name, password_hash, user_type)
                   Values (?, ?, ? ,"admin") ''', (1, 'admin' ,p_hash))
    
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                subject_code TEXT NOT NULL,
                student_id INTEGER NOT NULL,
                semester TEXT NOT NULL,
                yearwork REAL,
                final REAL,
                subject_group TEXT NOT NULL)''')
    
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS subjects (
                code TEXT NOT NULL,
                title TEXT NOT NULL,
                preq TEXT,
                coreq TEXT,
                description TEXT,
                cr INTEGER NOT NULL,
                faculty TEXT,
                dept TEXT,
                branch TEXT)''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS subject_groups (
                subject_code TEXT NOT NULL,
                teacher_id INTEGER,
                subject_group TEXT NOT NULL,
                maximum_capacity INTEGER,
                semester TEXT NOT NULL,
                capacity INTEGER NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS current_semester (semester TEXT PRIMARY KEY)''')
    cursor.execute('''INSERT INTO current_semester (semester) SELECT NULL WHERE NOT EXISTS (SELECT 1 FROM current_semester)''')

    conn.commit()
    conn.close()
