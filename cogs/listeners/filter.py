import discord
from discord.ext import commands

class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.__contains__("discord.gg/"):
            await message.delete()
