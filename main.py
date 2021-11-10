import discord
from os import listdir
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import os
import asyncio

from webserver import keep_alive

keep_alive()



def get_prefix(bot, message):

	if not isinstance(message.guild, discord.Guild):
		
		return '!'

	return ['!', '<@855532968349270026>]


bot = commands.Bot(command_prefix=get_prefix, description="It's not because I like u or anything")

if __name__=='__main__':
	"""Loads the cogs from the `./cogs` folder
		"""
	for cog in listdir('./cogs'):
		if cog.endswith('.py') == True:
			bot.load_extension(f'cogs.{cog[:-3]}')

@bot.event
async def on_ready():
    print ("Bot online!")
    await bot.change_presence(activity=discord.Streaming(name="Please don't make me think about life", url="https://www.twitch.tv/Twitch"))
    channel = bot.get_channel(902743993408954458)
    
    embed = discord.Embed(title="<:emoji_23:903181135016787978> Bot Booted Successfully", description=f'<a:online:859859291586822154> **I have been updated and am now alive again!\n<a:DA_loveheart:862411473632755764> Heartbeat = > {round(bot.latency * 1000)} bpm!**', color=0xce2167)
    await channel.send(embed=embed)
    

@bot.command(aliases=['av'])
async def avatar(ctx, user: discord.Member=None):
    """Displays users avatar."""
    if not user:
        embed = discord.Embed(color=0xce2167)
        embed = discord.Embed(title="View full image | Deleting in <a:UV_60seks:905498380854239254>", url=ctx.message.author.avatar_url, color=0xce2167)
        embed.set_image(url=ctx.message.author.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)      
        await ctx.send(embed=embed, delete_after=60)
        await asyncio.sleep(60)
        await ctx.message.delete()
		    
    else:
        embed = discord.Embed(color=0xce2167)
        embed = discord.Embed(title="View full image | Deleting in <a:UV_60seks:905498380854239254>", url=user.avatar_url, color=0xce2167)
        embed.set_image(url=user.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed, delete_after=60) 
        await asyncio.sleep(60)
        await ctx.message.delete()

@bot.command()
async def invite(ctx):
        embed = discord.Embed(title = "Invite Link", description = "[Click me](https://discord.com/oauth2/authorize?client_id=855532968349270026&permissions=536835128567&scope=applications.commands%20bot)", color = ctx.author.color)
        
        
        await ctx.send(embed = embed)  

@bot.command()
async def alive(ctx):
	"""This sends a greet!
	"""
	await ctx.send(f'Hello {ctx.message.author.mention}!')
	#The bot send a message on the channel that is being invoked in and mention the invoker.
@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            
            embed = discord.Embed(title="__Hey eveveryone,__", description='Thank your for inviting me to this amazing server!\nI am here to assist you. You can either send me a private message or invoke my commands in the correct channels.**\n\n**Try, for example, to get help send **`!help`** to me, or type it in **correct bot channel** to see what I can do for you.\nIf any suggestions or message to the developer then use **`!contactDev [message]`**\n\nThank you! <a:UV_hearts:857218865377443840>.', color=0xce2167)
            await channel.send(embed=embed)
            
            break

@bot.event
async def on_command(ctx):
    channel = bot.get_channel(902743993408954458)
    server = ctx.guild.name
    user = ctx.author
    command = ctx.command
    
    embed = discord.Embed(title="Command Execution Logging", description="**{}** used `{}` in **{}**".format(user, command, server), color=0xce2167)
    await channel.send(embed=embed)



bot.run(os.getenv("TOKEN"))#Runs the bot 
