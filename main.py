import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


from functions.sum import sum_command
from functions.test import test_command

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix=">>")


@bot.command()
async def test(ctx, ext=None, sum_name=None):
    await ctx.send(test_command(ctx, ext, sum_name))


@bot.command()
async def sum(ctx, sum_name=None, ext=None):
    await ctx.send(sum_command(ctx, sum_name, ext))


print("running!")
bot.run(TOKEN)
