import requests

def get_api_key(api_key):
    try: 
        response = requests.get(
            "https://api.tucrm.com/leads",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=10   #  max time to wait for a response (in seconds)
        )
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Return the JSON response if successful
 
    except requests.exceptions.Timeout as http_err:
        
        print(f"Request timed out: {http_err}")
        return None
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Response: {response.text}")
        return None
    
    except requests.exceptions.ConnectionError as err:
        print(f"Connection error occurred: {err}")
        return None