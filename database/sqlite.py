import sqlite3

try:
    with sqlite3.connect("db.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            user_id INTEGER UNIQUE,
            is_admin BOOLEAN,
            is_blocked BOOLEAN
        )
        """)
        conn.commit()
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
