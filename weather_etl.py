import requests
import sqlite3 # <--- New Library (Built-in)
import os
from datetime import datetime

# --- SETUP PATHS ---
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "weather.db") # Saving as a database file now
log_path = os.path.join(script_dir, "etl_log.txt")

# 1. EXTRACT
URL = "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current_weather=true"

try:
    response = requests.get(URL)
    response.raise_for_status()
    raw_data = response.json()
    
    # 2. TRANSFORM
    current_weather = raw_data["current_weather"]
    temp_c = current_weather["temperature"]
    windspeed = current_weather["windspeed"]
    temp_f = (temp_c * 9/5) + 32
    
    timestamp = datetime.now().isoformat()
    
    # 3. LOAD (SQL EDITION)
    # Connect to the database (it creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create Table (If not exists) - Ideally this is done once, but this is safe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            city TEXT,
            temp_c REAL,
            temp_f REAL,
            wind_speed REAL
        )
    """)
    
    # Insert Data
    cursor.execute("""
        INSERT INTO weather_logs (timestamp, city, temp_c, temp_f, wind_speed)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, "New York", temp_c, round(temp_f, 2), windspeed))
    
    # Commit (Save) and Close
    conn.commit()
    conn.close()
    
    # Log Success
    with open(log_path, "a") as f:
        f.write(f"{datetime.now()}: SUCCESS - Data saved to DB\n")

except Exception as e:
    with open(log_path, "a") as f:
        f.write(f"{datetime.now()}: ERROR - {e}\n")