import articlib.sqliteEngine as sqliteEngine


def createUser(databasePath, userID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.addEntry("Users", "UserID", userID)
    DBConnection.commitClose()


def deleteUser(databasePath, userID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.deleteEntry("Users", f"UserID = {userID}")
    DBConnection.commitClose()


def editUsername(databasePath, userID, username):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Users", "Username", username, f"UserID = {userID}")
    DBConnection.commitClose()


def editPassword(databasePath, userID, password):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Users", "Password", password, f"UserID = {userID}")
    DBConnection.commitClose()


def editCharacter(databasePath, userID, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Users", "CharacterID", characterID, f"UserID = {userID}")
    DBConnection.commitClose()
