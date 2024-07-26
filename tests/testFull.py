from articlib.testEngine import test
import tests.testDatabaseManager as testDatabaseManager
import tests.testAPI as testAPI


def runTest():
    print("Starting tests")

    testDatabaseManager.runTest()
    testAPI.runTest()

    print("Tests finished")


if __name__ == "__main__":
    runTest()
    test.printResults()
