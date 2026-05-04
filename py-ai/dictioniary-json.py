import json

# Convert a dictionary to a JSON string
lead = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "score": 85
}   

lead_json = json.dumps(lead, indent=2)  
print(lead_json)

# Convert a JSON string back to a dictionary
api_response = '{ "status": "success", "data": { "id": 123, "name": "John Doe" } }'

api_dict = json.loads(api_response)
print(api_dict)

# Save a dictionary to a JSON file

proccessed_leads = [
    {"name": "John Doe", "email": "john.doe@example.com", "score": 85},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "score": 92}
]

with open('processed_leads.json', 'w', encoding='utf-8') as file:
    json.dump(proccessed_leads, file, indent=2, ensure_ascii=False)
    
print("Save processed leads to processed_leads.json")

# Read a dictionary from a JSON file

with open('processed_leads.json', 'r', encoding='utf-8') as file:
    loaded_leads = json.load(file)
    
print(f"Leads loaded from file: {len(loaded_leads)}")

for lead in loaded_leads:
    print(f"Lead Name: {lead['name']}, Email: {lead['email']}, Score: {lead['score']}")

