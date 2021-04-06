from urllib.request import urlopen

from bs4 import BeautifulSoup
from data_structures.build_page import BuildPage

basic_page = "https://na.op.gg/{}/{}/statistics/{}/item"
aram_ver = 450
urf_ver = 900


def builds_command(champ_name, role):
    check = builds_check_input(champ_name, role)

    if check == True:
        if role.lower() == "aram":
            builds_page = basic_page.format("aram", champ_name, aram_ver)

        elif role.lower() == "urf":
            builds_page = basic_page.format("urf", champ_name, urf_ver)

        else:
            builds_page = basic_page.format("champion", champ_name, role)

        return builds_scrape(builds_page, champ_name, role)

    else:
        return check


def builds_scrape(builds_page, champ_name, role):
    html = urlopen(builds_page)
    soup = BeautifulSoup(html, features="html.parser")

    build = BuildPage(champ_name, role)

    ##MAIN ITEMS
    main_items_div = soup.find("div", class_="l-champion-statistics-content__main")

    current_box = 0
    for champ_box in main_items_div("div", class_="champion-box"):
        current_box += 1

        switcher = {
            1: lambda: build.core_build.extend(item_row_scrape(champ_box)),
            2: lambda: build.boots.append(single_item_scrape(champ_box)),
            3: lambda: build.starter_items.extend(item_row_scrape(champ_box)),
        }

        switcher.get(current_box, lambda: "Invalid arg")()

    ##EXTRA ITEMS
    extra_items_tbody = soup.find(
        "div", class_="l-champion-statistics-content__side"
    ).find("tbody")
    for row in extra_items_tbody.find_all("tr"):
        build.extra_items.append(single_item_scrape(row))

    return build.pretty_print()


def item_row_scrape(champ_box):
    try:
        main_ul = champ_box.find(
            "td",
            class_="champion-stats__table__cell champion-stats__table__cell--data",
        ).findChild("ul")

        item_list = []

        for li in main_ul.find_all("li", class_="champion-stats__list__item tip"):
            title = li.get("title")
            item_name = title[title.find("'>") + 2 : title.find("</b>")]
            item_cost = title[title.rfind("'>") + 2 : title.rfind("</span>")]

            item_list.append([item_name, item_cost])

        return item_list

    except AttributeError:
        return []


def single_item_scrape(champ_box):
    main_img = (
        champ_box.find(
            "td",
            class_="champion-stats__table__cell champion-stats__table__cell--data",
        )
        .findChild("div")
        .findChild("img")
    )
    title = main_img.get("title")

    item_name = title[title.find("'>") + 2 : title.find("</b>")]
    item_cost = title[title.rfind("'>") + 2 : title.rfind("</span>")]

    return [item_name, item_cost]


def builds_check_input(champ_name, role):
    list_of_roles = ["top", "mid", "bot", "adc", "support", "jungle", "aram", "urf"]

    if champ_name == None:
        return f"""> **Usage**
        > `sum <Champ Name> <Role>` """

    elif role == None or role not in list_of_roles:
        return f"""You need to provide a role. Possible options are:
  - 'top'
  - 'mid'
  - 'bot'/'adc'
  - 'support'
  - 'jungle'
  - 'aram'
  - 'urf'"""

    else:
        return True
