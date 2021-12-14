import random

import discord
from discord.ext import commands

from cogs.commands.misc import Misc
from cogs.commands.mod import Mod
from cogs.commands.info import Info

description = """lammy bot v4"""

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)

bot.add_cog(Misc(bot))
bot.add_cog(Mod(bot))
bot.add_cog(Info(bot))

# Events
@bot.event
async def on_ready():
    print("Lammy Bot V4 init")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.event
async def on_member_join(member: discord.Member):
    server = member.guild

    await server.get_channel(919807935641710613).send(f"Welcome, `{member.name}`")
    await member.add_roles(server.get_role(913237446915948554), reason="Autorole")

@bot.event
async def on_member_remove(member: discord.Member):
    server = member.guild

    await server.get_channel(919807935641710613).send(f"Goodbye, `{member.name}`")

bot.run(open("TOKEN.txt", "r").read())