import sqlite3
from sys_env import *
from utils.helpers import hash_password

def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   password_hash BLOB NOT NULL,
                   user_type TEXT NOT NULL,
                   enrollment_date INTEGER)''')
    
    p_hash = hash_password(FIRST_ADMIN["password"])

    cursor.execute('''INSERT OR IGNORE INTO users (id ,name, password_hash, user_type)
                   Values (?, ?, ? ,"admin") ''', (1,FIRST_ADMIN['name'],p_hash))
    
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                subject_code TEXT NOT NULL,
                student_id INTEGER NOT NULL,
                semester TEXT,
                yearwork REAL,
                final REAL,
                subject_group TEXT)''')
    
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

    conn.commit()
    conn.close()
