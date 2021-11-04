from discord.ext import commands
import discord
import datetime
import wikipedia
from datetime import datetime, timedelta
from discord import AllowedMentions
import random
from googletrans import Translator
tl = Translator()
F = "🇫"
ongoing_respects = dict()

class Tools(commands.Cog):
    """**Some useful commands for your daily discording **<:farm_ogladi:859860008429813820>
    """
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def givef(self, ctx):
        """Spam that **F**
      Usage :: Reply to respect message with **`!givef`**"""

        reference = ctx.message.reference
        if reference:
            message = await ctx.fetch_message(id=reference.message_id)
            text = message.content
        

            message = await ctx.send(f"<a:emoji_14:903097354532556860> ┃ **React to pay respect!**\n            {text}")
            await message.add_reaction(F)
            ongoing_respects[message.id] = (text, set())
        else:
            embed = discord.Embed(title="<a:UV_ghanta:905498296452263948> | Invalid Usage", description="You did't reply to the `respect message`!", color=0xce2167)
            await ctx.reply(embed=embed)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):


        message = reaction.message
        channel = message.channel
        if user.bot: return

        if reaction.emoji != F: return

        if message.id not in ongoing_respects: return
        respects = ongoing_respects[message.id]
        if user.id in respects[1]: return

        respects[1].add(user.id)
        await channel.send(f"<:UV_uppu:792060506982711376> ┃ **{user} **payed respect to:\n            **{respects[0]}**", allowed_mentions=AllowedMentions.none())
   
    @commands.command(name='echo')
    async def echo(self, ctx, *, message):
		
        await ctx.message.delete()
        await ctx.send(message)


    @commands.command(name='ping')
    async def ping(self, ctx):
        """Sends a message with bot's latency in ms
		"""
      
        embed = discord.Embed(title="", description=f"<a:online:859859291586822154> **I am now alive!\n<a:DA_loveheart:862411473632755764> Heartbeat = > {round(self.bot.latency * 1000)} bpm!**", color=0xce2167)
        
        await ctx.send(embed=embed)
        



    @commands.command(aliases=['wikipedia'])
    async def wiki(self, ctx, *, query):
        '''Search up something on wikipedia'''
        em = discord.Embed(title=str(query))
        em.set_footer(text='Powered by wikipedia.org')
        try:
            result = wikipedia.summary(query)
            if len(result) > 2000:
                em.color = 0xce2167
                em.description = f"Result too long. View the website [here](https://wikipedia.org/wiki/{query.replace(' ', '_')})"
                return await ctx.send(embed=em)
            em.color = 0xce2167
            em.description = result
            await ctx.send(embed=em)
        except wikipedia.exceptions.DisambiguationError as e:
            em.color = 0xce2167
            options = '\n'.join(e.options)
            em.description = f"**Options:**\n\n{options}"
            await ctx.send(embed=em)
        except wikipedia.exceptions.PageError:
            em.color = 0xce2167        
            em.description = '<a:UV_exclamation:857218959224733696> | Page not found!'
            await ctx.send(embed=em)

          

    @commands.command()
    async def contactDev(self, ctx, *, idea: str):
        """<a:emoji_18:903101151623401492> | Your idea will be sent to the developer server!"""
        suggest = self.bot.get_channel(876000147543310376)
        em = discord.Embed(color=0xce2167)
        em.title = f"{ctx.author} | User ID: {ctx.author.id}"
        em.description = idea
        em.set_footer(text=f"From {ctx.author.guild} | Server ID: {ctx.author.guild.id}", icon_url=ctx.guild.icon_url)
        await suggest.send(embed=em)
      
        embed = discord.Embed(title="Message Sent", url="https://ukatoverse.com/discord", description="<a:emoji_19:903101184473169921> ┃ Your idea has been successfully sent to support server!", color=0xce2167)
        await ctx.send(embed=embed)


    @commands.command()
    async def invites(self, ctx, user:discord.Member=None):
        if user is None:
            total_invites = 0
            for i in await ctx.guild.invites():
                if i.inviter == ctx.author:
                    total_invites += i.uses
            
            embed = discord.Embed(title="Your Total Invites <a:UV_hearts:857218865377443840>", description=f"You've invited **{total_invites}** member{'' if total_invites == 1 else 's'} to the server!", color=0xce2167)
            await ctx.send(embed=embed)
            
        else:
            total_invites = 0
            for i in await ctx.guild.invites():
                if i.inviter == user:
                    total_invites += i.uses
            
            embed = discord.Embed(title=f"{user}'s Total Invites <a:UV_hearts:857218865377443840>", description=f"{user} has invited **{total_invites}** member{'' if total_invites == 1 else 's'} to the server!", color=0xce2167)
            await ctx.send(embed=embed)
 


    @commands.command(aliases=["stats", "activity"])
    async def messages(self, ctx, timeframe=7, channel: discord.TextChannel = None, *, user: discord.Member = None):
        if timeframe > 1968:
            embed = discord.Embed(title="", description="<:UV_No_Tick:853483191977115688> | Number of days exceeded the limit!", color=0xce2167)
            await ctx.channel.send(embed=embed)
        elif timeframe <= 0:
            embed = discord.Embed(title="", description="<:UV_No_Tick:853483191977115688> | Minimum day is **1**", color=0xce2167)
            await ctx.channel.send(embed=embed)
            

        else:
            if not channel:
                channel = ctx.channel
            if not user:
                user = ctx.author

            async with ctx.channel.typing():
                msg = await ctx.channel.send('<:UV_sed_meowwoo:792060495393456148> ┃ Please wait a sek')
                

                counter = 0
                async for message in channel.history(limit=5000, after=datetime.today() - timedelta(days=timeframe)):
                    if message.author.id == user.id:
                        counter += 1


                if counter >= 5000:
                    await msg.edit(content=f'```{user} has sent over 5000 messages in the channel "{channel}" within the last {timeframe} days!```')
                else:
                    await msg.edit(content=f'```{user} has sent {str(counter)} messages in the channel {channel} within the last {timeframe} days!```')

  
    @commands.command(name='changelog')
    async def get_info(self, ctx):
      embed = discord.Embed(title= 'Recent changes to Seina!', description= '**Seina by <a:emoji_14:903097354532556860> SOGI#1922**', color=0xce2167
                       )
      embed.set_footer(text="💌 | !contactDev [message/idea]")
      embed.add_field(name='Features added!', value='<a:emoji_21:903114385831104532> **Category ::** \n`Mal`,\n`Global`,\n`Fun`\n`Moderation`\n<:UV_uppu:792060506982711376> **Commands ::** \n`account`,\n`schedule`,\n`serverlink`,\n`serverunlink`,\n`servers`,\n`dice`,\n`numberfact`,\n`trump`,\n`purge`', inline=True)
      embed.add_field(name='Version', value='<:emoji_23:903181135016787978> 0.4', inline=True)
      embed.add_field(name='Language', value='<:emoji_22:903180126500560956> Python 3.8.12', inline=True)
      embed.add_field(name='Total servers', value=f'Running on {len(self.bot.guilds)} servers!', inline=True)
      await ctx.send(embed = embed)


    @commands.command(pass_context = True)
    async def reply(self, ctx, member : discord.Member, *, message=None):
      await member.send(message)
      
      embed = discord.Embed(title="", description=f"Successfully DMed {member}!\n**Message sent ::** {message}", color=0xce2167)
      await ctx.send(embed=embed, delete_after=30)
      await ctx.message.delete()
     
      
def setup(bot):
    bot.add_cog(Tools(bot))