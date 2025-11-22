import requests
import json
import os
from datetime import datetime

# 1. EXTRACT
# Define the Source URL (Open-Meteo API)
# Coordinates for New York City (Lat: 40.71, Long: -74.01)
URL = "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current_weather=true"

try:
    response = requests.get(URL)
    response.raise_for_status()
    raw_data = response.json()
    
    # 2. TRANSFORM
    # Dig into the dictionary to find the data we want
    current_weather = raw_data["current_weather"]
    temp_celsius = current_weather["temperature"]
    windspeed = current_weather["windspeed"]
    
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    
    # Create our clean row
    clean_data = {
        "timestamp_iso": datetime.now().isoformat(),
        "city": "New York",
        "temp_c": temp_celsius,
        "temp_f": round(temp_fahrenheit, 2), # Round to 2 decimal places
        "wind_speed_kmh": windspeed,
        "is_windy": windspeed > 15 # Boolean logic flag
    }
    
    print(f"Current Weather in NY: {temp_celsius}°C ({clean_data['temp_f']}°F)")

    # 3. LOAD
    # Save to 'weather_history.json'
    file_path = "weather_history.json"
    
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            history = json.load(f)
    else:
        history = []
        
    history.append(clean_data)
    
    with open(file_path, "w") as f:
        json.dump(history, f, indent=4)
        
    print(f"Data saved to {file_path}")

except Exception as e:
    print(f"Error: {e}")