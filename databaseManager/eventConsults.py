import articlib.sqliteEngine as sqliteEngine

def getAllIDs(databasePath):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntry("Events", "ID")
    DBConnection.commitClose()
    return [i[0] for i in result]

def getEventName(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Events", "Name", f"ID = {eventID}")
    DBConnection.commitClose()
    return result[0][0]

def getEventDescription(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Events", "Description", f"ID = {eventID}")
    DBConnection.commitClose()
    return result[0][0]

def getEventHack(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Events", "Hack", f"ID = {eventID}")
    DBConnection.commitClose()
    return result[0][0]

def getEventEquip(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Events", "Equip", f"ID = {eventID}")
    DBConnection.commitClose()
    return result[0][0]

def getEventActivate(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Events", "Activate", f"ID = {eventID}")
    DBConnection.commitClose()
    return result[0][0]

def getEventWait(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Events", "Wait", f"ID = {eventID}")
    DBConnection.commitClose()
    return result[0][0]

def getEventActivated(databasePath, eventID):    
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Events", "Activated", f"ID = {eventID}")
    DBConnection.commitClose()
    if result[0][0] == 1:
        return True
    else:
        return False
    
def getEventRedirectID(databasePath, eventID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Events", "RedirectID", f"ID = {eventID}")
    DBConnection.commitClose()
    return result[0][0]