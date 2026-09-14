import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM players")
results = cursor.fetchall()

print(results)

conn.commit()
conn.close()