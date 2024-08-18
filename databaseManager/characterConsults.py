import articlib.sqliteEngine as sqliteEngine


def getAllIDs(databasePath):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntry("Characters", "ID")
    DBConnection.commitClose()
    return [i[0] for i in result]


def getCharacterName(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "Name",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterPlayer(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "Player",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterHealth(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "Health",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterStrength(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "Strength",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterMedicine(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "Medicine",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterHacking(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "Hacking",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterBackground(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "Background",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterMainObjective(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "MainObjective",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterSecondaryObjective(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "SecondaryObjective",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterLoseCondition(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "LoseCondition",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0][0]


def getCharacterFull(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    result = DBConnection.readEntryFiltered("Characters", "*",
                                            f"ID = {characterID}")
    DBConnection.commitClose()
    return result[0]
