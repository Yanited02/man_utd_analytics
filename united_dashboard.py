import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os
import subprocess


# --- Page Config ---
st.set_page_config(page_title="Man Utd Analytics", layout="wide")

# --- Refresh Data Button ---
if st.button("🔄 Refresh Match Data"):
    with st.spinner("Fetching latest data from FotMob..."):
        result = subprocess.run(["python", "data_loader.py"], capture_output=True, text=True)
        st.success("✅ Data refreshed!")
        st.code(result.stdout)


# --- Styling ---
st.markdown(
    """
    <style>
    /* Background image */
    .stApp {
        background: url("https://upload.wikimedia.org/wikipedia/commons/5/59/Old_Trafford_inside_20060726_1.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Dark overlay */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.65);
        z-index: 0;
    }

    /* Content container */
    .block-container {
        z-index: 1;
        position: relative;
        padding-top: 2rem;
    }

    /* Headings */
    h1, h2, h3, .stMarkdown {
        color: white;
    }

    /* Table transparency */
    .stDataFrame {
        background-color: rgba(255,255,255,0.9);
        border-radius: 10px;
    }

    /* Logo image alignment */
    .logo-container {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .logo-text {
        font-size: 2rem;
        font-weight: bold;
        color: white;
        margin: 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Connect to DB ---
conn = sqlite3.connect("united_analytics.db")

@st.cache_data
def load_match_data():
    query = """
    SELECT date, opponent, venue, result, goals_for, goals_against, xg_for, xg_against
    FROM matches
    ORDER BY date
    """
    df = pd.read_sql_query(query, conn)
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_match_data()  # Runs initially
if 'Refresh Match Data' in st.session_state:
    df = load_match_data()  # Reload after refresh

# --- Header with Logo ---
st.markdown(
    """
    <div class="logo-container">
        <img src="https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg" width="70">
        <p class="logo-text">Manchester United Analytics Dashboard</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### Tracking every match performance, result, and expected goals.")

# --- Filters ---
venue_filter = st.selectbox("📍 Filter by venue:", ["All", "Home", "Away"])
opponents = ["All"] + sorted(df["opponent"].unique().tolist())
opponent_filter = st.selectbox("⚔️ Filter by opponent:", opponents)

filtered_df = df.copy()
if venue_filter != "All":
    filtered_df = filtered_df[filtered_df["venue"] == venue_filter]
if opponent_filter != "All":
    filtered_df = filtered_df[filtered_df["opponent"] == opponent_filter]

# --- Match Table ---
st.subheader("📋 Match Results")
st.dataframe(filtered_df, use_container_width=True)

# --- Chart: Goals vs xG ---
st.subheader("📊 Goals vs Expected Goals (xG)")

# Apply safe modern style
plt.style.use("ggplot")
fig, ax = plt.subplots()
fig.set_facecolor("none")
ax.set_facecolor("none")

# Plot lines
ax.plot(filtered_df["date"], filtered_df["goals_for"], label="Goals For", marker="o")
ax.plot(filtered_df["date"], filtered_df["xg_for"], label="xG For", marker="x")
ax.plot(filtered_df["date"], filtered_df["goals_against"], label="Goals Against", marker="o")
ax.plot(filtered_df["date"], filtered_df["xg_against"], label="xG Against", marker="x")

ax.set_xlabel("Date")
ax.set_ylabel("Goals / xG")
ax.set_title("Match Trend")
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

# --- Footer ---
st.markdown("---")
st.markdown("<center>Made with ❤️ at Old Trafford. Glory Glory Man United.</center>", unsafe_allow_html=True)
