import requests

# The base URL of the API endpoint
url = "https://groupsor.link/api_endpoint"  # Replace with the actual API endpoint.

# Headers (if required by the API)
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # Replace with your token if needed.
    "Content-Type": "application/json"  # Adjust content type if needed.
}

# Payload (adjust based on API requirements)
payload = {
    "key1": "value1",
    "key2": "value2"
}

# Sending the request
try:
    response = requests.post(url, json=payload, headers=headers)  # Or requests.get() if it's a GET request
    response.raise_for_status()  # Check if the request was successful
    data = response.json()  # Assuming the response is in JSON format
    print("Response Data:", data)
except requests.exceptions.RequestException as e:
    print("Error:", e)
  
