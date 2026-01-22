import sqlite3
import bcrypt

DB_NAME = "student_portal.db"

def create_users_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def register_user(email, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (email, password_hash) VALUES (?, ?)",
            (email, password_hash)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash FROM users WHERE email = ?",
        (email,)
    )
    result = cursor.fetchone()
    conn.close()

    if not result:
        return False

    return bcrypt.checkpw(password.encode(), result[0].encode())
