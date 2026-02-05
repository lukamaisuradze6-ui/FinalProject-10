import sqlite3
import bcrypt
import os

DB_NAME = "student_portal.db"

def create_users_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            first_last TEXT NOT NULL,
            personal_number TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_courses_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS courses (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT UNIQUE NOT NULL,
            course_name TEXT NOT NULL,
            credits INTEGER NOT NULL    
        )
    """)
    conn.commit()
    conn.close()

def create_enrollments_table():
    # Fixed typo: connnect -> connect
    conn = sqlite3.connect(DB_NAME) 
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS enrollments(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           user_id INTEGER NOT NULL,
           course_id INTEGER NOT NULL,
           UNIQUE(user_id, course_id),
           FOREIGN KEY (user_id) REFERENCES users(id),
           FOREIGN KEY (course_id) REFERENCES courses(Id)                   
        )
    """)
    conn.commit()
    conn.close()

def register_user(first_last, personal_number, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (first_last, personal_number, password_hash) VALUES (?, ?, ?)",
            (first_last, personal_number, password_hash)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(personal_number, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash FROM users WHERE personal_number = ?",
        (personal_number,)
    )
    result = cursor.fetchone()
    conn.close()
    if not result:
        return False
    return bcrypt.checkpw(password.encode(), result[0].encode())

def enroll_course(personal_number, course_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Fixed: added comma to (personal_number,)
    cursor.execute(
        "SELECT id FROM users WHERE personal_number = ?",
        (personal_number,)
    )
    user = cursor.fetchone()
    if not user:
        conn.close()
        return False
    user_id = user[0]
    try:
        cursor.execute(
            "INSERT INTO enrollments (user_id, course_id) VALUES (?, ?)",
            (user_id, course_id)
        )
        conn.commit()
        return True 
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()