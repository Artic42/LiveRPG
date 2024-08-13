import articlib.sqliteEngine as sqliteEngine


def getAllIDs(databasePath):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntry("Information", "ID")
    DBConnection.commitClose()
    return [i[0] for i in result]


def getKnownCharacter(databasePath, ID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Information", "KnownCharacter",
                                            f"ID = {ID}")
    DBConnection.commitClose()
    return result[0][0]


def getAboutCharacter(databasePath, ID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Information", "AboutCharacter",
                                            f"ID = {ID}")
    DBConnection.commitClose()
    return result[0][0]


def getDescription(databasePath, ID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Information", "Description",
                                            f"ID = {ID}")
    DBConnection.commitClose()
    return result[0][0]


def getFullInformation(databasePath, ID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Information", "*", f"ID = {ID}")
    DBConnection.commitClose()
    return result[0]


def getIDsForKnownCharacter(databasePath, knownCharacter):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered(
        "Information", "ID",
        f"KnownCharacter = '{knownCharacter}'")
    DBConnection.commitClose()
    return [i[0] for i in result]
