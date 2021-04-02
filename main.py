import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from riotwatcher import ApiError, LolWatcher

from functions.sum import sum_command
from functions.test import test_command

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# GUILD = os.getenv("DISCORD_GUILD")
RIOT = os.getenv("RIOT_TOKEN")

lol_watcher = LolWatcher(RIOT)
bot = commands.Bot(command_prefix=">>")


@bot.command()
async def test(ctx, ext=None, sum_name=None):
    await ctx.send(test_command(ctx, ext, lol_watcher, sum_name))


@bot.command()
async def sum(ctx, sum_name=None, ext=None):
    await ctx.send(sum_command(lol_watcher, ctx, sum_name, ext))


print("running!")
bot.run(TOKEN)
