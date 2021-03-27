def test_command(ctx, ext, lol_watcher, sum_name):
    if ext == None:
        return "hello world!"

    if ext == "saymyname":
        name = str(ctx.author).split("#")[0]
        return f"{name}"

    if ext == "bold":
        return "**hello world!**"

    if ext == "block":
        return """> This is hopefully a block
        > hello world!
        > **ok goodbye**
        > *just kidding!*
        > ok fr goodbye"""

    if ext == "colour":
        return """ ```ini\n[please be blue]```
this isnt blue :3"""

    if ext == "emoji":
        return ":scream: AHHHHHHHHHHH"

    if ext == "lolsum":
        if sum_name != None:
            my_user = lol_watcher.summoner.by_name("na1", str(sum_name))
            return f"{my_user['name']} is level {my_user['summonerLevel']} "
        else:
            return "provide a username to search :blush:"
