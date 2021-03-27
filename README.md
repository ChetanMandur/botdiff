# Riot League Bot (WIP)

## **Quick Installation:**
Make sure you have Python 3.6+ and virtualenv (`pip install virtualenv`)
1. Clone the repo 
2. Go into the newly cloned repo using a CLI
3. Create a python virtual environment using `python3 -m virtualenv env`
4. Load the virtual environment by using `source env/bin/activate` (for Windows mans, use `C:\<path_to_riotleaguebot>\env\Scripts\activate.bat`)
5. Finally, install the dependencies by using `pip install -r requirements.txt`

## **Getting Tokens/Setup**

### **Discord Bot**

Setting up a Discord bot is important when testing features.  
For more information, go check out the [offical Discord dev docs](https://discord.com/developers/docs/intro)

### **Riot API/Tokens**

You will need to get your own API tokens from Riot. These dev tokens refresh every 24 hours.  
To get your own token, go to [Riot's dev pages](https://developer.riotgames.com/)


## **Setting up Token**
With this project, API tokens are needed to communicate with both Discord API and Riot API.  
To handle these tokens, we store the files in a `.env` file (is coved by .gitignore).
Here are the token names we use: 
1. `DISCORD_TOKEN` - This is where the Discord API token will be stored
2. `DISCORD_GUILD` - This is where the Discord GUILD will be stored
3. `RIOT_TOKEN` - This is where the Riot API token will be stored  

You will need to create this file yourself (in root) and paste your own tokens.


## **Code Style Guide**

### **Creating Branches**
Before making any changes to the code, you must create your own branch/fork.  
For the sake of continuity, branches should follow this specific format: `<name>-<main_changes>`  
For example: `chetan-cool-new-feature`
### **Creating Functions**
With the structure of this repo, we want to make sure logic isn't bloating `main.py`.  
To do this, we are following a file structure that puts logic away in another file.  
This logic is then called when running the command.  
To follow this structure, do the following:
1. In `main.py` create an async function with the following format:
``` 
@bot.command()
async def <name>(ctx):
    await ctx.send(<name>_command())
```
2. Place `<name>_command()` in `functions/<name>.py`
3. Import this file into `main.py` by using `from functions.<name> import <name>_command`
4. Test the function/bot by running `python3 main.py`

### **Other Notes**
Use `snake_case`! :) 


## **Common Git Commands:**

### **Pushing code:**
1. `git checkout -b "<branch name>"` - Creates a branch from your current branch
2. `git status` - Checks the status of changes
3. `git add .` - Adds all changes/files
4. `git commit -m "<Message>"` - Creates a commit (OR `git commit` to open vim like a l33t chad :3)
5. `git push` - Pushes the branch to GitHub

### **Rebasing:**
1. `git checkout main` - Switches your branch to main
2. `git pull` - Pulls the most recent code from main
3. `git checkout <branch name>` - Switches back to the branch you are working on/want to rebase
4. `git rebase main` - Starts the rebasing with main, conflicts might occur just solve them with your IDE
5. `git push -f` - Force pushes your branch to origin, ready for PR

### **Extra Git Commands:**
1. `git checkout <branch name>` - Swaps to a branch (doesn't create one)
2. `git fetch` - Notes any differences between local and origin

## **Open Source Projects we use:**
This project could not be possible without the help of opensource projects.  
Here's the main projects that we use:
1. [Discord.py](https://github.com/Rapptz/discord.py) - The Python wrapper for Discord API
2. [Riot Watcher](https://github.com/pseudonym117/Riot-Watcher) - The Python wrapper for Riot API
3. [python-dotenv](https://github.com/theskumar/python-dotenv) - Handles the tokens
