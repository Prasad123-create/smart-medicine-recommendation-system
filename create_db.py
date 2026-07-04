import sqlite3

conn = sqlite3.connect('medicines.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS medicines(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    problem TEXT,
    medicine TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")