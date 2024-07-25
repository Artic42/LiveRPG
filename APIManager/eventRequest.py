import requests
import json

# POST requests


def createEvent(ID):
    url = f"http://localhost:8000/event/create/{ID}"

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response

# DELETE requests


def deleteEvent(ID):
    url = f"http://localhost:8000/event/delete/{ID}"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    return response


# PUT requests


def editEventDescription(ID, description):
    url = f"http://localhost:8000/event/editDescription/{ID}"

    payload = json.dumps({"description": description})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


def editEventFlags(ID, hack, equip, activate, wait):
    url = f"http://localhost:8000/event/editFlags/{ID}"

    payload = json.dumps({"hack": hack,
                          "equip": equip,
                          "activate": activate,
                          "wait": wait})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


def activateEvent(ID):
    url = f"http://localhost:8000/event/activate/{ID}"

    payload = {}
    headers = {}

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


def deactivateEvent(ID):
    url = f"http://localhost:8000/event/deactivate/{ID}"

    payload = {}
    headers = {}

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


def editRedirectEvent(ID, redirectID):
    url = f"http://localhost:8000/event/editRedirect/{ID}"

    payload = json.dumps({"redirectID": redirectID})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


def editFullEvent(ID, description, hack,
                  equip, activate, wait,
                  activated, redirectID):
    url = f"http://localhost:8000/event/editEvent/{ID}"

    payload = json.dumps({"description": description,
                          "hacking": hack,
                          "equip": equip,
                          "activate": activate,
                          "wait": wait,
                          "activated": activated,
                          "redirectID": redirectID})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response

# GET requests


def readEvent(ID):
    url = f"http://localhost:8000/event/read/{ID}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def readEventDescription(ID):
    url = f"http://localhost:8000/event/readDescription/{ID}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def readEventFlags(ID):
    url = f"http://localhost:8000/event/readFlags/{ID}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def readEventActivated(ID):
    url = f"http://localhost:8000/event/readActivated/{ID}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def readEventRedirect(ID):
    url = f"http://localhost:8000/event/readRedirect/{ID}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response
