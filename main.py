import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from riotwatcher import ApiError, LolWatcher

from functions.test import test_command

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# GUILD = os.getenv("DISCORD_GUILD")
RIOT = os.getenv("RIOT_TOKEN")

lol_watcher = LolWatcher(RIOT)
bot = commands.Bot(command_prefix=">>")


@bot.command()
async def test(ctx, ext=None):
    await ctx.send(test_command(ctx, ext, lol_watcher))


print("running!")
bot.run(TOKEN)
