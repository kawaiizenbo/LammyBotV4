import discord
from discord import embeds
from discord.ext import commands
from config import cfg

class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
        embed = discord.Embed(
            color = discord.Colour.yellow(),
            title = "Message edited",
        )
        embed.set_author(name=before.author, icon_url=before.author.display_avatar)
        embed.add_field(name="Before", value=before.content, inline=False)
        embed.add_field(name="After", value=after.content, inline=False)
        embed.add_field(name="Channel", value=before.channel.mention, inline=False)
        embed.add_field(name="Message ID", value=before.id)
        embed.add_field(name="User ID", value=before.author.id)
        await before.author.guild.get_channel(cfg["PRIVATE_LOG_CHANNEL_ID"]).send(embed = embed)

    @commands.Cog.listener()
    async def on_raw_message_delete(self, cache: discord.RawMessageDeleteEvent) -> None:
        message = cache.cached_message
        embed = discord.Embed(
            color = discord.Colour.red(),
            title = "Message deleted",
        )
        embed.set_author(name=message.author, icon_url=message.author.display_avatar)
        embed.add_field(name="Content", value=message.content, inline=False)
        embed.add_field(name="Channel", value=message.channel.mention, inline=False)
        embed.add_field(name="Message ID", value=message.id)
        embed.add_field(name="User ID", value=message.author.id)
        await message.author.guild.get_channel(cfg["PRIVATE_LOG_CHANNEL_ID"]).send(embed = embed)
