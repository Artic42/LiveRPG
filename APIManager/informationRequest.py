import requests
import json


# POST request
def createInformation(ID):
    url = f"http://localhost:8000/information/create/{ID}"

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# DELETE request
def deleteInformation(ID):
    url = f"http://localhost:8000/information/delete/{ID}"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response


# PUT request
def editKnownCharacter(ID, knownCharacter):
    url = f"http://localhost:8000/information/editKnown/{ID}"

    payload = json.dumps({"knownCharacter": knownCharacter})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response


def editAboutCharacter(ID, aboutCharacter):
    url = f"http://localhost:8000/information/editAbout/{ID}"

    payload = json.dumps({"aboutCharacter": aboutCharacter})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response


def editDescription(ID, description):
    url = f"http://localhost:8000/information/editDescription/{ID}"

    payload = json.dumps({"description": description})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response


def editFullInformation(ID, knownCharacter, aboutCharacter, description):
    url = f"http://localhost:8000/information/editFull/{ID}"

    payload = json.dumps({"knownCharacter": knownCharacter,
                          "aboutCharacter": aboutCharacter,
                          "description": description})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response


# GET requests
def readKnownCharacter(ID):
    url = f"http://localhost:8000/information/readKnown/{ID}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def readAboutCharacter(ID):
    url = f"http://localhost:8000/information/readAbout/{ID}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def readDescription(ID):
    url = f"http://localhost:8000/information/readDescription/{ID}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def readFullInformation(ID):
    url = f"http://localhost:8000/information/readFull/{ID}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response
