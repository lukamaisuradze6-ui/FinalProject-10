import sqlite3
import bcrypt

DB_NAME = "student_portal.db"


def create_users_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_last TEXT NOT NULL,
            personal_number TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def register_user(first_last, personal_number, password):
    password_hash = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

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
    row = cursor.fetchone()
    conn.close()

    if not row:
        return False

    return bcrypt.checkpw(password.encode(), row[0].encode())
