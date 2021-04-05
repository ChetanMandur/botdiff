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
            basic_page = basic_page.format("aram", champ_name, aram_ver)

        elif role.lower() == "urf":
            basic_page = basic_page.format("urf", champ_name, urf_ver)

        else:
            builds_page = basic_page.format("champion", champ_name, role)

        return builds_scrape(builds_page, champ_name, role)

    else:
        return check


def builds_scrape(builds_page, champ_name, role):
    html = urlopen(builds_page)
    soup = BeautifulSoup(html, features="html.parser")

    build = BuildPage(champ_name, role)

    # Core Build
    cb_tbody = soup.find("div", class_="tabItem ChampionKeystoneRune-1").findChild(
        "tbody"
    )


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
