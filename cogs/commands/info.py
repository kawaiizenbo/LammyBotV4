import discord
import json
import datetime, time

from discord.commands import slash_command, Option
from discord.ext import commands
from config import cfg

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 
        global startTime
        startTime = time.time()

    @slash_command(name="userinfo", guild_ids=[cfg["GUILD_ID"]])
    async def userinfo(self, ctx, member: Option(discord.Member, "User to see info of", required=False)):
        """Gets user info."""
        user = member or ctx.author
        cd: str = user.created_at.strftime("%Y %b %d %H:%M:%S")
        jd: str = user.joined_at.strftime("%Y %b %d %H:%M:%S")
        froles: str = ""
        for r in user.roles:
            if r.name == "@everyone":
                continue
            froles += f"{r.mention} "
        _permissions_dict = dict(iter(user.guild_permissions))
        permissions = (
            ", ".join(
            [
            (permission.replace("_", " ").title())
            for permission in _permissions_dict
            if _permissions_dict[permission]
            ]
        )
        if not _permissions_dict["administrator"]
        else "Administrator"
        )
        if user == ctx.guild.owner:
            permissions = "Server Owner"
        embed = discord.Embed(
            color = 0xBF005F,
            title = f"User info",
        )
        embed.set_author(name=user, icon_url=user.display_avatar)
        embed.add_field(name="User ID", value=f"`{user.id}`", inline=False)
        embed.add_field(name="Creation Date", value=f"`{cd}`")
        embed.add_field(name="Join Date", value=f"`{jd}`")
        embed.add_field(name="Roles", value=froles, inline=False)
        embed.add_field(name="Permissions", value=permissions, inline=False)
        await ctx.respond(embed = embed)

    @slash_command(name="riitag", guild_ids=[cfg["GUILD_ID"]], required=False)
    async def riitag(self, ctx, member: Option(discord.Member, "User to see RiiTag of")):
        """Gets user's RiiTag"""
        user = member or ctx.author
        embed = discord.Embed(
            color = 0xBF005F,
            title = f"RiiTag",
        )
        embed.set_author(name=user, icon_url=user.display_avatar)
        embed.set_image(url=f"https://tag.rc24.xyz/{user.id}/tag.max.png")
        await ctx.respond(embed = embed)

    @slash_command(name="about", guild_ids=[cfg["GUILD_ID"]])
    async def about(self, ctx):
        """Get bot info."""
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        embed = discord.Embed(
            color = 0xBF005F,
            title = "Bot info",
        )
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.display_avatar)
        embed.add_field(name="Uptime", value=uptime)
        embed.add_field(name="Latency", value=round(self.bot.latency*1000, 1))
        embed.add_field(name="Pycord Version", value=discord.__version__)
        await ctx.respond(embed = embed)
    
    @slash_command(name="kill", guild_ids=[cfg["GUILD_ID"]])
    async def about(self, ctx):
        """stop bot (bot owner only)"""
        if ctx.author.id != self.bot.owner_id:
            await ctx.respond("You arent allowed to do that.")
        else:
            await ctx.respond("Lammy fell out of this world.")
            exit(0)

    @slash_command(name="source", guild_ids=[cfg["GUILD_ID"]])
    async def about(self, ctx):
        """show bot source"""
        await ctx.respond("<https://github.com/kawaiizenbo/LammyBotV4>")

    @slash_command(name="tnt", guild_ids=[cfg["GUILD_ID"]])
    async def tnt(self, ctx):
        """dumb."""
        await ctx.respond(f"BOOOOOOOOOOOM!!!\n\n\n\n{ctx.user.mention} you died by an explosion\n\n\n\nThe WALMART is on fire\n\n\n\n{ctx.user.mention} you blew up {ctx.guild.name}")
