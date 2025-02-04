import requests
import json

# Replace with your personal API key
api_key = '8HALnlv0Gc2ZyMFDLQmwYKFlTieI3pWmS3RmUDRv'  # Use your key obtained from the NASA portal

# Define the start and end dates
start_date = '2023-02-01'
end_date = '2023-02-02'

# API URL with query parameters
url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'

# Make the GET request
response = requests.get(url)

# If the request is successful
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))  # Display the data formatted in JSON
else:
    print(f"Error making the request: {response.status_code}")
