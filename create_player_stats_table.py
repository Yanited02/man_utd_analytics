import sqlite3

conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS player_stats (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    player_id INTEGER,
    minutes INTEGER,
    goals INTEGER,
    assists INTEGER,
    xg REAL,
    pass_pct REAL,
    tackles INTEGER,
    rating REAL,
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
)
''')

conn.commit()
conn.close()

print("✅ 'player_stats' table created successfully!")
