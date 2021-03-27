import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from functions.test import test_command

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix=">>")


@bot.command()
async def test(ctx):
    await ctx.send(test_command())


print("running!")
bot.run(TOKEN)
