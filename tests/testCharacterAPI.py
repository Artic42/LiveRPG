from articlib.testEngine import test
import APIManager.characterRequest as characterRequest
import APIManager.request as request
import requests


def runTest():
    print("Starting character API test")    
    runScenario1()
    runScenario2()
    runScenario3()
    print("Character API test finished")


def runScenario1():
    test.newScenario("Read all characters and create a new character")
    test11()
    test12()
    test13()
    test.endScenario("Read all characters and create a new character")
    
def runScenario2():
    test.newScenario("Write and read each parameter one by one")
    test21()
    test22()
    test23()
    test24()
    test25()
    test26()
    test27()
    test.endScenario("Write and read each parameter one by one")
    
def runScenario3():
    test.newScenario("Write and Read all character in one go")
    test31()
    test32()
    test.endScenario("Write and Read all character in one go")
    
def test11():
    response = characterRequest.getCharacters()
    characters= response.json()
    test.testIfEqual(characters["1"], "Name1", "Characters request character name")
    test.testIfEqual(characters["2"], "Name2", "Characters request character name")
    
def test12():
    response = characterRequest.createCharacter(20)
    test.testIfEqual(response.json()["status"], 200, "Create character status")
    
def test13():
    characters = characterRequest.deleteCharacter(20)
    test.testIfEqual(characters.json()["status"], 200, "Delete character status")
    
def test21():
    print ("Test 21")
    response = characterRequest.editName(1, "NewName1")
    print(response)
    print(response.json())
    test.testIfEqual(response.json()["status"], 200, "Edit name status")
    name = characterRequest.readName(1)
    test.testIfEqual(name.json()["name"], "NewName1", "Read name")  
    
def test22():
    response = characterRequest.editPlayer(1, "NewPlayer1")
    test.testIfEqual(response.json()["status"], 200, "Edit player status")
    player = characterRequest.readPlayer(1)
    test.testIfEqual(player.json()["player"], "NewPlayer1", "Read player")
    
def test23():
    response = characterRequest.editCharacteristics(1, 1, 2, 3)
    test.testIfEqual(response.json()["status"], 200, "Edit characteristics status")
    strength = characterRequest.readStrength(1)
    test.testIfEqual(strength.json()["strength"], 1, "Read strength")
    medicine = characterRequest.readMedicine(1)
    test.testIfEqual(medicine.json()["medicine"], 2, "Read medicine")
    hacking = characterRequest.readHacking(1)
    test.testIfEqual(hacking.json()["hacking"], 3, "Read hacking")
    
def test24():
    response = characterRequest.editBackground(1, "NewBackground1")
    test.testIfEqual(response.json()["status"], 200, "Edit background status")
    background = characterRequest.readBackground(1)
    test.testIfEqual(background.json()["background"], "NewBackground1", "Read background")
    
def test25():
    response = characterRequest.editMainObjective(1, "NewMainObjective1")
    test.testIfEqual(response.json()["status"], 200, "Edit main objective status")
    mainObjective = characterRequest.readMainObjective(1)
    test.testIfEqual(mainObjective.json()["mainObjective"], "NewMainObjective1", "Read main objective")
    
def test26():
    response = characterRequest.editSecondaryObjective(1, "NewSecondaryObjective1")
    test.testIfEqual(response.json()["status"], 200, "Edit secondary objective status")
    secondaryObjective = characterRequest.readSecondaryObjective(1)
    test.testIfEqual(secondaryObjective.json()["secondaryObjective"], "NewSecondaryObjective1", "Read secondary objective")
    
def test27():
    response = characterRequest.editLoseCondition(1, "NewLoseCondition1")
    test.testIfEqual(response.json()["status"], 200, "Edit lose condition status")
    loseCondition = characterRequest.readLoseCondition(1)
    test.testIfEqual(loseCondition.json()["loseCondition"], "NewLoseCondition1", "Read lose condition")
    
def test31():
    response = characterRequest.editFullCharacter(2,
                                                  "NewName2",
                                                  "NewPlayer2",
                                                   2,
                                                   3,
                                                   4,
                                                   "NewBackground2",
                                                   "NewMainObjective2",
                                                   "NewSecondaryObjective2",
                                                   "NewLoseCondition2")
    test.testIfEqual(response.json()["status"], 200, "Edit character status")
    
def test32():
    character = characterRequest.getFullCharacter(2)
    test.testIfEqual(character.json()["Name"], "NewName2", "Read name")
    test.testIfEqual(character.json()["Player"], "NewPlayer2", "Read player")
    test.testIfEqual(character.json()["Strength"], 2, "Read strength")
    test.testIfEqual(character.json()["Medicine"], 3, "Read medicine")
    test.testIfEqual(character.json()["Hacking"], 4, "Read hacking")
    test.testIfEqual(character.json()["Background"], "NewBackground2", "Read background")
    test.testIfEqual(character.json()["MainObjective"], "NewMainObjective2", "Read main objective")
    test.testIfEqual(character.json()["SecondaryObjective"], "NewSecondaryObjective2", "Read secondary objective")
    test.testIfEqual(character.json()["LoseCondition"], "NewLoseCondition2", "Read lose condition")

if __name__ == "__main__":
    request.activateTestMode()
    runTest()
    test.printResults()
    request.deactivateTestMode()  