import sqlite3

class Database:
    def __init__(self, db_name="game.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                progress INTEGER DEFAULT 1  -- Tracks the last unlocked level
            )
        """)
        self.conn.commit()

    def add_user(self, username):
        try:
            self.cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass  # User already exists

    def get_progress(self, username):
        self.cursor.execute("SELECT progress FROM users WHERE username=?", (username,))
        result = self.cursor.fetchone()
        return result[0] if result else 1

    def update_progress(self, username, level):
        self.cursor.execute("UPDATE users SET progress=? WHERE username=?", (level, username))
        self.conn.commit()
