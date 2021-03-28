def test_command(ctx, ext, lol_watcher, sum_name):
    if ext == None:
        return "hello world!"

    else:
        switcher = {
            "saymyname": saymyname,
            "bold": bold,
            "block": block,
            "colour": colour,
            "emoji": emoji,
            "lolsum": lolsum,
        }
        return switcher.get(ext, lambda: "Invalid arg")(ctx, ext, lol_watcher, sum_name)


def saymyname(ctx, ext, lol_watcher, sum_name):
    name = str(ctx.author).split("#")[0]
    return f"{name}"


def bold(ctx, ext, lol_watcher, sum_name):
    return "**hello world!**"


def block(ctx, ext, lol_watcher, sum_name):
    return """> This is hopefully a block
    > hello world!
    > **ok goodbye**
    > *just kidding!*
    > ok fr goodbye"""


def colour(ctx, ext, lol_watcher, sum_name):
    return """ ```ini\n[please be blue]```
this isnt blue :3"""


def emoji(ctx, ext, lol_watcher, sum_name):
    return ":scream: AHHHHHHHHHHH"


def lolsum(ctx, ext, lol_watcher, sum_name):
    if sum_name != None:
        my_user = lol_watcher.summoner.by_name("na1", str(sum_name))
        return f"{my_user['name']} is level {my_user['summonerLevel']} "
    else:
        return "provide a username to search :blush:"
