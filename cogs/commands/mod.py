import discord
from discord import member
from discord import message
from discord.ext import commands
from discord.commands import slash_command, Option
from config import cfg

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 

    @slash_command(name="kick", guild_ids=[cfg["GUILD_ID"]])
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: Option(discord.User, "User to kick"), reason: Option(str, "Reason of kick", required=False, default="No reason specified")):
        """Kick a specified user."""
        await ctx.guild.kick(user = user, reason = f"Kicked by {ctx.author}: {reason}")
        embed = discord.Embed()
        embed.color = 0xBF005F
        embed.title = "Kicked user."
        embed.description = f"`{user.name}#{user.discriminator}` was kicked\nReason: `{reason}`\nUser ID: `{user.id}`"
        embed.set_thumbnail(url = user.avatar.url)
        await ctx.respond(embed = embed)

    @slash_command(name="ban", guild_ids=[cfg["GUILD_ID"]])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: Option(discord.User, "User to ban"), reason: Option(str, "Reason of ban", required=False, default="No reason specified")):
        """Ban a specified user."""
        await ctx.guild.ban(user = user, delete_message_days = 0, reason = f"Banned by {ctx.author}: {reason}")
        embed = discord.Embed()
        embed.color = 0xBF005F
        embed.title = "Banned user."
        embed.description = f"`{user.name}#{user.discriminator}` was banned\nReason: `{reason}`\nUser ID: `{user.id}`"
        embed.set_thumbnail(url = user.avatar.url)
        await ctx.respond(embed = embed)

    @slash_command(name="unban", guild_ids=[cfg["GUILD_ID"]])
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, user: Option(discord.User, "User to unban"), reason: Option(str, "Reason of unban", required=False, default="No reason specified")):
        """Unban a specified user."""
        await ctx.guild.unban(user = user, reason = f"Unbanned by {ctx.author}: {reason}")
        embed = discord.Embed()
        embed.color = 0xBF005F
        embed.title = "Unbanned user."
        embed.description = f"`{user.name}#{user.discriminator}` was unbanned\nReason: `{reason}`\nUser ID: `{user.id}`"
        embed.set_thumbnail(url = user.avatar.url)
        await ctx.respond(embed = embed)
