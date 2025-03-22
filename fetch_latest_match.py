import sqlite3
import pandas as pd
from soccerdata import FotMob

# Constants
TEAM_NAME = "Manchester United"
LEAGUE_NAME = "ENG-Premier League"
SEASON = "2023/2024"  # Adjust if 2024/2025 is not supported yet

# Connect to the database
conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

# FotMob instance
fotmob = FotMob(leagues=LEAGUE_NAME, seasons=SEASON)

def match_exists(date, opponent):
    cursor.execute("SELECT 1 FROM matches WHERE date = ? AND opponent = ?", (date, opponent))
    return cursor.fetchone() is not None

def insert_match(match_data):
    cursor.execute('''
        INSERT INTO matches (date, opponent, venue, result, goals_for, goals_against, xg_for, xg_against, tactic_used)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', match_data)
    conn.commit()
    return cursor.lastrowid

def display_match_row(match_dict):
    df = pd.DataFrame([match_dict])
    print(df.to_string(index=False))

def loop_and_store_matches():
    print("🔁 Fetching all Manchester United matches from FotMob...")
    schedule = fotmob.read_schedule()
    team_matches = schedule[
        ((schedule['home_team'] == TEAM_NAME) | (schedule['away_team'] == TEAM_NAME)) &
        (schedule['status'] == 'FT')
    ]

    print(f"📅 Found {len(team_matches)} played matches.")

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
        match_id = match['game_id']

        if match_exists(date, opponent):
            print(f"⏩ Skipping {date} vs {opponent} (already in DB)")
            continue

        match_data = (date, opponent, venue, result, goals_for, goals_against, xg_for, xg_against, tactic_used)
        match_db_id = insert_match(match_data)

        print(f"✅ Stored match: {date} vs {opponent}")
        display_match_row({
            "Date": date,
            "Opponent": opponent,
            "Venue": venue,
            "Result": result,
            "Goals For": goals_for,
            "Goals Against": goals_against
        })

    print("\n🎉 All matches processed and stored!\n")

if __name__ == "__main__":
    loop_and_store_matches()
