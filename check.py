import sqlite3

conn = sqlite3.connect('medicines.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM medicines")

data = cursor.fetchall()

print(data)

conn.close()