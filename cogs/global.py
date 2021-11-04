import json
import discord
import datetime
from random import randint
from discord.ext import commands


class Global(commands.Cog):
    '''<:farm_ogladi:859860008429813820> **Connect your server channel to the outside servers with ease!**'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def serverlink(self, ctx, channel):
        """Connect your server with global chats"""
        guild_id = ctx.message.guild.id
        channel_id = int(channel.strip('<>#'))

        with open('meow.json', 'r') as file:
            global_chat_data = json.load(file)
            new_global_chat = str(guild_id)

            # Existing global chat
            if new_global_chat in global_chat_data:
                await ctx.send('<:UV_No_Tick:853483191977115688> ┃ **Channel has already been added to global chat!**')

            # Add new global chat
            else:
                global_chat_data[new_global_chat] = channel_id
                with open('meow.json', 'w') as new_global_chat:
                    json.dump(global_chat_data, new_global_chat, indent=4)

                await ctx.send('<:UV_uppu:792060506982711376> ┃ **Channel has been added to global chat!**')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def serverunlink(self, ctx):
        """Disconnect the server from global chats"""
        guild_id = ctx.message.guild.id

        with open('meow.json', 'r') as file:
            global_chat_data = json.load(file)

        global_chat_data.pop(str(guild_id))

        # Update global chat
        with open('meow.json', 'w') as update_global_chat_file:
            json.dump(global_chat_data, update_global_chat_file, indent=4)

        await ctx.send('<:UV_uppu:792060506982711376> ┃ **Channel has been removed from global chat!**')

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if not message.content.startswith('!'):
                with open('meow.json', 'r') as file:
                    global_chat_data = json.load(file)

                channel_id = list(global_chat_data.values())

                # Message sender
                if message.channel.id in channel_id:

       
                    if not message.content:
                        return

                    # Message receiver
                    for ids in channel_id:
                        if message.channel.id != ids:
                            message_embed = discord.Embed(colour=randint(0, 0xce2167))

                            message_embed.timestamp = datetime.datetime.utcnow()
                            message_embed.set_author(icon_url=message.author.avatar_url, name=f'{message.author}')
                            message_embed.description = f'**`Said: {message.content}`**'
                            message_embed.set_footer(icon_url=message.guild.icon_url, text=message.guild.name)

                            await self.bot.get_channel(ids).send(f'> **{message.author} == > ** **`{message.content}`**')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def servers(self, ctx):
        """Shows the servers with global chats channel in a .JSON containing IDs"""
        guild_id = ctx.message.guild.id
      

        with open('meow.json', 'r') as file:
            global_chat_data = json.load(file)
            new_global_chat = str(guild_id)
            await ctx.send(f"**Following are the servers ids with respective Global Chat channels!**\n**Thanks y'all for connecting** <:farm_ogladi:859860008429813820>\n```py\n{global_chat_data}\n```")


def setup(bot):
    bot.add_cog(Global(bot))