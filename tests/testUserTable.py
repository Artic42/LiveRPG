from articlib.testEngine import test
import articlib.sqliteEngine as sqliteEngine
import databaseManager.userActions as userActions
import databaseManager.userConsults as userConsults
import shutil


def runTest():
    print("Starting user table test")
    runScenario1()
    runScenario2()
    print("User table test finished")


def runScenario1():
    test.newScenario("Create an user")
    test11_13()
    test14()
    test15()
    test.endScenario("Create an user")


def runScenario2():
    test.newScenario("Get user information")
    test21_29()
    test.endScenario("Get user information")


def test11_13():
    userActions.createUser("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1, DB.readNumberOfEntries("Users"),
                     "Checking if event has been created")
    DB.commitClose()
    userActions.createUser("test.db", 2)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(2, DB.readNumberOfEntries("Users"),
                     "Checking if a second event has been created")
    DB.commitClose()
    userActions.deleteUser("test.db", 1)
    DB = sqliteEngine.sqliteEngine("test.db")
    test.testIfEqual(1, DB.readNumberOfEntries("Users"),
                     "Checking if a event has been deleted")
    DB.commitClose()
    userActions.createUser("test.db", 1)


def test14():
    userActions.editUsername("test.db", 1, "Username1")
    userActions.editPassword("test.db", 1, "Password1")
    userActions.editCharacter("test.db", 1, 2)
    test.testIfTrue(True, "Edit user")


def test15():
    pass


def test21_29():
    username1 = userConsults.readUsername("test.db", 1)
    password1 = userConsults.readPassword("test.db", 1)
    character1 = userConsults.readCharacter("test.db", 1)
    test.testIfEqual("Username1", username1, "Checking username")
    test.testIfEqual("Password1", password1, "Checking password")
    test.testIfEqual(2, character1, "Checking character")


if __name__ == "__main__":
    shutil.copy("database/emptyDatabase.db", "test.db")
    runTest()
    test.printResults()
