import sqlite3

# Connect to the existing database
conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

# Sample player data
players = [
    ("Bruno Fernandes", "CAM", 29, "Portugal", "Right"),
    ("Marcus Rashford", "LW", 26, "England", "Right"),
    ("Alejandro Garnacho", "RW", 19, "Argentina", "Right"),
    ("Scott McTominay", "CM", 27, "Scotland", "Right"),
    ("Rasmus Højlund", "ST", 21, "Denmark", "Left")
]

# Insert data into the table
cursor.executemany('''
    INSERT INTO players (name, position, age, nationality, preferred_foot)
    VALUES (?, ?, ?, ?, ?)
''', players)

# Commit changes and close
conn.commit()
conn.close()

print("Players added successfully!")
