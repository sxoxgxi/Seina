# some sec c content 

from discord.ext import commands
import asyncio
import discord
import nekos
 
class NSFW(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gif(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('nsfw_neko_gif')))
      embed.set_author(name="Gif", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)

    @commands.command()
    async def feet(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('feet')))
      embed.set_author(name="Feet", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)

    @commands.command()
    async def cum(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('cum')))
      embed.set_author(name="Cumming!", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)

    @commands.command()
    async def hentai(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('random_hentai_gif')))
      embed.set_author(name="Hentai!", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)

      

    @commands.command()
    async def anal(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('anal')))
      embed.set_author(name="Anal", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      
 
    @commands.command()
    async def bj(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('bj')))
      embed.set_author(name="Blowjob", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      

    @commands.command()
    async def lewd(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('lewd')))
      embed.set_author(name="Lewd", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      

    @commands.command()
    async def yuri(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('yuri')))
      embed.set_author(name="Yuri", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      

    @commands.command()
    async def smug(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description=f"{ctx.message.author.mention} smugs!", color=0xce2167)
      embed.set_image(url=(nekos.img('smug')))
      embed.set_author(name="Smuggging!", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      

    @commands.command()
    async def getavatar(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('avatar')))
      embed.set_author(name="A avatar for horny peep", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      

    @commands.command()
    async def gasm(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('gasm')))
      embed.set_author(name="Gasm", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      

    @commands.command()
    async def boobs(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('boobs')))
      embed.set_author(name="Booba", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      

    @commands.command()
    async def classic(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('classic')))
      embed.set_author(name="Classy", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      
 
      

    @commands.command()
    async def pussy(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('pussy')))
      embed.set_author(name="Pussy", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      

    @commands.command()
    async def baka(self, ctx):
      if not ctx.channel.is_nsfw():
        embed = discord.Embed(description = f"{ctx.message.author}, Horny Baka! Find a nsfw channel first <:UV_uwuUP:906757302143569921>", colour = 0xce2167)
        await ctx.send(embed=embed)
        return
      embed=discord.Embed(title="Source: nekos.life", url="https://nekos.life/", description="", color=0xce2167)
      embed.set_image(url=(nekos.img('baka')))
      embed.set_author(name="Baakaa!", url='https://ukatoverse.com/discord')
      await ctx.send(embed=embed)
      

def setup(bot):
    bot.add_cog(NSFW(bot))   
 
 
