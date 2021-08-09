from urllib.request import urlopen

from bs4 import BeautifulSoup
from data_structures.build_page import BuildPage

basic_page = "https://na.op.gg/{}/{}/statistics/{}/skill"
aram_ver = 450
urf_ver = 900


def skillbuilds_command(champ_name, role):
    check = skillbuilds_check_input(champ_name, role)

    if check == True:
        if role.lower() == "aram":
            builds_page = basic_page.format("aram", champ_name, aram_ver)

        elif role.lower() == "urf":
            builds_page = basic_page.format("urf", champ_name, urf_ver)

        else:
            builds_page = basic_page.format("champion", champ_name, role)

        return skillbuilds_scrape(builds_page, champ_name, role)

    else:
        return check


def skillbuilds_scrape(builds_page, champ_name, role):
    html = urlopen(builds_page)
    soup = BeautifulSoup(html, features="html.parser")
    main_skill_table = soup.find("table", class_="champion-skill-build__table")

    skills_list = []

    for td in main_skill_table.find_all("td"):
        if len(td.find_all("span")) == 0:
            text = td.renderContents().strip()

        else:
            text = td.find("span").renderContents().strip()

        skills_list.append(text.decode("utf-8"))

    return skillbuilds_format(skills_list, champ_name, role)


def skillbuilds_format(skills_list, champ_name, role):
    text = f"> __**{champ_name.upper()} ({role.upper()})**__ \n"
    for i in range(15):
        text += f"> **{i+1}:** {skills_list[i]} \n"

    return text


# This is just a messy attempt in making a horizontal table
# Turns out weird since it kept getting misaligned
#     return """
# > __**{} ({})**__
# > | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
# > | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |
# """.format(
#         champ_name.upper(),
#         role.upper(),
#         skills_list[0],
#         skills_list[1],
#         skills_list[2],
#         skills_list[3],
#         skills_list[4],
#         skills_list[5],
#         skills_list[6],
#         skills_list[7],
#         skills_list[8],
#         skills_list[9],
#         skills_list[10],
#         skills_list[11],
#         skills_list[12],
#         skills_list[13],
#         skills_list[14],
#     )


def skillbuilds_check_input(champ_name, role):
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
