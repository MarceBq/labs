import requests

headers = {
    "Authorization": "Bearer YOUR_API_KEY_HERE",
    "Content-Type": "application/json"
}

new_lead = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "company": "Example Inc.",
    "origin": "Website",
    "score": 85
}

response = requests.post(
    "https://api.tucrm.com/contactos",
    headers=headers,
    json=new_lead   #request body in JSON format
)

if response.status_code == 201:
    contact = response.json()
    print("Lead created successfully!")
    print(f"Lead ID: {contact['id']}")
else:
    print(f"Failed to create lead. Status code: {response.status_code}: {response.text}")