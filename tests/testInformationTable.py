from articlib.testEngine import test
import databaseManager.infoActions as infoActions
import databaseManager.infoConsults as infoConsults
import articlib.sqliteEngine as sqliteEngine
import shutil

def runTest():
    print("Starting information table test")
    runScenario1()
    runScenario2()
    print("Information table test finished")
    
def runScenario1():
    test.newScenario("Create an information")
    test11_13()
    test14()
    test15()
    test.endScenario("Create an information")

def runScenario2():
    test.newScenario("Get information information")
    test21_29()
    test.endScenario("Get information information")
    
def test11_13():
    infoActions.createInformation("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1,DB.readNumberOfEntries("Information"),"Checking if information has been created")
    DB.commitClose()
    infoActions.createInformation("test.db", 2)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(2,DB.readNumberOfEntries("Information"), "Checking if a second information has been created")
    DB.commitClose()
    infoActions.deleteInformation("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1,DB.readNumberOfEntries("Information"), "Checking if a information has been deleted")
    DB.commitClose()
    infoActions.createInformation("test.db", 1)    

def test14():
    infoActions.editDescription("test.db", 2, "Description2")
    infoActions.editKnownCharacter("test.db", 2, 1)
    infoActions.editAboutCharacter("test.db", 2, 0)
    test.testIfTrue(True, "Edit information")
    infoActions.editFullInformation("test.db", 1, 1, 0, "Description1")

def test15():
    infoActions.editFullInformation("test.db", 2, 1, 0, "Description2")
    test.testIfTrue(True, "Edit full information")

def test21_29():
    test.testIfEqual([1,2], infoConsults.getAllIDs("test.db"), "Get all IDs")
    test.testIfEqual("Description2", infoConsults.getDescription("test.db", 2), "Get description")
    test.testIfEqual(1, infoConsults.getKnownCharacter("test.db", 2), "Get known character")
    test.testIfEqual(0, infoConsults.getAboutCharacter("test.db", 2), "Get about character")
    test.testIfEqual("Description1", infoConsults.getDescription("test.db", 1), "Get description")

if __name__ == "__main__":
    shutil.copy("database/emptyDatabase.db", "test.db")
    runTest()
    test.printResults()
    