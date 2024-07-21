import articlib.sqliteEngine as sqliteEngine

def createInformation(databasePath, ID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.addEntry("Information", "ID", ID)
    DBConnection.commitClose()
    
def editKnownCharacter(databasePath, ID, knownCharacter):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Information", "KnownCharacter", knownCharacter, f"ID = {ID}")
    DBConnection.commitClose()
    
def editAboutCharacter(databasePath, ID, aboutCharacter):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Information", "AboutCharacter", aboutCharacter, f"ID = {ID}")
    DBConnection.commitClose()

def editDescription(databasePath, ID, description):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Information", "Description", description, f"ID = {ID}")
    DBConnection.commitClose()
    
def editFullInformation(databasePath, ID, knownCharacter, aboutCharacter, description):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Information", "KnownCharacter", knownCharacter, f"ID = {ID}")
    DBConnection.updateEntry("Information", "AboutCharacter", aboutCharacter, f"ID = {ID}")
    DBConnection.updateEntry("Information", "Description", description, f"ID = {ID}")
    DBConnection.commitClose()

def deleteInformation(databasePath, ID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.deleteEntry("Information", f"ID = {ID}")
    DBConnection.commitClose()