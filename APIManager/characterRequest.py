import requests
import json

# Post Requests

def createCharacter(ID):
    url = f"http://localhost:8000/character/create/{ID}"

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)
    
    return response

# Delete Requests

def deleteCharacter(ID):
    url = f"http://localhost:8000/character/delete/{ID}"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)
    
    return response

# Put Requests

def editName(ID, name):
    url = f"http://localhost:8000/character/editName/{ID}"

    payload = json.dumps({"name": name})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    
    return response

def editPlayer(ID, player):
    url = f"http://localhost:8000/character/editPlayer/{ID}"

    payload = json.dumps({"player": player})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    
    return response

def editCharacteristics(ID, strength, medicine, hacking):
    url = f"http://localhost:8000/character/editCharacteristics/{ID}"

    payload = json.dumps({"strength": strength,
               "medicine": medicine,
               "hacking": hacking})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    
    return response

def editBackground(ID, background):
    url = f"http://localhost:8000/character/editBackground/{ID}"

    payload = json.dumps({"background": background})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    
    return response

def editMainObjective(ID, mainObjective):
    url = f"http://localhost:8000/character/editMainObjective/{ID}"

    payload = json.dumps({"mainObjective": mainObjective})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    
    return response

def editSecondaryObjective(ID, secondaryObjective):
    url = f"http://localhost:8000/character/editSecondaryObjective/{ID}"

    payload = json.dumps({"secondaryObjective": secondaryObjective})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    
    return response

def editLoseCondition(ID, loseCondition):
    url = f"http://localhost:8000/character/editLoseCondition/{ID}"

    payload = json.dumps({"loseCondition": loseCondition})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    
    return response

def editFullCharacter(ID, name, player, strength, medicine, hacking, background, mainObjective, secondaryObjective, loseCondition):
    url = f"http://localhost:8000/character/edit/{ID}"

    payload = json.dumps({"name": name,
               "player": player,
               "strength": strength,
               "medicine": medicine,
               "hacking": hacking,
               "background": background,
               "mainObjective": mainObjective,
               "secondaryObjective": secondaryObjective,
               "loseCondition": loseCondition})
    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload)
    
    return response

# Get Requests

def getCharacters():
    url = "http://localhost:8000/characters"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def readName (ID):
    url = f"http://localhost:8000/character/{ID}/name"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def readPlayer (ID):
    url = f"http://localhost:8000/character/{ID}/player"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def readStrength (ID):
    url = f"http://localhost:8000/character/{ID}/strength"
    
    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def readMedicine (ID):
    url = f"http://localhost:8000/character/{ID}/medicine"
    
    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def readHacking (ID):
    url = f"http://localhost:8000/character/{ID}/hacking"
    
    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def readBackground (ID):
    url = f"http://localhost:8000/character/{ID}/background"
    
    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def readMainObjective (ID):
    url = f"http://localhost:8000/character/{ID}/mainObjective"
    
    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def readSecondaryObjective (ID):
    url = f"http://localhost:8000/character/{ID}/secondaryObjective"
    
    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def readLoseCondition (ID):
    url = f"http://localhost:8000/character/{ID}/loseCondition"
    
    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response

def getFullCharacter (ID):
    url = f"http://localhost:8000/character/{ID}"
    
    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response