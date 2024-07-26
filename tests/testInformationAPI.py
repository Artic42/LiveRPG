from articlib.testEngine import test
import APIManager.informationRequest as informationRequest
import APIManager.request as request


def runTest():
    print("Starting information API test")
    runScenario1()
    runScenario2()
    runScenario3()
    print("Event API information finished")


def runScenario1():
    test.newScenario("Read all events and create a new information entry")
    test12()
    test13()
    test.endScenario("Read all events and create a new information entry")


def runScenario2():
    test.newScenario("Write and read each parameter one by one")
    test21()
    test22()
    test23()
    test.endScenario("Write and read each parameter one by one")


def runScenario3():
    test.newScenario("Write and Read all information in one go")
    test31()
    test32()
    test.endScenario("Write and Read all information in one go")


def test12():
    response = informationRequest.createInformation(20)
    test.testIfEqual(response.json()["status"], 200, "Create event status")


def test13():
    response = informationRequest.deleteInformation(20)
    test.testIfEqual(response.json()["status"], 200, "Delete event status")


def test21():
    response = informationRequest.editKnownCharacter(1, "NewKnown1")
    test.testIfEqual(response.json()["status"], 200, "Edit known character")
    response = informationRequest.readKnownCharacter(1)
    test.testIfEqual(response.json()["knownCharacter"], "NewKnown1",
                     "Read known character")


def test22():
    response = informationRequest.editAboutCharacter(1, "NewAbout1")
    test.testIfEqual(response.json()["status"], 200, "Edit about character")
    response = informationRequest.readAboutCharacter(1)
    test.testIfEqual(response.json()["aboutCharacter"], "NewAbout1",
                     "Read about character")


def test23():
    response = informationRequest.editDescription(1, "NewDescription1")
    test.testIfEqual(response.json()["status"], 200, "Edit description")
    response = informationRequest.readDescription(1)
    test.testIfEqual(response.json()["description"], "NewDescription1",
                     "Read description")


def test31():
    response = informationRequest.editFullInformation(2,
                                                      "NewKnown2",
                                                      "NewAbout2",
                                                      "NewDescription2")
    test.testIfEqual(response.json()["status"], 200, "Edit event status")


def test32():
    response = informationRequest.readFullInformation(2)
    test.testIfEqual(response.json()["knownCharacter"], "NewKnown2",
                     "Read known character")
    test.testIfEqual(response.json()["aboutCharacter"], "NewAbout2",
                     "Read about character")
    test.testIfEqual(response.json()["description"], "NewDescription2",
                     "Read description")


if __name__ == "__main__":
    request.activateTestMode()
    runTest()
    test.printResults()
    request.deactivateTestMode()
