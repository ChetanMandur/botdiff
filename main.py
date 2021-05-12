import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from requests.exceptions import HTTPError
from riotwatcher import ApiError, LolWatcher

import helpers.riot_helper as riot_helper
from functions.builds import builds_command
from functions.runes import runes_command
from functions.sum import sum_command
from functions.test import test_command
from functions.topchampions import topchampions_command

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
    try:
        await ctx.send(sum_command(lol_watcher, ctx, sum_name, ext))
    except HTTPError as e:
        await ctx.send(riot_helper.error_handling(e))


@bot.command()
async def runes(ctx, champ_name=None, role=None, num=None):
    await ctx.send(runes_command(bot, champ_name, role, num))


@bot.command()
async def builds(ctx, champ_name=None, role=None):
    await ctx.send(builds_command(champ_name, role))

@bot.command()
async def top(ctx, sum_name=None, ext=None):
    await ctx.send(topchampions_command(ctx, sum_name, ext))


@bot.command()
async def top(ctx, sum_name=None, ext=None):
    await ctx.send(topchampions_command(sum_name, ext))


print("running!")
bot.run(TOKEN)
