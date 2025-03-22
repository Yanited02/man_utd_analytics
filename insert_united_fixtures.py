import sqlite3

# Connect to the database
conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

# Sample fixture data
matches = [
    ("2024-08-10", "Manchester City", "Home", "W", 2, 1, 1.8, 1.5, "4-2-3-1"),
    ("2024-08-16", "Fulham", "Home", "W", 1, 0, 2.1, 0.8, "4-2-3-1"),
    ("2024-08-24", "Brighton & Hove Albion", "Away", "L", 1, 2, 1.5, 1.7, "4-3-3"),
    ("2024-09-01", "Liverpool", "Home", "L", 0, 3, 1.2, 2.5, "4-2-3-1"),
    ("2024-09-14", "Southampton", "Away", "W", 3, 0, 2.0, 0.9, "4-2-3-1"),
    ("2024-09-21", "Crystal Palace", "Away", "D", 0, 0, 1.0, 0.8, "4-3-3"),
    ("2024-09-29", "Tottenham Hotspur", "Home", "L", 0, 3, 1.1, 2.0, "4-2-3-1"),
    ("2024-10-06", "Aston Villa", "Away", "D", 0, 0, 0.9, 0.9, "4-3-3"),
    ("2024-10-19", "Brentford", "Home", "W", 2, 1, 1.8, 1.0, "4-2-3-1"),
    ("2024-10-27", "West Ham United", "Away", "L", 1, 2, 1.3, 1.6, "4-3-3"),
    ("2024-11-03", "Chelsea", "Home", "D", 1, 1, 1.4, 1.4, "4-2-3-1"),
    ("2024-11-10", "Leicester City", "Home", "W", 3, 0, 2.2, 0.7, "4-2-3-1"),
    ("2024-11-24", "Ipswich Town", "Away", "D", 1, 1, 1.3, 1.1, "4-3-3"),
    ("2024-12-01", "Everton", "Home", "W", 4, 0, 2.5, 0.6, "4-2-3-1"),
    ("2024-12-04", "Arsenal", "Away", "L", 0, 2, 1.0, 2.0, "4-3-3"),
    ("2024-12-07", "Nottingham Forest", "Home", "L", 2, 3, 1.9, 2.1, "4-2-3-1"),
    ("2024-12-15", "Manchester City", "Away", "W", 2, 1, 1.6, 1.8, "4-3-3"),
    ("2024-12-22", "AFC Bournemouth", "Home", "L", 0, 3, 1.2, 1.5, "4-2-3-1"),
    ("2024-12-26", "Wolverhampton Wanderers", "Away", "L", 0, 2, 1.0, 1.3, "4-3-3"),
    ("2024-12-30", "Newcastle United", "Home", "L", 0, 2, 1.1, 1.4, "4-2-3-1"),
    ("2025-01-05", "Liverpool", "Away", "D", 2, 2, 1.8, 2.0, "4-3-3"),
    ("2025-01-16", "Southampton", "Home", "W", 3, 1, 2.3, 1.1, "4-2-3-1"),
    ("2025-01-19", "Brighton & Hove Albion", "Home", "L", 1, 3, 1.4, 2.2, "4-2-3-1"),
    ("2025-01-26", "Fulham", "Away", "W", 1, 0, 1.7, 0.9, "4-3-3"),
    ("2025-02-02", "Crystal Palace", "Home", "L", 0, 2, 1.2, 1.5, "4-2-3-1"),
    ("2025-02-16", "Tottenham Hotspur", "Away", "L", 0, 1, 1.0, 1.2, "4-3-3"),
    

# Insert into the matches table
cursor.executemany('''
    INSERT INTO matches (date, opponent, venue, result, goals_for, goals_against, xg_for, xg_against, tactic_used)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', matches)

conn.commit()
conn.close()

print("📅 5 sample fixtures inserted successfully!")
