from urllib.request import urlopen

import discord
from bs4 import BeautifulSoup

discord_bot = None
champ_searched = None
role_searched = None

basic_page = "https://na.op.gg/{}/{}/statistics/{}/rune"
aram_ver = 450
urf_ver = 900


def runes_command(bot, champ_name, role, num):
    global discord_bot, champ_searched, role_searched, basic_page, aram_ver, urf_ver
    discord_bot = bot
    champ_searched = champ_name
    role_searched = role

    check = runes_check_input(champ_name, role, num)

    if check == True:
        if role.lower() == "aram":
            runes_page = basic_page.format("aram", champ_name, aram_ver)

        elif role.lower() == "urf":
            runes_page = basic_page.format("urf", champ_name, urf_ver)

        else:
            runes_page = basic_page.format("champion", champ_name, role)

        if num == None:
            return runes_scrape(runes_page, 1)

        else:
            return runes_scrape(runes_page, num)

    else:
        return check


def runes_scrape(runes_page, num):
    html = urlopen(runes_page)
    soup = BeautifulSoup(html, features="html.parser")

    main_tree = []
    sec_tree = []
    shards_tree = []
    type_names = []

    # Grabs the body that contains all rune builds
    for tbody in soup.find_all("tbody"):
        # Grabs the specified row/rune build
        for tr in tbody.find_all("tr")[num - 1 : num]:
            # Parses through the two tree paths
            for perk_trees in tr.find_all("div", class_="perk-page"):

                # Grabs the name of the path
                for perk_tree_type in perk_trees.find_all(
                    "div", class_="perk-page__item perk-page__item--mark"
                ):
                    title = perk_tree_type.findChild().get("title")
                    type_name = title[title.find("'>") + 2 : title.find("</b>")]
                    type_names.append(type_name)

                # Looks through all the runes, and grabs all the active/used runes
                for perk_active in perk_trees.find_all("div"):
                    if "perk-page__item--active" in perk_active["class"]:
                        rune_name = perk_active.findChild().findChild().get("alt")

                        # After the first 4 runes have been found, the rest must be part of secondary tree
                        if len(main_tree) != 4:
                            main_tree.append(rune_name)
                        else:
                            sec_tree.append(rune_name)

            # Grabs the fragments/shards page
            for extras_list in tr.find_all("div", class_="fragment-page"):
                # Grabs all the individual images within the page
                for extra in extras_list.find_all("img"):
                    # Grabs all active/used fragments/shards
                    if "active" in extra["class"][0]:
                        title = extra.get("title")
                        extra_description = title[
                            title.find("<span>") + 6 : title.find("</span>")
                        ]
                        extra_name = extra.get("alt")
                        shards_tree.append([extra_name, extra_description])

    return runes_pretty(main_tree, sec_tree, shards_tree, type_names)


def runes_pretty(main_tree, sec_tree, shards_tree, type_names):
    global champ_searched, role_searched
    try:
        return f"""> __**{champ_searched.upper()} ({role_searched.upper()})**__
        > **{runes_emoji(type_names[0])}**
        > {runes_emoji(main_tree[0])} 
        > {runes_emoji(main_tree[1])}
        > {runes_emoji(main_tree[2])}
        > {runes_emoji(main_tree[3])}
        > 
        > **{runes_emoji(type_names[1])}**
        > {runes_emoji(sec_tree[0])}
        > {runes_emoji(sec_tree[1])}
        > 
        > **Shards**
        > {shards_emoji(shards_tree[0])}
        > {shards_emoji(shards_tree[1])}
        > {shards_emoji(shards_tree[2])}"""

    except IndexError:
        return "No runes found"


def runes_emoji(name):
    global discord_bot
    emoji_name = "Rune_" + name
    emoji_name = emoji_name.replace(" ", "_")
    emoji_name = emoji_name.replace(":", "")
    emoji_name = emoji_name.replace("'", "")
    emoji = discord.utils.get(discord_bot.emojis, name=emoji_name)
    if emoji != None:
        return f"{emoji} {name}"
    else:
        return f"{name}"


def shards_emoji(shard):
    emoji_key_list = {
        "+9 Adaptive Force": "diamond",
        "+10% Attack Speed": "axe",
        "+8 Ability Haste": "time",
        "+6 Armor": "shield",
        "+8 Magic Resist": "circle",
        "+15-90 Health (based on level)": "heart",
    }
    shard_type = shard[0]
    shard_name = shard[1]

    emoji_name = emoji_key_list.get(shard_name)
    emoji = discord.utils.get(discord_bot.emojis, name=emoji_name)

    return f"{emoji} {shard_type} {shard_name}"


def runes_check_input(champ_name, role, num):
    list_of_roles = ["top", "mid", "bot", "adc", "support", "jungle", "aram", "urf"]

    if num != None:
        try:
            num = int(num)

        except Exception:
            return "The page number must be a digit"

    elif champ_name == None:
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
