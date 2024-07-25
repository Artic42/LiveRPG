import articlib.sqliteEngine as sqliteEngine


def createEvent(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.addEntry("Events", "ID", eventID)
    DBConnection.commitClose()


def deleteEvent(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.deleteEntry("Events", f"ID = {eventID}")
    DBConnection.commitClose()


def editDescription(databasePath, eventID, description):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Events", "Description", description,
                             f"ID = {eventID}")
    DBConnection.commitClose()


def editFlags(databasePath, eventID, hack, equip, activate, wait):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Events", "Hack", hack, f"ID = {eventID}")
    DBConnection.updateEntry("Events", "Equip", equip, f"ID = {eventID}")
    DBConnection.updateEntry("Events", "Activate", activate, f"ID = {eventID}")
    DBConnection.updateEntry("Events", "Wait", wait, f"ID = {eventID}")
    DBConnection.commitClose()


def setActivated(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Events", "Activated", 1, f"ID = {eventID}")
    DBConnection.commitClose()


def resetActivated(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Events", "Activated", 0, f"ID = {eventID}")
    DBConnection.commitClose()


def editRedirectID(databasePath, eventID, redirectID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Events", "RedirectID", redirectID,
                             f"ID = {eventID}")
    DBConnection.commitClose()


def editFullEvent(databasePath, eventID, description, hack,
                  equip, activate, wait, activated, redirectID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Events", "Description",
                             description, f"ID = {eventID}")
    DBConnection.updateEntry("Events", "Hack", hack, f"ID = {eventID}")
    DBConnection.updateEntry("Events", "Equip", equip, f"ID = {eventID}")
    DBConnection.updateEntry("Events", "Activate", activate, f"ID = {eventID}")
    DBConnection.updateEntry("Events", "Wait", wait, f"ID = {eventID}")
    DBConnection.updateEntry("Events", "Activated",
                             activated, f"ID = {eventID}")
    DBConnection.updateEntry("Events", "RedirectID",
                             redirectID, f"ID = {eventID}")
    DBConnection.commitClose()
