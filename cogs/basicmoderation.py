from discord.ext import commands
import asyncio
import discord
from tinydb import TinyDB, Query
ongoing_purges = set()
 
class BasicMods(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["clear"])
    async def purge(self, ctx, *args):

        if not ctx.message.author.guild_permissions.manage_messages:
            embed = discord.Embed(title="", description="<a:UV_ghanta:905498296452263948> | You do not have the `manage_messages` permissions", color=0xce2167)
            await ctx.reply(embed=embed)
            
            return

        if ctx.channel.id in ongoing_purges:
            embed = discord.Embed(title="", description="<a:connecting:859859518569840660> ┃ A cleanup is going on!", color=0xce2167)
            msg = await ctx.reply(embed=embed)
            await asyncio.sleep(1)
            try: await msg.delete()
            except: pass
            return

        if len(args) != 0:
            limit = "".join(args)
            if limit.isdigit():
                limit = int(limit)
                if limit > 1000:
                    embed = discord.Embed(title="", description="<a:UV_exclamation:857218959224733696> ┃ You cannot purge more than 1000 messages at a time", color=0xce2167)
                    await ctx.reply(embed=embed)
      
                    return
                ongoing_purges.add(ctx.channel.id)
                await ctx.channel.purge(limit=limit + 1)
                ongoing_purges.remove(ctx.channel.id)
                message = await ctx.send("<a:connecting:859859518569840660> ┃ **purging**")
                await asyncio.sleep(1)
                await message.edit(content=f"<:UV_uppu:792060506982711376> ┃ Purged **{limit}** messages", delete_after=2)
                
                return
        embed = discord.Embed(title="", description="<:UV_No_Tick:853483191977115688> ┃ You must specify how many messages to purge!", color=0xce2167)
        await ctx.reply(embed=embed)



    @commands.command()
    async def send(self, ctx, channel: discord.TextChannel, *, content):
        await channel.send(content)
        await ctx.message.delete()
        embed = discord.Embed(title="", description=f"<a:UV_hearts:857218865377443840> ┃ Successfully delivered the message to {channel.mention}", color=0xce2167)
        await ctx.send(embed=embed)
        

    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, note : str = None):
     if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.kick_members or ctx.message.author.guild_permissions.ban_members:
        embed=discord.Embed(title="You have recieved a warning", description="**Warned by <:emoji_12:903094490850529281>** {1} ┃ **Moderator Note <:emoji_12:903094490850529281>** {2}".format(ctx.message.guild.name, ctx.message.author, note), color=0xce2167)
        embed.set_thumbnail(url="https://images.emojiterra.com/twitter/512px/26a0.png")
        await ctx.message.delete()
        await ctx.send(f"{member.mention}", embed=embed)
        
     else:
        embed = discord.Embed(title="<:UV_No_Tick:853483191977115688> ┃ Permission Denied!", description="You don't have permission to use this command", color=0xce2167)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(BasicMods(bot))