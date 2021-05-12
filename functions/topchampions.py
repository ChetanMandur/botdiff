from re import findall
from urllib.request import urlopen, urlretrieve

import requests
from bs4 import BeautifulSoup
from bs4.builder import HTML

basic_page = "https://na.op.gg/summoner/userName={}"
basic_champions_page = "https://na.op.gg/summoner/champions/ajax/champions.most/summonerId={}&season={}&queueType={}&"
queueType = {"all": "all", "solo": "soloranked", "flex": "flexranked5v5"}


def topchampions_command(sum_name, queue):
    url = basic_page.format(sum_name)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    top_champions = []

    if queue == "all":
        top_champions = get_all_data(soup)
    elif queue == "solo" or queue == "flex":
        top_champions = get_ranked_data(soup, queue)
    else:
        return "Invalid Input"

    return format_data(top_champions)


def get_all_data(soup):
    top_champions = []
    champions = soup.find_all("div", class_="ChampionBox Ranked")

    for rank, champion in enumerate(champions):
        data = {}
        data["rank"] = rank + 1
        data["name"] = champion.find("div", class_="ChampionName")["title"]
        data["winrate"] = champion.find("div", class_="WinRatio").getText().strip()
        data["kda"] = (
            champion.find("div", class_="KDA").getText().strip().split(":", 1)[0]
        )
        data["cs"] = champion.find("div", class_="ChampionMinionKill").getText().strip()
        data["played"] = champion.find("div", class_="Title").getText().strip()
        top_champions.append(data)

    return top_champions


def get_ranked_data(soup, queue):
    sum_data = soup.find("div", attrs={"data-summoner-id": True})
    sum_id = sum_data["data-summoner-id"]
    season = sum_data["data-season"]

    champions_url = basic_champions_page.format(sum_id, season, queueType[queue])
    champions_page = requests.get(champions_url)
    soup = BeautifulSoup(champions_page.content, "html.parser")

    top_champions = []
    champions = soup.find_all("div", class_="ChampionBox")

    for rank, champion in enumerate(champions):
        data = {}
        data["rank"] = rank + 1
        data["name"] = champion.find("div", class_="ChampionName")["title"]
        data["winrate"] = champion.find("div", class_="WinRatio").getText().strip()
        data["kda"] = (
            champion.find("div", class_="KDA").getText().strip().split(":", 1)[0]
        )
        data["cs"] = champion.find("div", class_="ChampionMinionKill").getText().strip()
        data["played"] = champion.find("div", class_="Title").getText().strip()
        top_champions.append(data)

    return top_champions


def format_data(top_champions):
    retval = ""
    for champion in top_champions:
        retval += f"{champion['rank']}. {champion['name']} winrate {champion['winrate']} played {champion['played']}\n"
    return retval
