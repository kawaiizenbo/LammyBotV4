import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 

    @commands.command(name="kick")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.User, reason: str = "No reason specified"):
        """Kick a specified user."""
        await ctx.guild.kick(user = user, reason = f"Kicked by {ctx.message.author.name}#{ctx.message.author.discriminator}: {reason}")
        embed = discord.Embed()
        embed.color = discord.Colour.red()
        embed.title = "Kicked user."
        embed.description = f"`{user.name}#{user.discriminator}` was kicked\nReason: `{reason}`\nUser ID: `{user.id}`"
        embed.set_thumbnail(url = user.avatar.url)
        await ctx.send(embed = embed)

    @commands.command(name="ban")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.User, reason: str = "No reason specified"):
        """Ban a specified user."""
        await ctx.guild.ban(user = user, delete_message_days = 0, reason = f"Banned by {ctx.message.author.name}#{ctx.message.author.discriminator}: {reason}")
        embed = discord.Embed()
        embed.color = discord.Colour.red()
        embed.title = "Banned user."
        embed.description = f"`{user.name}#{user.discriminator}` was banned\nReason: `{reason}`\nUser ID: `{user.id}`"
        embed.set_thumbnail(url = user.avatar.url)
        await ctx.send(embed = embed)

    @commands.command(name="unban")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, user: discord.User, reason: str = "No reason specified"):
        """Unban a specified user."""
        await ctx.guild.unban(user = user, reason = f"Unbanned by {ctx.message.author.name}#{ctx.message.author.discriminator}: {reason}")
        embed = discord.Embed()
        embed.color = discord.Colour.red()
        embed.title = "Unbanned user."
        embed.description = f"`{user.name}#{user.discriminator}` was unbanned\nReason: `{reason}`\nUser ID: `{user.id}`"
        embed.set_thumbnail(url = user.avatar.url)
        await ctx.send(embed = embed)
