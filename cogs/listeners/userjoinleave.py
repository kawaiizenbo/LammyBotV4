import discord
from discord.ext import commands

class UserJoinLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        server = member.guild

        await server.get_channel(919807935641710613).send(f"Welcome, `{member.name}`")
        await member.add_roles(server.get_role(913237446915948554), reason="Autorole")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        server = member.guild

        await server.get_channel(919807935641710613).send(f"Goodbye, `{member.name}`")
