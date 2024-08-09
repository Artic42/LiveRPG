import requests
import time

# Define the API endpoint URL
url = "http://example.com/api/about"

# Loop until the API responds with "OK"
while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Server is online!")
            break
        else:
            print(f"Received status code {response.status_code}. Retrying...")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}. Retrying...")

    # Wait for a few seconds before retrying
    time.sleep(5)
