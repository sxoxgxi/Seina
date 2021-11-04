
import discord
import asyncio, aiohttp
import json

from jikanpy import AioJikan
from discord.ext import commands

class Anime(commands.Cog):

  def __init__(self, bot):
    self.client = bot


  @commands.command()
  async def account(self, ctx, message):
    #loop = asyncio.get_event_loop()
    aio_jikan = AioJikan()
    
    if message == '':
      embed = discord.Embed(title="", description="<:UV_No_Tick:853483191977115688> **┃ Please provide username**", color=0xce2167)
      await ctx.channel.send(embed=embed)
      
      return

    async with ctx.channel.typing():

      try:
        user = await aio_jikan.user(username = message)

      except:
        embed = discord.Embed(title="", description="<a:UV_ghanta:905498296452263948> ┃ User not found!", color=0xce2167)
        await ctx.channel.send(embed=embed)
        
        return

      url = user.get('url')
      username = user.get('username')
      anime = user.get('anime_stats')

      if user.get('image_url') == None:
        img = 'https://cdn.discordapp.com/avatars/755703966720983050/8cb59073b3f240634b5aa19224bbfdc1.png?size=2048'

      else:
        img = user.get('image_url')

      days = anime.get('days_watched')
      avg_score = anime.get('mean_score')
      watching = anime.get('watching')
      completed = anime.get('completed')
      hold = anime.get('on_hold')
      dropped = anime.get('dropped')
      plan = anime.get('plan_to_watch')
      total = anime.get('total_entries')
      num_ep = anime.get('episodes_watched')

      embed = discord.Embed(
        title = '**' + username + '**',
        colour = 0xce2167,
        url = url
      )


      embed.set_thumbnail(url = img)
      embed.add_field(name = 'Days watched', value = days)
      embed.add_field(name = 'Episodes Watched', value = num_ep)
      embed.add_field(name = 'Average Score', value = avg_score)
      embed.add_field(name = 'Total number of shows', value = total)
      embed.add_field(name = 'Watching', value = watching)
      embed.add_field(name = 'Completed', value = completed)
      embed.add_field(name = 'Plan to Watch', value = plan)
      embed.add_field(name = 'Dropped', value = dropped)
      embed.add_field(name = 'On hold', value = hold)

      await aio_jikan.close()

      await ctx.send(embed = embed)
      return




  @commands.command()
  async def schedule(self, ctx, day = ''):
    #loop = asyncio.get_event_loop()
    aio_jikan = AioJikan()

    shows = {
      'm':'monday',
      't':'tuesday',
      'w':'wednesday',
      'th':'thursday',
      'f':'friday',
      's':'saturday',
      'su':'sunday'
    }

    if day == '':
      async with ctx.channel.typing():
        scheduled = await aio_jikan.schedule()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        embed = discord.Embed(
          title = 'This week anime schedule',
          colour = 0xce2167
        )

        for x in range(7):
          hr = scheduled.get(days[x])
          date = days[x]
          sch = hr[0]
          title = sch.get('title')
          score = sch.get('score')

          embed.add_field(name = date.capitalize(), value = title + '\nScore :: ' + str(score), inline = False)
  

        await ctx.send(embed = embed)
        await aio_jikan.close()
        return

    elif day == 'days':
      async with ctx.channel.typing():
        desc = ''

        for x in shows:
          desc += x + ' : ' + shows[x] + '\n'
          print(desc)

        embed = discord.Embed(
          title = 'Days',
          colour = 0xce2167,
          description = desc
        )
        await ctx.send(embed = embed)
        return

    elif day in shows:
      async with ctx.channel.typing():
        scheduled = await aio_jikan.schedule(shows[day])
    
        embed = discord.Embed(
          title = shows[day].capitalize(),
          colour = 0xce2167
        )

        hr = scheduled.get(shows[day])

        if len(hr) > 7:
          for x in range(7):
            sch = hr[x]
            title = sch.get('title')
            score = sch.get('score')

            embed.add_field(name = title, value = 'Score :: ' + str(score), inline = False)

        else:
          for x in range(len(hr)):
            sch = hr[x]
            title = sch.get('title')
            score = sch.get('score')

            embed.add_field(name = title, value = 'Score :: ' + str(score), inline = False)

        await ctx.send(embed = embed)
        await aio_jikan.close()
        return

    else:
      embed = discord.Embed(title="<a:UV_ghanta:905498296452263948> | Provide valid day", description=">>> **su :: Sunday\nm :: Monday\nt :: Tuesday\nw :: Wednesday\nth :: Thursday\nf :: Friday\ns :: Saturday**", color=0xce2167)
      await ctx.send(embed=embed)
      
      return



def setup(bot):
  bot.add_cog(Anime(bot))