import requests
import json

# Function to fetch space facts from NASA API
def fetch_space_facts():
    # URL of NASA API for the Curiosity rover (Mars)
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    # Request parameters
    params = {
        "sol": 1000,  # Sol is the Martian day number, for example, 1000.
        "camera": "FHAZ",  # Choose a camera from the rover, like "FHAZ"
        "api_key": "8HALnlv0Gc2ZyMFDLQmwYKFlTieI3pWmS3RmUDRv"  # Replace with your NASA API key
    }
    
    # Making the GET request
    response = requests.get(url, params=params)
    
    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()  # Converts the response to JSON
        return data
    else:
        print(f"Request error. Code: {response.status_code}")
        return None

# Function to store data in a JSON file
def store_data_in_json(data, file_name="space_facts.json"):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data stored in the file {file_name}")

# Main function to fetch and store data
def space_research_agent():
    data = fetch_space_facts()
    if data:
        store_data_in_json(data)

# Calling the function
space_research_agent()

