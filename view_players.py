import sqlite3

conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM players")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
