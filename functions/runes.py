from urllib.request import urlopen

import discord
from bs4 import BeautifulSoup
from data_structures.rune_page import RunePage

discord_bot = None

basic_page = "https://na.op.gg/{}/{}/statistics/{}/rune"
aram_ver = 450
urf_ver = 900


def runes_command(discord_bot, champ_name, role, num):
    global basic_page, aram_ver, urf_ver

    if num != None:
        try:
            num = int(num)

        except Exception:
            return "The page number must be a digit"

    check = runes_check_input(champ_name, role, num)

    if check == True:
        if role.lower() == "aram":
            runes_page = basic_page.format("aram", champ_name, aram_ver)

        elif role.lower() == "urf":
            runes_page = basic_page.format("urf", champ_name, urf_ver)

        else:
            runes_page = basic_page.format("champion", champ_name, role)

        if num == None:
            return runes_scrape(runes_page, 1, champ_name, role, discord_bot)

        else:
            return runes_scrape(runes_page, num, champ_name, role, discord_bot)

    else:
        return check


def runes_scrape(runes_page, num, champ_name, role, discord_bot):
    html = urlopen(runes_page)
    soup = BeautifulSoup(html, features="html.parser")

    runes = RunePage(champ_name, role)

    # Grabs the main tbody which houses the runes rows
    main_tbody = soup.find("div", class_="tabItem ChampionKeystoneRune-1").findChild(
        "tbody"
    )

    # Goes through each row in the
    for tr in main_tbody.find_all("tr")[num - 1 : num]:
        # Parses through the two tree paths
        for perk_trees in tr.find_all("div", class_="perk-page"):

            # Grabs the name of the path
            for perk_tree_type in perk_trees.find_all(
                "div", class_="perk-page__item perk-page__item--mark"
            ):
                title = perk_tree_type.findChild().get("title")
                type_name = title[title.find("'>") + 2 : title.find("</b>")]
                runes.type_names.append(type_name)

            # Looks through all the runes, and grabs all the active/used runes
            for perk_active in perk_trees.find_all("div"):
                if "perk-page__item--active" in perk_active["class"]:
                    rune_name = perk_active.findChild().findChild().get("alt")

                    # After the first 4 runes have been found, the rest must be part of secondary tree
                    if len(runes.main_tree) != 4:
                        runes.main_tree.append(rune_name)
                    else:
                        runes.sec_tree.append(rune_name)

        # Grabs the fragments/shards page
        for shards_list in tr.find_all("div", class_="fragment-page"):
            # Grabs all the individual images within the page
            for shard in shards_list.find_all("img"):
                # Grabs all active/used fragments/shards
                if "active" in shard["class"][0]:
                    title = shard.get("title")
                    shard_description = title[
                        title.find("<span>") + 6 : title.find("</span>")
                    ]
                    shard_name = shard.get("alt")
                    runes.shards_tree.append([shard_name, shard_description])

    return runes.pretty_print(discord_bot)


def runes_check_input(champ_name, role, num):
    list_of_roles = ["top", "mid", "bot", "adc", "support", "jungle", "aram", "urf"]

    if champ_name == None:
        return f"""> **Usage**
        > `sum <Champ Name> <Role> <(Optional) Page Number>` """

    elif role == None or role not in list_of_roles:
        return f"""You need to provide a role. Possible options are:
  - 'top'
  - 'mid'
  - 'bot'/'adc'
  - 'support'
  - 'jungle'
  - 'aram'
  - 'urf'"""

    elif isinstance(num, int) and num > 5:
        return "Please pick a number between 1-5"

    else:
        return True
