import datetime, time

import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 
        global startTime
        startTime = time.time()

    @commands.command()
    async def ping(self, ctx):
        """the classic game of no end."""
        embed = discord.Embed()
        embed.color = ctx.message.author.color
        embed.title = "🏓 pong!"
        embed.description = f"Took {round(self.bot.latency, 1)} ms"
        await ctx.send(embed = embed)

    @commands.command()
    async def uptime(self, ctx):
        """Check uptime of the bot."""
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        embed = discord.Embed()
        embed.color = ctx.message.author.color
        embed.title = "Bot uptime"
        embed.description = f"Uptime: {uptime}"
        await ctx.send(embed = embed)