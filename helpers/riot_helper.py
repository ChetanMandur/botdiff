import os

from dotenv import load_dotenv
from riotwatcher import ApiError, LolWatcher

load_dotenv()
RIOT = os.getenv("RIOT_TOKEN")
lol_watcher = LolWatcher(RIOT)


def queue_type_clean(queuetype):
    ranks = {"RANKED_SOLO_5x5": "Ranked Solo/Duo", "RANKED_TEAM_5x5": "Flex"}

    return ranks.get(queuetype)
