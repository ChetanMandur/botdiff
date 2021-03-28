def level(lol_watcher, ctx, sum_name, ext):
    user = lol_watcher.summoner.by_name("na1", str(sum_name))
    return f"This user is level {user['summonerLevel']}"


def id(lol_watcher, ctx, sum_name, ext):
    user = lol_watcher.summoner.by_name("na1", str(sum_name))
    return f"""> **Username:** {user['name']}
    > **ID:** {user['id']}
    > **Account ID:** {user['accountId']}  """


def sum_command(lol_watcher, ctx, sum_name, ext):
    if sum_name == None:
        return f"""> **Usage**
        > `sum <UserName> <Command>` """

    if ext == None:
        user = lol_watcher.summoner.by_name("na1", str(sum_name))
        return f"""> **Username:** {user['name']}
        > **Level**: {user['summonerLevel']}
        > **ID:** {user['id']}
        > **Account ID:** {user['accountId']}  """

    else:
        switcher = {
            "level": level,
            "id": id,
        }
        return switcher.get(ext, lambda: "Invalid arg")(lol_watcher, ctx, sum_name, ext)
