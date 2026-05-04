import requests

# using os library to load API key from environment variable
import os
API_KEY_ENV = os.getenv("API_KEY")

# Form 1: Using API key in headers
headers = {
    "Authorization": f"Bearer {API_KEY_ENV}",
    "Content-Type": "application/json"
}

response = requests.get("https://api.example.com/data", headers=headers)


# Form 2: Using API key as a query parameter
response2 = requests.get("https://api.example.com/data", params={"api_key": API_KEY_ENV})  

