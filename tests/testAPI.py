from articlib.testEngine import test
import APIManager.request as request
import tests.testCharacterAPI as testCharacterAPI
import tests.testEventAPI as testEventAPI
import tests.testInformationAPI as testInformationAPI


def runTest():
    print("Starting API tests")

    request.activateTestMode()

    testCharacterAPI.runTest()
    testEventAPI.runTest()
    testInformationAPI.runTest()

    print("API tests finished")


if __name__ == "__main__":
    runTest()
    test.printResults()
