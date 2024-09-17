import articlib.sqliteEngine as sqliteEngine


def readUsername(databasePath, userID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    username = DBConnection.readEntryFiltered("Users", "Username", f"UserID = {userID}")
    DBConnection.commitClose()
    return username[0][0]


def readPassword(databasePath, userID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    password = DBConnection.readEntryFiltered("Users", "Password", f"UserID = {userID}")
    DBConnection.commitClose()
    return password[0][0]


def readCharacter(databasePath, userID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    characterID = DBConnection.readEntryFiltered("Users", "CharacterID", f"UserID = {userID}")
    DBConnection.commitClose()
    return characterID[0][0]


def getID(databasePath, username):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    ID = DBConnection.readEntryFiltered("Users", "UserID", f"Username = '{username}'")
    DBConnection.commitClose()
    return ID[0][0]
