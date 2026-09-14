import sqlite3

def setup_database():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS history (name TEXT, score INTEGER)")
    conn.commit()
    return conn