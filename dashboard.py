import streamlit as st
import sqlite3
import pandas as pd
import os
import time

# --- CONFIGURATION ---
# Set the page title and icon
st.set_page_config(page_title="NYC Weather Monitor", page_icon="🌤️")

# Get the absolute path to the DB (same logic as before)
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "weather.db")

# --- TITLE ---
st.title("🌤️ Real-Time Weather Pipeline")
st.markdown(f"**Database Location:** `{db_path}`")

# --- DATA LOADING FUNCTION ---
def load_data():
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Use Pandas to read the SQL table directly into a DataFrame
    # This is the bridge between "Engineering" (SQL) and "Math" (Pandas)
    df = pd.read_sql("SELECT * FROM weather_logs ORDER BY timestamp DESC", conn)
    
    conn.close()
    return df

# --- AUTO-REFRESH LOGIC ---
# Create a placeholder container that we can wipe and update
placeholder = st.empty()

# Run a loop to simulate a live dashboard
# (In production, Streamlit handles this differently, but this is great for a demo)
while True:
    with placeholder.container():
        # 1. Load the latest data
        df = load_data()

        # 2. Key Metrics (The "Headlines")
        if not df.empty:
            latest_temp = df.iloc[0]["temp_f"]
            latest_wind = df.iloc[0]["wind_speed"]
            last_updated = df.iloc[0]["timestamp"]

            col1, col2, col3 = st.columns(3)
            col1.metric("Temperature", f"{latest_temp} °F")
            col2.metric("Wind Speed", f"{latest_wind} km/h")
            col3.metric("Last Update", last_updated.split("T")[1][:8]) # clean time format

            # 3. Visualization (The "Math")
            st.subheader("Temperature Trend (Last 50 Readings)")
            # We reverse the order for the chart so time goes Left -> Right
            chart_data = df.head(50).sort_values("id")
            st.line_chart(chart_data, x="timestamp", y="temp_f")

            # 4. Raw Data (The "Evidence")
            st.subheader("Raw Database Records")
            st.dataframe(df)
            
        else:
            st.warning("No data found in the database yet!")

    # Wait for 2 seconds before refreshing (to save CPU)
    time.sleep(2)