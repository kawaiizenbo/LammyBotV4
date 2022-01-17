import discord

from cogs.commands.info import Info

from cogs.listeners.userjoinleave import UserJoinLeave
from cogs.listeners.filter import Filter
from cogs.listeners.logger import Logger

from config import cfg

description = """lammy bot v4"""

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = discord.Bot(intents = intents)

# Command Cogs
bot.add_cog(Info(bot))

# Listener Cogs
bot.add_cog(UserJoinLeave(bot))
bot.add_cog(Filter(bot))
bot.add_cog(Logger(bot))

# Events
@bot.event
async def on_ready():
    print("Lammy Bot V4 init")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

bot.run(cfg["TOKEN"])
