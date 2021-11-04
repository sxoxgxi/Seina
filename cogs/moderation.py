import discord
import os
import datetime
import asyncio
from discord.ext import commands


class Moderation(commands.Cog):
	def __init__(self, bot):
		self.bot = bot





	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def kick(self, ctx, member: discord.Member, reason="No Reason"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Kicked!", description=f"{member.mention} has been kicked!!", colour=0xce2167, timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Reason: ", value=reason, inline=False)
			await ctx.reply(embed=embed)
			await guild.kick(user=member)


	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def ban(self, ctx, member: discord.Member, reason="No Reason"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)
		else:
			guild = ctx.guild
			embed = discord.Embed(title="Banned!", description=f"{member.mention} has been banned!", colour=0xce2167, timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Reason: ", value=reason, inline=False)
			await ctx.reply(embed=embed)
			await guild.ban(user=member)



	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def unban(self, ctx, user: discord.User):
		if user == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Unbanned!", description=f"{user.display_name} has been unbanned!", colour=0xce2167, timestamp=datetime.datetime.utcnow())
			await ctx.reply(embed=embed)
			await guild.unban(user=user)



def setup(bot):
	bot.add_cog(Moderation(bot))