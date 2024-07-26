import requests

# Post Requests


def activateTestMode():
    url = "http://localhost:8000/activateTestMode"

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


def deactivateTestMode():
    url = "http://localhost:8000/deactivateTestMode"

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


def checkConnection():
    url = "http://localhost:8000/about"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        return True
    else:
        return False
