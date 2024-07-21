
# Database

The database will be compose of three tables, one for characters, one for events and one for the info of the characters.

## Tables

### Character table

ColumnName | Data Type
-- | --
__CharacterID__ | Integer
Name | Text
Player | Text
Strength | Integer
Medicine | Integer
Hacking | Integer
Background | Text
MainObjective | Text
SecondObjective | Text
LoseCondition | Text

### Events table

ColumnName | Data Type
-- | --
__Event ID__ | Integer
Description | Text
Hack | Bool (Integer)
Equip | Bool (Integer)
Activate | Bool (Integer)
Wait | Integer
Activated | Bool (Integer)
RedirectID | Integer

### Information table

ColumnName | Data Type
-- | --
__InfoID__ | Text
AboutCharacter | Integer
KnownCharacter | Integer
Description | Text

## Actions

Set of action that can be run on the database, for editing the information

### Character actions

- Create a character
- Edit each parameter for each a character
  - Name
  - Player
  - Characteristics
  - Background
  - MainObjective
  - SecondaryObjective
  - LoseCondition

### Event actions

- Create an event
- Edit event
  - Description
  - Flags (Hack, Equip, Activate, Wait)
  - Set activated
  - Reset activated
  - RedirectID

### Information actions

- Create an edit line
- Edit information
  - Edit Known
  - Edit About
  - Edit Description

## Consults

Set of consults that can be run on the database, for reading the information

### Character consults

- List all characters
- List characters characteristics
- List characters objectives
- List characters lose conditions
- List character background
- List character player
- List entire character
- List character name

### Event consults

- List all events
- List event description
- List event flags
- List event activated
- List event redirect

### Information consults

- List all entry of Known Characters
- List all entry of About Characters
- List description of Known Character About Character entry
