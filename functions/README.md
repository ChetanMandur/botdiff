# Functions
This is where all the main functions of the bot reside. Each file should share the same name as its corresponding Discord command.

## **Functions List:**
As this bot is a WIP, some of the commands have not been implimented yet.

- #### `test.py`
  - Simple test functions/commands that can be done with the bot
  - Commands:
    - `None` (aka no command) - Displays hello world message
    - `saymyname` - Displays name of user
    - `bold` - Displays sample message with use of bolding
    - `block` - Displays sample message with use of blocking
    - `colour` - Displays sample message with use of colour
    - `emoji` - Displays sample message with use of emoji
    - `lolsum <username>` - Example of Riot Watcher API, displays username and level
- #### `sum.py`
  - Displays basic information about a summoner 
    - `None` (aka no command) - Displays usage message
    - `<username>` - Displays level and IDs
    - `<username> level` - Displays level
    - `<username> id` - Displays IDs
    - `<username> rankedstat` - Displays rank, win/loss, league points, and hotstreak status
- #### `runes.py` (WIP)
  - Displays the most common runes for a given champion
    - `<champion>` - Displays the top runes for the given champion
    - `<champion> <1..5>` - Displays other top runes for the given champion 
- #### `topcharacters.py` (WIP)
  - Displays the top characters for a given summoner and their win rates
    - `<summoner>` - Read above
- #### `recentgames.py` (WIP)
  - Displays the most recent matches of a given summoner and offers way to view matches
     - `<summoner>` - Lists the most recent matches in a number list, with 1 being the most recent
     - `<summoner> <1..>` - Opens the specifed recent match
     - `<summoner> <1..> runes` - Sees the currently used runes of the player
     - `<summoner> <1..> avgrank` - Sees the average rank of both teams (individual)
     - `<summoner> <1..> bans` - Sees the bans of each team 
- #### `live.py` (WIP)
   - Displays the current live match of a given summoner
     - `<username>` - If the player is in a match, displays current champ, queue type, teams/other players, current K/D/A, summoner spells, and current gametime
     - `<username> runes` - Sees the currently used runes of the player
     - `<username> avgrank` - Sees the average rank of both teams (individual)
     - `<username> bans` - Sees the bans of each team 