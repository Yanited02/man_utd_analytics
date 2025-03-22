import sqlite3

# Connect to your database
conn = sqlite3.connect("united_analytics.db")
cursor = conn.cursor()

# Format: (name, position, age, nationality, preferred_foot)
players = [
    # --- FIRST TEAM ---
    ("André Onana", "GK", 28, "Cameroon", "Right"),
    ("Altay Bayındır", "GK", 26, "Turkey", "Right"),
    ("Tom Heaton", "GK", 38, "England", "Right"),

    ("Matthijs de Ligt", "CB", 25, "Netherlands", "Right"),
    ("Leny Yoro", "CB", 19, "France", "Right"),
    ("Lisandro Martínez", "CB", 26, "Argentina", "Left"),
    ("Victor Lindelöf", "CB", 30, "Sweden", "Right"),
    ("Jonny Evans", "CB", 37, "Northern Ireland", "Right"),

    ("Patrick Dorgu", "LB", 20, "Denmark", "Left"),
    ("Luke Shaw", "LB", 29, "England", "Left"),
    ("Diogo Dalot", "RB", 25, "Portugal", "Right"),
    ("Noussair Mazraoui", "RB", 27, "Morocco", "Right"),

    ("Bruno Fernandes", "CAM", 29, "Portugal", "Right"),
    ("Mason Mount", "CM", 26, "England", "Right"),
    ("Manuel Ugarte", "CDM", 24, "Uruguay", "Right"),
    ("Casemiro", "CDM", 33, "Brazil", "Right"),
    ("Kobbie Mainoo", "CM", 19, "England", "Right"),
    ("Christian Eriksen", "CM", 33, "Denmark", "Right"),
    ("Toby Collyer", "CDM", 20, "England", "Right"),

    ("Rasmus Højlund", "ST", 21, "Denmark", "Left"),
    ("Joshua Zirkzee", "ST", 23, "Netherlands", "Right"),
    ("Jadon Sancho", "RW", 24, "England", "Right"),
    ("Alejandro Garnacho", "LW", 20, "Argentina", "Right"),
    ("Amad Diallo", "RW", 22, "Ivory Coast", "Left"),

    # --- U21 SQUAD ---
    ("Radek Vitek", "GK", 20, "Czech Republic", "Right"),
    ("Bjørn Hardley", "CB", 21, "Netherlands", "Left"),
    ("Teden Mengi", "CB", 21, "England", "Right"),
    ("Marc Jurado", "RB", 20, "Spain", "Right"),
    ("Sam Murray", "LB", 20, "England", "Left"),

    ("Dan Gore", "CM", 19, "England", "Right"),
    ("Isak Hansen-Aarøen", "CM", 19, "Norway", "Right"),
    ("Omari Forson", "CAM", 19, "England", "Right"),
    ("Shola Shoretire", "CAM", 20, "England", "Right"),

    ("Joe Hugill", "ST", 20, "England", "Left"),
    ("Noam Emeran", "RW", 21, "France", "Right"),
]

# Insert all the players
cursor.executemany('''
    INSERT INTO players (name, position, age, nationality, preferred_foot)
    VALUES (?, ?, ?, ?, ?)
''', players)

conn.commit()
conn.close()

print("🔥 All current Manchester United players (First Team + U21) inserted successfully!")
