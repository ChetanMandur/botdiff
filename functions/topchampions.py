import requests
from bs4 import BeautifulSoup


def topchampions_command(ctx, sum_name, ext):

    URL = f"https://na.op.gg/summoner/userName={sum_name}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, "html.parser")
    champions = soup.find_all(attrs={"class": "ChampionInfo"})
    retval = ""

    for x in range(0, 7):
        retval += (champions[x].div.a.text.strip()) + "\n"

    return retval
