import random

import discord
from discord.ext import commands

from cogs.commands.misc import Misc
from cogs.commands.mod import Mod
from cogs.commands.info import Info

from cogs.listeners.userjoinleave import UserJoinLeave
from cogs.listeners.filter import Filter

description = """lammy bot v4"""

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)

# Command Cogs
bot.add_cog(Misc(bot))
bot.add_cog(Mod(bot))
bot.add_cog(Info(bot))

# Listener Cogs
bot.add_cog(UserJoinLeave(bot))
bot.add_cog(Filter(bot))

# Events
@bot.event
async def on_ready():
    print("Lammy Bot V4 init")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

bot.run(open("TOKEN.txt", "r").read())
