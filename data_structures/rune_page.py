import discord


class RunePage:
    def __init__(self, champ, role):
        self.champ_searched = champ
        self.role_searched = role
        self.main_tree = []
        self.sec_tree = []
        self.shards_tree = []
        self.type_names = []

    def pretty_print(self, bot):
        try:
            return f"""> __**{self.champ_searched.upper()} ({self.role_searched.upper()})**__
                > **{self.runes_emoji(self.type_names[0], bot)}**
                {self.pretty_tree_print(self.main_tree,bot, True)}
                > 
                > **{self.runes_emoji(self.type_names[1], bot)}**
                {self.pretty_tree_print(self.sec_tree,bot, True)}
                > 
                > **Shards**
                {self.pretty_tree_print(self.shards_tree,bot, False)}"""

        except IndexError:
            return "No runes found"

    def pretty_tree_print(self, tree_list, bot, rune_tree):
        output = ""
        item_count = 0
        for item in tree_list:
            if item_count > 0:
                output = output + "\n"
            if rune_tree:
                new_item = f"> {self.runes_emoji(item,bot)}"
                output = output + new_item
            else:
                new_item = f"> {self.shards_emoji(item,bot)}"
                output = output + new_item
            item_count += 1

        return output

    def runes_emoji(self, name, discord_bot):
        emoji_name = "Rune_" + name
        emoji_name = emoji_name.replace(" ", "_")
        emoji_name = emoji_name.replace(":", "")
        emoji_name = emoji_name.replace("'", "")
        emoji = discord.utils.get(discord_bot.emojis, name=emoji_name)
        if emoji != None:
            return f"{emoji} {name}"
        else:
            return f"{name}"

    def shards_emoji(self, shard, discord_bot):
        emoji_key_list = {
            "+9 Adaptive Force": "diamond",
            "+10% Attack Speed": "axe",
            "+8 Ability Haste": "time",
            "+6 Armor": "shield",
            "+8 Magic Resist": "circle",
            "+15-90 Health (based on level)": "heart",
        }
        shard_type = shard[0]
        shard_name = shard[1]

        emoji_name = emoji_key_list.get(shard_name)
        emoji = discord.utils.get(discord_bot.emojis, name=emoji_name)

        if emoji != None:
            return f"{emoji} {shard_type} {shard_name}"
        else:
            return f"{shard_type} {shard_name}"
