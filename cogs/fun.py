import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import random
import aiohttp
import secrets
import asyncio

class Fun(commands.Cog):
    '''**Fun commands for fun **<:UV_esmile:792060488887566416>'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx, number=1):
        '''Rolls a certain number of dice'''
        if number > 20:
            number = 20

        fmt = ''
        for i in range(1, number + 1):
            fmt += f'`Dice {i}: {random.randint(1, 6)}`\n'
            color = discord.Color.blue()
        em = discord.Embed(color=color, title=f'Rolled {number} times', description=fmt)
        await ctx.send(embed=em)


    @commands.command(aliases=['number'])
    async def numberfact(self, ctx, number: int):
        '''Get a fact about a number.'''
        if not number:
            await ctx.send(f'Usage: `{ctx.prefix}numberfact <number>`')
            return
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://numbersapi.com/{number}?json') as resp:
                    file = await resp.json()
                    fact = file['text']
                    await ctx.send(f"**Did you know?**\n> {fact}")
        except KeyError:
            await ctx.send("No facts are available for that number.")

    @commands.command(aliases=['trump', 'trumpquote'])
    async def asktrump(self, ctx, *, question):
        '''Ask Donald Trump a question!'''
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q={question}') as resp:
                file = await resp.json()
        quote = file['message']
        em = discord.Embed(color=discord.Color.blue())
        em.title = "What does Trump-Kun think?"
        em.description = f"- {quote}"
        em.set_footer(text="Try visiting whatdoestrumpthink.com", icon_url="https://cdn.discordapp.com/avatars/855522627187638272/d50e9cb1135fb57f075d5e015e5d3d36.png?size=2048")
        await ctx.send(embed=em)

    
    @commands.command()
    async def password(self, ctx, nbytes: int = 18):
        """ Generates and dms you the pssword
        """
        if nbytes not in range(3, 1401):
            return await ctx.send("<:UV_No_Tick:853483191977115688> | I only accept any numbers between 3-1400")
        if hasattr(ctx, "guild") and ctx.guild is not None:
            await ctx.send(f"<a:emoji_19:903101184473169921> | Sending you a private message with your random generated password **{ctx.author.name}**")
        await ctx.author.send(f"<a:hello:792212408751357952> | **Here is your password:**\n> {secrets.token_urlsafe(nbytes)}")



    @commands.command()
    async def rate(self, ctx, *, thing: commands.clean_content):
        """ Rates what you desire """
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.send(f"<:UV_uppu:792060506982711376> | I'd rate **{thing}** a **{round(rate_amount, 2)} /100**")


    @commands.command(aliases=["howhot", "hot"])
    async def sexy(self, ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        if hot > 75:
            emoji = "<:farm_ogladi:859860008429813820>"
        elif hot > 50:
            emoji = "<:UV_auhhhh:862252551156006932>"
        elif hot > 25:
            emoji = "<:UV_lisablush:900398189105020958>"
        else:
            emoji = "💔"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** sexy/hot {emoji}")

    
      
def setup(bot):
    bot.add_cog(Fun(bot))