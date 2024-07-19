
# Database

The database will be compose of three tables, one for characters, one for events and one for the info of the characters.

## Character table

- ¦ -
ColumnName ¦ Data Type
- ¦ -
Name ¦ Text
Player ¦ Text
Strength ¦ Integer
Medicine ¦ Integer
Hacking ¦ Integer
Background ¦ Text
Main Objective ¦ Text
Secondary Objective ¦ Text
Lose condition ¦ Text

## Events table

- ¦ -
ColumnName ¦ Data Type
-- ¦ --
Event ID ¦ Integer
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
AboutCharacter ¦ Text
KnownCharacter ¦ Text
Description ¦ Text
