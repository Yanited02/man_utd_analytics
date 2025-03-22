import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

# Create the players table
cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT,
    age INTEGER,
    nationality TEXT,
    preferred_foot TEXT
)
''')

# Save changes and close the connection
conn.commit()
conn.close()

print("Database and 'players' table created successfully!")
