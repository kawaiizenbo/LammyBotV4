import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        """Gets user info."""
        embed = discord.Embed()
        embed.color = member.color
        embed.title = f"{member.name}#{member.discriminator}"
        embed.description = f"User ID: {member.id}\nCreation Date: {member.created_at}\nJoin Date: {member.joined_at}"
        await ctx.send(embed = embed)