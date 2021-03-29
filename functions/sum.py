import helpers.riot_helper as riot_helper


def sum_command(lol_watcher, ctx, sum_name, ext):
    if sum_name == None:
        return f"""> **Usage**
        > `sum <UserName> <Command>` """

    user = lol_watcher.summoner.by_name("na1", str(sum_name))
    if ext == None:
        return f"""> **Username:** {user['name']}
        > **Level**: {user['summonerLevel']}
        > **ID:** {user['id']}
        > **Account ID:** {user['accountId']}  """

    else:
        switcher = {
            "level": level,
            "id": id,
            "rankedstat": rankedstat,
        }
        return switcher.get(ext, lambda: "Invalid arg")(
            lol_watcher, ctx, sum_name, ext, user
        )


def level(lol_watcher, ctx, sum_name, ext, user):
    return f"This user is level {user['summonerLevel']}"


def id(lol_watcher, ctx, sum_name, ext, user):
    return f"""> **Username:** {user['name']}
    > **ID:** {user['id']}
    > **Account ID:** {user['accountId']}  """


def rankedstat(lol_watcher, ctx, sum_name, ext, user):
    ranked_stat = lol_watcher.league.by_summoner("na1", user["id"])[0]

    tier = ranked_stat["tier"]
    rank = ranked_stat["rank"]
    queue_type = riot_helper.queue_type_clean(ranked_stat["queueType"])

    wins = ranked_stat["wins"]
    losses = ranked_stat["losses"]

    lp = ranked_stat["leaguePoints"]
    hotstreak = ranked_stat["hotStreak"]

    return f"""> **Rank:** {tier} {rank} ({queue_type})
    > **Win/Loss:** {wins}/{losses}
    > **League Point:** {lp}
    > **Hotstreak?:** {hotstreak}"""
