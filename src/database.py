import sqlite3

DATABASE_NAME = r'data\university.db'


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            user_type TEXT NOT NULL,
        )
    ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                subject_code TEXT NOT NULL,
                subject_title TEXT,
                student_id INTEGER NOT NULL,
                student_name TEXT,
                semester TEXT,
                yearwork REAL,
                final REAL
            )
        ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS subjects (
                code TEXT,
                title TEXT,
                preq BLOB,
                coreq BLOB,
                cr INTEGER,
                facualty TEXT,
                dept TEXT,
                branch TEXT,
                description TEXT                 
            )
        ''')

    conn.commit()
    conn.close()
