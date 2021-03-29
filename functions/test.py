def test_command(ctx, ext, lol_watcher, sum_name):
    if ext == None:
        return "hello world!"

    else:
        switcher = {
            "saymyname": lambda: saymyname(ctx),
            "bold": lambda: bold(),
            "block": lambda: block(),
            "colour": lambda: colour(),
            "emoji": lambda: emoji(),
            "lolsum": lambda: lolsum(lol_watcher, sum_name),
        }
        return switcher.get(ext, lambda: "Invalid arg")()


def saymyname(ctx):
    name = str(ctx.author).split("#")[0]
    return f"{name}"


def bold():
    return "**hello world!**"


def block():
    return """> This is hopefully a block
    > hello world!
    > **ok goodbye**
    > *just kidding!*
    > ok fr goodbye"""


def colour():
    return """ ```ini\n[please be blue]```
this isnt blue :3"""


def emoji():
    return ":scream: AHHHHHHHHHHH"


def lolsum(lol_watcher, sum_name):
    if sum_name != None:
        my_user = lol_watcher.summoner.by_name("na1", str(sum_name))
        return f"{my_user['name']} is level {my_user['summonerLevel']} "
    else:
        return "provide a username to search :blush:"
