from urllib.request import urlopen

from bs4 import BeautifulSoup


def runes_command(champ_name, role, num):
    if num != None:
        try:
            num = int(num)

        except Exception:
            return "The page number must be a digit"

    if champ_name == None or role == None:
        return f"""> **Usage**
        > `sum <Champ Name> <Role> <(Optional) Page Number>` """

    elif isinstance(num, int) and num > 5:
        return "Please pick a number between 1-5"

    else:
        if num == None:
            return runes_scrape(champ_name, role, 1)

        elif isinstance(num, int):
            return runes_scrape(champ_name, role, num)


def runes_scrape(champ_name, role, num):
    runes_page = f"https://na.op.gg/champion/{champ_name}/statistics/{role}/rune"

    html = urlopen(runes_page)
    soup = BeautifulSoup(html, features="html.parser")

    main_tree = []
    sec_tree = []
    extra_tree = []
    type_names = []

    for tbody in soup.find_all("tbody"):
        for tr in tbody.find_all("tr")[num - 1 : num]:
            for perk_trees in tr.find_all("div", class_="perk-page"):

                for perk_tree_type in perk_trees.find_all(
                    "div", class_="perk-page__item perk-page__item--mark"
                ):
                    title = perk_tree_type.findChild().get("title")
                    type_name = title[title.find("'>") + 2 : title.find("</b>")]
                    type_names.append(type_name)

                for perk_active in perk_trees.find_all("div"):
                    if "perk-page__item--active" in perk_active["class"]:
                        rune_name = perk_active.findChild().findChild().get("alt")
                        if len(main_tree) != 4:
                            main_tree.append(rune_name)
                        else:
                            sec_tree.append(rune_name)

            for extras_list in tr.find_all("div", class_="fragment-page"):
                for extra in extras_list.find_all("img"):
                    if "active" in extra["class"][0]:
                        title = extra.get("title")
                        extra_description = title[
                            title.find("<span>") + 6 : title.find("</span>")
                        ]
                        extra_name = extra.get("alt")
                        extra_tree.append([extra_name, extra_description])

    return runes_pretty(main_tree, sec_tree, extra_tree, type_names)


def runes_pretty(main_tree, sec_tree, extra_tree, type_names):
    try:
        return f"""> **{type_names[0]}**
        > {main_tree[0]}
        > {main_tree[1]}
        > {main_tree[2]}
        > {main_tree[3]}
        > **{type_names[1]}**
        > {sec_tree[0]}
        > {sec_tree[1]}
        > **Extras**
        > {extra_tree[0][0]} {extra_tree[0][1]}
        > {extra_tree[1][0]} {extra_tree[1][1]}
        > {extra_tree[2][0]} {extra_tree[2][1]}"""

    except IndexError:
        return "No runes found"
