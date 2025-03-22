import sqlite3

conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

# EXAMPLE: match_id = 2 (vs Brighton), player_id values should match your 'players' table

player_stats = [
    # Format: (match_id, player_id, minutes, goals, assists, xg, pass_pct, tackles, rating)
    (2, 1, 90, 0, 0, 0.01, 87.5, 1, 6.9),  # Onana
    (2, 4, 90, 0, 0, 0.02, 84.2, 2, 7.1),  # De Ligt
    (2, 5, 90, 0, 0, 0.03, 81.3, 3, 7.4),  # Yoro
    (2, 10, 85, 0, 1, 0.12, 89.0, 1, 7.6), # Shaw
    (2, 11, 90, 0, 0, 0.05, 83.3, 2, 7.0), # Dalot
    (2, 13, 90, 0, 1, 0.23, 91.2, 2, 8.0), # Bruno
    (2, 14, 70, 0, 0, 0.06, 84.1, 1, 6.8), # Mount
    (2, 17, 90, 0, 0, 0.09, 93.1, 3, 7.9), # Mainoo
    (2, 20, 75, 1, 0, 0.55, 76.4, 0, 8.2), # Højlund
    (2, 23, 80, 0, 0, 0.20, 82.5, 1, 7.2), # Garnacho
    (2, 22, 65, 0, 0, 0.18, 85.0, 0, 7.0), # Sancho
    # Add more if subs played
]

cursor.executemany('''
    INSERT INTO player_stats (
        match_id, player_id, minutes, goals, assists, xg, pass_pct, tackles, rating
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', player_stats)

conn.commit()
conn.close()

print("✅ Player stats added for match_id = 2")
