import sqlite3
import pandas as pd
from soccerdata import FotMob

TEAM_NAME = "Manchester United"
LEAGUE_NAME = "ENG-Premier League"
SEASON = "2023/2024"  # Change to current if supported

def connect_db():
    return sqlite3.connect("united_analytics.db")

def match_exists(cursor, date, opponent):
    cursor.execute("SELECT 1 FROM matches WHERE date = ? AND opponent = ?", (date, opponent))
    return cursor.fetchone() is not None

def insert_match(cursor, match_data):
    cursor.execute('''
        INSERT INTO matches (date, opponent, venue, result, goals_for, goals_against, xg_for, xg_against, tactic_used)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', match_data)


def fetch_and_store_all_matches():
    conn = connect_db()
    cursor = conn.cursor()

    fotmob = FotMob(leagues=LEAGUE_NAME, seasons=SEASON)
    schedule = fotmob.read_schedule()
    
    team_matches = schedule[
        ((schedule['home_team'] == TEAM_NAME) | (schedule['away_team'] == TEAM_NAME)) &
        (schedule['status'] == 'FT')
    ]

    print(f"📅 Found {len(team_matches)} played matches for {TEAM_NAME}.")

    for i, match in team_matches.iterrows():
        date = pd.to_datetime(match['date']).strftime("%Y-%m-%d")
        opponent = match['away_team'] if match['home_team'] == TEAM_NAME else match['home_team']
        venue = "Home" if match['home_team'] == TEAM_NAME else "Away"
        result = f"{match['home_score']} - {match['away_score']}"
        goals_for = match['home_score'] if venue == "Home" else match['away_score']
        goals_against = match['away_score'] if venue == "Home" else match['home_score']
        xg_for = match.get('home_xg', 0.0) if venue == "Home" else match.get('away_xg', 0.0)
        xg_against = match.get('away_xg', 0.0) if venue == "Home" else match.get('home_xg', 0.0)
        tactic_used = None

        if match_exists(cursor, date, opponent):
            print(f"⏩ Skipping {date} vs {opponent} (already in DB)")
            continue

        match_data = (date, opponent, venue, result, goals_for, goals_against, xg_for, xg_against, tactic_used)
        insert_match(cursor, match_data)
        print(f"✅ Stored match: {date} vs {opponent}")

    conn.commit()
    conn.close()
    print("\n🎉 All matches stored and database updated!")

if __name__ == "__main__":
    fetch_and_store_all_matches()