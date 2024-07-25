from articlib.testEngine import test
import APIManager.eventRequest as eventRequest
import APIManager.request as request


def runTest():
    print("Starting event API test")
    runScenario1()
    runScenario2()
    runScenario3()
    print("Event API test finished")


def runScenario1():
    test.newScenario("Read all events and create a new event")
    test12()
    test13()
    test.endScenario("Read all events and create a new event")


def runScenario2():
    test.newScenario("Write and read each parameter one by one")
    test21()
    test22()
    test23()
    test24()
    test.endScenario("Write and read each parameter one by one")


def runScenario3():
    test.newScenario("Write and Read all event in one go")
    test31()
    test32()
    test.endScenario("Write and Read all event in one go")


def test12():
    response = eventRequest.createEvent(20)
    test.testIfEqual(response.json()["status"], 200, "Create event status")


def test13():
    events = eventRequest.deleteEvent(20)
    test.testIfEqual(events.json()["status"], 200,
                     "Delete event status")


def test21():
    response = eventRequest.editEventDescription(1, "NewDescription1")
    print(response)
    print(response.json())
    test.testIfEqual(response.json()["status"], 200, "Edit description status")
    name = eventRequest.readEventDescription(1)
    test.testIfEqual(name.json()["description"], "NewDescription1",
                     "Read description")


def test22():
    response = eventRequest.editEventFlags(1, 1, 0, 1, 0)
    test.testIfEqual(response.json()["status"], 200, "Edit flags")
    flags = eventRequest.readEventFlags(1)
    test.testIfEqual(flags.json()["hack"], 1, "Read hack")
    test.testIfEqual(flags.json()["equip"], 0, "Read equip")
    test.testIfEqual(flags.json()["activate"], 1, "Read activate")
    test.testIfEqual(flags.json()["wait"], 0, "Read wait")


def test23():
    response = eventRequest.editRedirectEvent(1, 2)
    test.testIfEqual(response.json()["status"], 200,
                     "Edit event status")
    redirectID = eventRequest.readEventRedirect(1)
    test.testIfEqual(redirectID.json()["redirectID"], 2, "Read redirect ID")


def test24():
    response = eventRequest.activateEvent(1)
    test.testIfEqual(response.json()["status"], 200,
                     "Edit event status")
    activate = eventRequest.readEventActivated(1)
    test.testIfEqual(1, activate.json["activate"], "Read activate")
    response = eventRequest.deactivateEvent(1)
    test.testIfEqual(response.json()["status"], 200,
                     "Edit event status")
    activate = eventRequest.readEventActivated(1)
    test.testIfEqual(0, activate.json["activate"], "Read activate")


def test31():
    response = eventRequest.editFullEvent(2,
                                          "newDescription2",
                                          0,
                                          1,
                                          0,
                                          10,
                                          0,
                                          1)
    test.testIfEqual(response.json()["status"], 200, "Edit event status")


def test32():
    event = eventRequest.readEvent(2)
    test.testIfEqual(event.json()["description"], "NewDescription2",
                     "Read description")
    test.testIfEqual(event.json()["hacking"], 0, "Read hacking")
    test.testIfEqual(event.json()["equip"], 1, "Read equip")
    test.testIfEqual(event.json()["activate"], 0, "Read activate")
    test.testIfEqual(event.json()["wait"], 10, "Read wait")
    test.testIfEqual(event.json()["activated"], 0, "Read activated")
    test.testIfEqual(event.json()["redirectID"], 1, "Read redirect ID")
    test.testIfEqual(event.json()["SecondaryObjective"],
                     "NewSecondaryObjective2", "Read secondary objective")
    test.testIfEqual(event.json()["LoseCondition"],
                     "NewLoseCondition2", "Read lose condition")


if __name__ == "__main__":
    request.activateTestMode()
    runTest()
    test.printResults()
    request.deactivateTestMode()
