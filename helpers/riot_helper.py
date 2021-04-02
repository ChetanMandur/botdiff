import os

import discord
from dotenv import load_dotenv
from requests.exceptions import HTTPError
from riotwatcher import ApiError, LolWatcher

load_dotenv()
RIOT = os.getenv("RIOT_TOKEN")
lol_watcher = LolWatcher(RIOT)


def queue_type_clean(queuetype):
    ranks = {"RANKED_SOLO_5x5": "Ranked Solo/Duo", "RANKED_TEAM_5x5": "Flex"}

    return ranks.get(queuetype)


def error_handling(error):
    if error.response.status_code == 403:
        return "The Riot API token as expired. Please yell at admin."
    elif error.response.status_code == 404:
        return f"404 error... did you spell the name properly?"

    else:
        return f"""something broke... this is what I know:
> {error}"""
