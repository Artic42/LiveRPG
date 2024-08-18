from articlib.testEngine import test
import tests.testCharacterTable
import tests.testEventTable
import tests.testInformationTable
import tests.testUserTable
import shutil


def runTest():
    print("Starting database manager tests")
    shutil.copy("database/emptyDatabase.db", "test.db")
    tests.testCharacterTable.runTest()
    tests.testEventTable.runTest()
    tests.testInformationTable.runTest()
    tests.testUserTable.runTest()
    print("Database manager tests finished")


if __name__ == "__main__":
    runTest()
    test.printResults()
