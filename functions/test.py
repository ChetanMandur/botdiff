def test_command(ctx, ext):
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
