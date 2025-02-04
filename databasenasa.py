import requests

# Replace your API key below
API_KEY = "8HALnlv0Gc2ZyMFDLQmwYKFlTieI3pWmS3RmUDRv"

# Mars Rover API endpoint (example endpoint for Perseverance rover images)
url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/photos?sol=1000&api_key={API_KEY}"

# Function to get data
def get_mars_rover_data():
    try:
        # Send GET request to the endpoint
        response = requests.get(url)
        
        # Check if the response was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            photos = data.get('photos', [])
            
            if photos:
                print(f"Total photos found: {len(photos)}")
                for photo in photos[:5]:  # Display the first 5 photos
                    print(f"Photo URL: {photo['img_src']}")
                    print(f"Sol: {photo['sol']}")
                    print(f"Date: {photo['earth_date']}")
                    print("-" * 30)
            else:
                print("No photos found for the specified sol.")
        else:
            print("Request error. Status code:", response.status_code)
    
    except Exception as e:
        print(f"An error occurred: {e}")

