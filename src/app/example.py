import requests

# Endpoint URL - adjust the host and port as needed
url = 'http://0.0.0.0:8000/opt'

# Example payload matching the OptRequestModel structure
payload = {
    'number_of_fields': 5,
    'number_of_seasons': 2,
    'crops': [
        {'name': 'CORN', 'crop_yield': 100, 'nutrient_impact': -2},
        {'name': 'SOYBEAN', 'crop_yield': 80, 'nutrient_impact': -1},
    ],
    'initial_nutrients': 10,
    'min_nutrients': 3,
    'max_nutrients': 20
}

# Make the POST request
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 200:
    print("Success! Here's the response data:")
    print(response.text)
else:
    print(f"Failed to get a successful response, status code: {response.status_code}")
    print("Response text:", response.text)
