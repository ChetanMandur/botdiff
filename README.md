# Riot League Bot (WIP)

## Quick Installation:
Make sure you have Python 3.6+ and virtualenv (`pip install virtualenv`)
1. Clone the repo 
2. Go into the newly cloned repo using a CLI
3. Create a python virtual environment using `python3 -m virtualenv env`
4. Load the virtual environment by using `source env/bin/activate` (for Windows mans, use `C:\<path_to_riotleaguebot>\env\Scripts\activate.bat`)
5. Finally, install the dependencies by using `pip install -r requirements.txt`


## Setting up Token (WIP)
With this project, API tokens are needed to communicate with both Discord API and Riot API.  
To handle these tokens, we store the files in a `.env` file (is coved by .gitignore).
Here are the token names we use: 
1. `DISCORD_TOKEN` - This is where the Discord API token will be stored
2. `DISCORD_GUID` - This is where the Discord GUID will be stored
3. `RIOT_TOKEN` - This is where the Riot API token will be stored  

You will need to create this file yourself and paste your own tokens.


## Common Git Commands:

### Pushing code:
1. `git checkout -b "<branch name>"` - Creates a branch from your current branch
2. `git status` - Checks the status of changes
3. `git add .` - Adds all changes/files
4. `git commit -m "<Message>"` - Creates a commit 
5. `git push` - Pushes the branch to GitHub

### Rebasing:
1. `git checkout main` - Switches your branch to main
2. `git pull` - Pulls the most recent code from main
3. `git checkout <branch name>` - Switches back to the branch you are working on/want to rebase
4. `git rebase main` - Starts the rebasing with main, conflicts might occur just solve them with your IDE
5. `git push -f` - Force pushes your branch to origin, ready for PR

### Extra Git Commands:
1. `git checkout <branch name>` - Swaps to a branch (doesn't create one)
2. `git fetch` - Notes any differences between local and origin

## Open Source Projects we use:
This project could not be possible without the help of opensource projects.  
Here's the main projects that we use:
1. [Discord.py](https://github.com/Rapptz/discord.py) - The Python wrapper for Discord API
2. [Riot Watcher](https://github.com/pseudonym117/Riot-Watcher) - The Python wrapper for Riot API
3. [python-dotenv](https://github.com/theskumar/python-dotenv) - Handles the tokens
