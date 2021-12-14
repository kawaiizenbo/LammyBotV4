import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.User):
        """Kick a specified user."""
        await ctx.guild.kick(user = user, reason = f"Kicked by {ctx.message.author.name}#{ctx.message.author.discriminator}")
        embed = discord.Embed()
        embed.color = ctx.message.author.color
        embed.title = "Kicked user."
        embed.description = f"`{user.name}#{user.discriminator}` was kicked\nUser ID: `{user.id}`"
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.User):
        """Ban a specified user."""
        await ctx.guild.ban(user = user, delete_message_days = 0, reason = f"Banned by {ctx.message.author.name}#{ctx.message.author.discriminator}")
        embed = discord.Embed()
        embed.color = ctx.message.author.color
        embed.title = "Banned user."
        embed.description = f"`{user.name}#{user.discriminator}` was banned\nUser ID: `{user.id}`"
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, user: discord.User):
        """Unban a specified user."""
        await ctx.guild.unban(user = user, reason = f"Unbanned by {ctx.message.author.name}#{ctx.message.author.discriminator}")
        embed = discord.Embed()
        embed.color = ctx.message.author.color
        embed.title = "Unbanned user."
        embed.description = f"`{user.name}#{user.discriminator}` was unbanned\nUser ID: `{user.id}`"
        await ctx.send(embed = embed)
