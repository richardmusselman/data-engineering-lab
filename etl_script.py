import json
import os
from dotenv import load_dotenv

# 1. Load the secrets from the .env file
load_dotenv()

# 2. Extract: Get configuration (Simulating a database connection)
db_user = os.getenv("DATABASE_USER")
# Note: We don't print the password for security reasons!
print(f"Connecting to database as user: {db_user}...")

data = {"id": 1, "name": "Test User", "role": "Data Engineer"}

# 3. Transform
data['role'] = data['role'].upper()

# 4. Load
with open('processed_data.json', 'w') as f:
    json.dump(data, f)

print("ETL Job Completed Successfully")