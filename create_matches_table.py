import sqlite3

conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    opponent TEXT,
    venue TEXT,
    result TEXT,
    goals_for INTEGER,
    goals_against INTEGER,
    xg_for REAL,
    xg_against REAL,
    tactic_used TEXT
)
''')

conn.commit()
conn.close()

print("✅ 'matches' table created successfully!")
