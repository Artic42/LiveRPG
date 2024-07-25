import requests
import json

# Post Requests

def activateTestMode():
    url = f"http://localhost:8000/activateTestMode"

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)
    
    return response

def deactivateTestMode():
    url = f"http://localhost:8000/deactivateTestMode"

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)