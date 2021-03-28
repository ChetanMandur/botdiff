def level(lol_watcher, ctx, sum_name, ext):
    my_user = lol_watcher.summoner.by_name("na1", str(sum_name))
    return f"This user is level {my_user['summonerLevel']}"


def id(lol_watcher, ctx, sum_name, ext):
    my_user = lol_watcher.summoner.by_name("na1", str(sum_name))
    return f"""> **Username:** {my_user['name']}
    > **ID:** {my_user['id']}
    > **Account ID:** {my_user['accountId']}  """


def sum_command(lol_watcher, ctx, sum_name, ext):
    if sum_name == None:
        return "Please provide a username"

    if ext == None:
        return "username only given"

    else:
        switcher = {
            "level": level,
            "id": id,
        }
        return switcher.get(ext, lambda: "Invalid arg")(lol_watcher, ctx, sum_name, ext)
