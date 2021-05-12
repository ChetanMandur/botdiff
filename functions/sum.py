from urllib.request import urlopen

from bs4 import BeautifulSoup


def sum_command(summoner, ext):
    basic_page = "https://na.op.gg/summoner/userName={}"
    summonerpage = basic_page.format(summoner)
    html = urlopen(summonerpage)
    soup = BeautifulSoup(html, feature="html.parser")
    summoner_SoloRank = soup.find("div", class_="TierRank")
    summoner_FlexRank = soup.find("div", class_="sub-tier__rank-tier")
    sum_level = soup.find("span", class_="Level tip tpd-delegation-uid-1")

    if summoner == None:
        return f""" **Usage**
        >sum <UserName> <Command>` """

    if ext == None:
        return f""" **Summoner Name** = {summoner}
        **Summoner Level** = {sum_level.get_text()}
        **Summoner Solo Rank** = {summoner_SoloRank.get_text()}
        **Summoner Flex Rank = {summoner_FlexRank.get_text()}
        """

    else:
        switcher = {
            "solo": lambda: soloStat(summoner, summoner_SoloRank, soup),
            "flex": lambda: flexStat(summoner, summoner_FlexRank, soup),
        }
        return switcher.get(ext, lambda: "Invalid command")()


def soloStat(summoner, rank, soup):
    solo_Winrate = soup.find("span", class_="winratio")
    solo_Wins = soup.find("span", class_="wins")
    solo_Losses = soup.find("span", class_="losses")
    solo_Points = soup.find("span", class_="LeaguePoints")
    solo_LeagueName = soup.find("div", class_="LeagueName")

    return f"""**Solo Rank** = {rank.get_text()}
    **League Points** = {solo_Points.get_text()}
    **League Name** = {solo_LeagueName.get_text()}
    **Wins** = {solo_Wins.get_text()}
    **Losses** = {solo_Losses.get_text()}
    **Winrate** = {solo_Winrate.get_text()}
    """


def flexStat(summoner, rank, soup):
    flex_Winrate = soup.find("div", class_="sub-tier__rank-tier")
    flex_WinsLosses = soup.find("span", class_="sub-tier__gray-text")
    flex_Points = soup.find("div", class_="sub-tier__gray-text")
    return f""" **Flex Rank** = {rank.get_text()}
    **Flex Points** = {flex_Points.get_text()}
    **Flex Winrate** = {flex_Winrate.get_text()}
    **Flex Wins** = {flex_WinsLosses.get_text().strip().split(' ')[0]}
    **Flex Losses** = {flex_WinsLosses.gettext().strip().split(' ')[1]}
    """
