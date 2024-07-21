from articlib.testEngine import test
import articlib.sqliteEngine as sqliteEngine
import databaseManager.eventActions as eventActions
import databaseManager.eventConsults as eventConsults
import shutil

def runTest():
    print("Starting databaseManager test")
    runScenario1()
    runScenario2()
    print("databaseManager test finished")
    
def runScenario1():
    test.newScenario("Create an event")
    test11_13()
    test14()
    test15()
    test.endScenario("Create an event")
    
def runScenario2():
    test.newScenario("Get event information")
    test21_29()
    test.endScenario("Get event information")
    
def test11_13():
    eventActions.createEvent("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1,DB.readNumberOfEntries("Events"),"Checking if event has been created")
    DB.commitClose()
    eventActions.createEvent("test.db", 2)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(2,DB.readNumberOfEntries("Events"), "Checking if a second event has been created")
    DB.commitClose()
    eventActions.deleteEvent("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1,DB.readNumberOfEntries("Events"), "Checking if a event has been deleted")
    DB.commitClose()
    eventActions.createEvent("test.db", 1)
    
def test14():
    eventActions.editDescription("test.db", 2, "Description2")
    eventActions.editFlags("test.db", 2, 1, 0, 1, 0)
    eventActions.setActivated("test.db", 2)
    eventActions.resetActivated("test.db", 2)
    eventActions.editRedirectID("test.db", 2, 3)
    test.testIfTrue(True, "Edit event")
    eventActions.setActivated("test.db", 2)
    
def test15():
    eventActions.editFullEvent("test.db", 1, "Description1", 1, 2, 3, 4, 0, 2)
    test.testIfTrue(True, "Edit full event")

def test21_29():
    test.testIfEqual([1,2], eventConsults.getAllIDs("test.db"), "Get all IDs")
    test.testIfEqual("Description2", eventConsults.getEventDescription("test.db", 2), "Get description")
    test.testIfTrue(eventConsults.getEventActivated("test.db", 2), "Get activated")
    test.testIfEqual(3, eventConsults.getEventRedirectID("test.db", 2), "Get redirect ID")
    test.testIfTrue(eventConsults.getEventHack("test.db", 2), "Get hack")
    test.testIfFalse(eventConsults.getEventEquip("test.db", 2), "Get equip")
    test.testIfEqual("Description1", eventConsults.getEventDescription("test.db", 1), "Get description")
    test.testIfTrue(eventConsults.getEventActivated("test.db", 2), "Get activated")
    test.testIfEqual(0, eventConsults.getEventWait("test.db", 2), "Get wait")
    


if __name__ == "__main__":
    shutil.copy("database/emptyDatabase.db", "test.db")
    runTest()
    test.printResults()  