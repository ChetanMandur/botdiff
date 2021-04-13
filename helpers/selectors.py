OVERVIEW_QUEUE_BUTTON = {
    "all": "#left_champion_all > a",
    "solo": "#left_champion_solorank > a",
    "flex": "#left_champion_flexrank5v5 > a",
}

OVERVIEW_TABLE = {
    "all": "#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.Box.tabWrap.stats-box._recognized > div.Content.tabItems > div.MostChampionContent.tabItem.overview-stats--all > div",
    "solo": "#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.Box.tabWrap.stats-box._recognized > div.Content.tabItems > div.tabItem.overview-stats--soloranked > div",
    "flex": "#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.Box.tabWrap.stats-box._recognized > div.Content.tabItems > div.tabItem.overview-stats--flexranked5v5 > div",
}

OVERVIEW_STATS = {
    "name": "div.ChampionInfo > div.ChampionName > a",
    "winrate": "div.Played > div.WinRatio.normal.tip.tpd-delegation-uid-1",
    "kda": "div.PersonalKDA > div.KDA.green.tip > span.KDA",
    "creepScore": "div.ChampionInfo > div.ChampionMinionKill.tip.tpd-delegation-uid-1",
    "played": "div.Played > div.Title",
}
