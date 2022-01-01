import discord
import re
from discord.ext import commands
from config import cfg

class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 

    @commands.Cog.listener()
    async def on_message(self, message):
        if re.search("(?:https?://)?discord(?:app)?\.(?:com/invite|gg)/[a-zA-Z0-9]+/?", message.content) != None:
            embed = discord.Embed(
                color = discord.Colour.red(),
                title = "Invite link removed",
            )
            embed.set_author(name=message.author, icon_url=message.author.display_avatar)
            embed.add_field(name="Content", value=message.content, inline=False)
            embed.add_field(name="Channel", value=message.channel.mention, inline=False)
            embed.add_field(name="Message ID", value=message.id)
            embed.add_field(name="User ID", value=message.author.id)
            await message.author.guild.get_channel(cfg["PRIVATE_LOG_CHANNEL_ID"]).send(embed = embed)
            await message.delete()
