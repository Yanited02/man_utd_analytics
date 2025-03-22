import sqlite3

# Connect to the database
conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

# Get all matches
cursor.execute("SELECT * FROM matches")
matches = cursor.fetchall()

# Print them
for match in matches:
    print(match)

conn.close()
