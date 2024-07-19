
# Database

The database will be compose of three tables, one for characters, one for events and one for the info of the characters.

## Character table

- ¦ -
ColumnName ¦ Data Type
- ¦ -
__CharacterID__ ¦ Integer
Name ¦ Text
Player ¦ Text
Strength ¦ Integer
Medicine ¦ Integer
Hacking ¦ Integer
Background ¦ Text
MainObjective ¦ Text
SecondObjective ¦ Text
LoseCondition ¦ Text

## Events table

- ¦ -
ColumnName ¦ Data Type
-- ¦ --
__Event ID__ ¦ Integer
Description ¦ Text
Hackable ¦ Bool (Integer)
Equipment ¦ Bool (Integer)
Activate ¦ Bool (Integer)
Wait ¦ Integer
Activated ¦ Bool (Integer)
RedirectID ¦ Integer

## Information table

- ¦ -
ColumnName ¦ Data Type
-- ¦ --
AboutCharacter ¦ Integer
KnownCharacter ¦ Integer
Description ¦ Text
