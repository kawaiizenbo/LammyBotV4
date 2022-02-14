import discord
from discord.ext import commands
from config import cfg

class UserJoinLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        server = member.guild
        embed = discord.Embed(
            color = 0xBF005F,
            description = f"Welcome, {member.mention}"
        )
        await server.get_channel(cfg["WELCOME_GOODBYE_CHANNEL_ID"]).send(embed = embed)
        await member.add_roles(server.get_role(cfg["AUTOROLE_ID"]), reason="Autorole")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        server = member.guild
        embed = discord.Embed(
            color = 0xBF005F,
            description = f"Goodbye, {member.mention}"
        )
        await server.get_channel(cfg["WELCOME_GOODBYE_CHANNEL_ID"]).send(embed = embed)
