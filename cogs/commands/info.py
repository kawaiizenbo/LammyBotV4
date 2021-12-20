import discord

import datetime, time
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 
        global startTime
        startTime = time.time()

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, member: discord.Member = None):
        """Gets user info."""
        user = member or ctx.author
        cd: str = user.created_at.strftime("%Y %b %d %H:%M:%S")
        jd: str = user.joined_at.strftime("%Y %b %d %H:%M:%S")
        froles: str = ""
        for r in user.roles:
            if r.name == "@everyone":
                continue
            froles += f"<@&{r.id}> "
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
            color = discord.Colour.red(),
            title = f"User info",
        )
        embed.set_author(name=user, icon_url=user.display_avatar)
        embed.add_field(name="User ID", value=f"`{user.id}`", inline=False)
        embed.add_field(name="Creation Date", value=f"`{cd}`")
        embed.add_field(name="Join Date", value=f"`{jd}`")
        embed.add_field(name="Roles", value=froles, inline=False)
        embed.add_field(name="Permissions", value=permissions, inline=False)
        await ctx.send(embed = embed)

    @commands.command(name="about")
    async def about(self, ctx):
        """Get bot info."""
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        embed = discord.Embed(
            color = discord.Colour.red(),
            title = "Bot info",
        )
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.display_avatar)
        embed.add_field(name="Uptime", value=uptime)
        embed.add_field(name="Latency", value=round(self.bot.latency*1000, 1))
        embed.add_field(name="Pycord Version", value=discord.__version__)
        await ctx.send(embed = embed)
