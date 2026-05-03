import requests

# Get = 'give me information'
api_response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

print(api_response.status_code)  # Should print 200 if the request was successful

data = api_response.json()

print(data)  # Print the entire response data

# Extracting specific information
print(data['rates']['EUR'])  # Print the exchange rate for EUR