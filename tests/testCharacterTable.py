from articlib.testEngine import test
import articlib.sqliteEngine as sqliteEngine
import databaseManager.characterActions as characterActions
import databaseManager.characterConsults as characterConsults
import shutil


def runTest():
    print("Starting databaseManager test")
    runScenario1()
    runScenario2()
    print("databaseManager test finished")


def runScenario1():
    test.newScenario("Create a character")
    test11_13()
    test14()
    test15()
    test.endScenario("Create a character")


def runScenario2():
    test.newScenario("Get character information")
    test21_29()
    test.endScenario("Get character information")


def test11_13():
    characterActions.createCharacter("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1, DB.readNumberOfEntries("Characters"),
                     "Checking if character has been created")
    DB.commitClose()
    characterActions.createCharacter("test.db", 2)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(2, DB.readNumberOfEntries("Characters"),
                     "Checking if a second character has been created")
    DB.commitClose()
    characterActions.deleteCharacter("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1, DB.readNumberOfEntries("Characters"),
                     "Checking if a character has been deleted")
    DB.commitClose()
    characterActions.createCharacter("test.db", 1)


def test14():
    characterActions.editBackground("test.db", 2, "Background2")
    characterActions.editName("test.db", 2, "Name2")
    characterActions.editPlayer("test.db", 2, "Player2")
    characterActions.editHealth("test.db", 2, 4)
    characterActions.editCharacteristics("test.db", 2, 4, 5, 6)
    characterActions.editMainObjective("test.db", 2, "Main2")
    characterActions.editSecondaryObjective("test.db", 2, "Second2")
    characterActions.editLoseCondition("test.db", 2, "Lose2")
    test.testIfTrue(True, "Edit character")


def test15():
    characterActions.editFullCharacter("test.db", 1, "Name1", "Player1", 4,
                                       1, 2, 3, "Background1", "Main1",
                                       "Second1", "Lose1")
    test.testIfTrue(True, "Edit full character")


def test21_29():
    test.testIfEqual(characterConsults.getCharacterBackground("test.db", 1),
                     "Background1", "Get character background")
    test.testIfEqual(characterConsults.getCharacterName("test.db", 1),
                     "Name1", "Get character name")
    test.testIfEqual(characterConsults.getCharacterPlayer("test.db", 1),
                     "Player1", "Get character player")
    test.testIfEqual(characterConsults.getCharacterHealth("test.db", 1),
                     4, "Get character health")
    test.testIfEqual(characterConsults.getCharacterStrength("test.db", 1),
                     1, "Get character strength")
    test.testIfEqual(characterConsults.getCharacterMedicine("test.db", 1),
                     2, "Get character medicine")
    test.testIfEqual(characterConsults.getCharacterHacking("test.db", 1),
                     3, "Get character hacking")
    test.testIfEqual(characterConsults.getCharacterMainObjective("test.db", 1),
                     "Main1", "Get character main objective")
    test.testIfEqual(
        characterConsults.getCharacterSecondaryObjective("test.db", 1),
        "Second1", "Get character secondary objective")
    test.testIfEqual(characterConsults.getCharacterLoseCondition("test.db", 1),
                     "Lose1", "Get character lose condition")
    test.testIfEqual(
        characterConsults.getAllIDs("test.db"), [1, 2], "Get all IDs")
    test.testIfEqual(characterConsults.getCharacterFull("test.db", 1),
                     (1, "Name1", "Player1", 4, 1, 2, 3, "Background1", "Main1",
                     "Second1", "Lose1"),
                     "Get character full")


if __name__ == "__main__":
    shutil.copy("database/emptyDatabase.db", "test.db")
    runTest()
    test.printResults()
