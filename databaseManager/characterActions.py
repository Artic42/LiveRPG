import articlib.sqliteEngine as sqliteEngine


def createCharacter(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.addEntry("Characters", "ID", characterID)
    DBConnection.commitClose()


def editName(databasePath, characterID, name):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Characters", "Name", name, f"ID = {characterID}")
    DBConnection.commitClose()


def editPlayer(databasePath, characterID, player):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Characters", "Player", player,
                             f"ID = {characterID}")
    DBConnection.commitClose()


def editCharacteristics(databasePath, characterID,
                        strength, medicine, hacking):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Characters", "Strength", strength,
                             f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "Medicine", medicine,
                             f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "Hacking", hacking,
                             f"ID = {characterID}")
    DBConnection.commitClose()


def editBackground(databasePath, characterID, background):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Characters", "Background", background,
                             f"ID = {characterID}")
    DBConnection.commitClose()


def editMainObjective(databasePath, characterID, mainObjective):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Characters", "MainObjective", mainObjective,
                             f"ID = {characterID}")
    DBConnection.commitClose()


def editSecondaryObjective(databasePath, characterID, secondaryObjective):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Characters", "SecondaryObjective",
                             secondaryObjective, f"ID = {characterID}")
    DBConnection.commitClose()


def editLoseCondition(databasePath, characterID, loseCondition):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Characters", "LoseCondition", loseCondition,
                             f"ID = {characterID}")
    DBConnection.commitClose()


def editFullCharacter(databasePath, characterID, name, player, strength,
                      medicine, hacking, background, mainObjective,
                      secondaryObjective, loseCondition):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.updateEntry("Characters", "Name", name, f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "Player", player,
                             f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "Strength", strength,
                             f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "Medicine", medicine,
                             f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "Hacking", hacking,
                             f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "Background", background,
                             f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "MainObjective", mainObjective,
                             f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "SecondaryObjective",
                             secondaryObjective, f"ID = {characterID}")
    DBConnection.updateEntry("Characters", "LoseCondition", loseCondition,
                             f"ID = {characterID}")
    DBConnection.commitClose()


def deleteCharacter(databasePath, characterID):
    DBConnection = sqliteEngine.sqliteEngine(databasePath)
    DBConnection.deleteEntry("Characters", f"ID = {characterID}")
    DBConnection.commitClose()
