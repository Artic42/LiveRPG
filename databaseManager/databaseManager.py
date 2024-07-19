import articlib.sqliteEngine as sqliteEngine

def connectToDatabase(databasePath="test.db"):
    return sqliteEngine.sqliteEngine.connectToDatabase(databasePath)

DBConnection = connectToDatabase()