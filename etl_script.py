import json

# 1. Extract (Simulated Data)
data = {"id": 1, "name": "Test User", "role": "Data Engineer"}

# 2. Transform (Modify Data)
data['role'] = data['role'].upper()

# 3. Load (Save to file)
with open('processed_data.json', 'w') as f:
    json.dump(data, f)

print("ETL Job Completed Successfully")