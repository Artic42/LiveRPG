from articlib.testEngine import test
import articlib.sqliteEngine as sqliteEngine
import databaseManager.characterActions as characterActions
import shutil

def runTest():
    print("Starting databaseManager test")
    shutil.copy("emptyDatabase.db", "test.db")
    runScenario1()
    print("databaseManager test finished")
    
def runScenario1():
    test.newScenario("Create a character")
    test11_13()
    test14()
    test15()
    test.endScenario("Create a character")
    
def test11_13():
    characterActions.createCharacter("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1,DB.readNumberOfEntries("Characters"),"Checking if character has been created")
    DB.commitClose()
    characterActions.createCharacter("test.db", 2)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(2,DB.readNumberOfEntries("Characters"), "Checking if a second character has been created")
    DB.commitClose()
    characterActions.deleteCharacter("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1,DB.readNumberOfEntries("Characters"), "Checking if a character has been deleted")
    DB.commitClose()
    
def test14():
    characterActions.editBackground("test.db", 2, "Background")
    characterActions.editName("test.db", 2, "Aron")
    characterActions.editPlayer("test.db", 2, "Mo")
    characterActions.editCharacteristics("test.db", 2, 1, 2, 3)
    characterActions.editMainObjective("test.db", 2, "abcde")
    characterActions.editSecondaryObjective("test.db", 2, "esta")
    characterActions.editLoseCondition("test.db", 2, "liso")
    test.testIfTrue(True, "Edit character")

def test15():
    characterActions.editFullCharacter("test.db", 2, "Aren", "Alter", 1, 2, 3, "fere", "asdf", "neo", "orle")
    test.testIfTrue(True, "Edit full character")
    
    
    
if __name__ == "__main__":
    runTest()
    test.printResults()  
