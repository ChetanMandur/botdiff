def test_command(ctx, ext, lol_watcher):
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
        my_user = lol_watcher.summoner.by_name("na1", "HideOnTurban")
        return f"{my_user['name']} is level {my_user['summonerLevel']} "
