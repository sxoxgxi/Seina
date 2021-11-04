from discord.ext import commands
import discord
from sys import version_info as sysv
from os import listdir

class Dev(commands.Cog):
	"""<a:UV_exclamation:857218959224733696> **| This is a cog/category with owner-only commands!\n<a:emoji_19:903101184473169921> | Want to contact developer? Do `!contactDev [message]`**
	"""
	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f'Python {sysv.major}.{sysv.minor}.{sysv.micro} - Disord.py {discord.__version__}\n')


	@commands.command(name='reloadall', hidden=True)#This command is hidden from the help menu.
	#This is the decorator for commands (inside of cogs).
	@commands.is_owner()
	#Only the owner (or owners) can use the commands decorated with this.
	async def reload_all(self, ctx):
		"""This commands reloads all the cogs in the `./cogs` folder.
		"""

		message = await ctx.send('<a:connecting:859859518569840660> ┃ Reloading')
		await ctx.message.delete()
		try:
			for cog in listdir('./cogs'):
				if cog.endswith('.py') == True:
					self.bot.reload_extension(f'cogs.{cog[:-3]}')
		except Exception as exc:
			await message.edit(content=f'<:UV_No_Tick:853483191977115688> | An error has occurred: {exc}', delete_after=20)
		else:
			await message.edit(content='<:UV_uppu:792060506982711376> ┃ All cogs have been reloaded.', delete_after=20)


	def check_cog(self, cog):
		"""Returns the name of the cog in the correct format.
		"""
		if (cog.lower()).startswith('cogs.') == True:
			return cog.lower()
		return f'cogs.{cog.lower()}'

	@commands.command(name='load', hidden=True)
	@commands.is_owner()
	async def load_cog(self, ctx, *, cog: str):
		"""This commands loads the selected cog, as long as that cog is in the `./cogs` folder.
		"""
		message = await ctx.send('<a:connecting:859859518569840660> ┃ Loading')
		await ctx.message.delete()
		try:
			self.bot.load_extension(self.check_cog(cog))
		except Exception as exc:
			await message.edit(content=f'<:UV_No_Tick:853483191977115688> ┃ An error has occurred: {exc}', delete_after=20)
		else:
			await message.edit(content=f'<:UV_uppu:792060506982711376> ┃ {self.check_cog(cog)} has been loaded.', delete_after=20)


	@commands.command(name='unload', hidden=True)
	@commands.is_owner()
	async def unload_cog(self, ctx, *, cog: str):
		"""This commands unloads the selected cog, as long as that cog is in the `./cogs` folder.
		"""
		message = await ctx.send('<a:connecting:859859518569840660> ┃ Unloading')
		await ctx.message.delete()
		try:
			self.bot.unload_extension(self.check_cog(cog))
		except Exception as exc:
			await message.edit(content=f'<:UV_No_Tick:853483191977115688> ┃ An error has occurred: {exc}', delete_after=20)
		else:
			await message.edit(content=f'<:UV_uppu:792060506982711376> ┃ {self.check_cog(cog)} has been unloaded.', delete_after=20)


	@commands.command(name='reload', hidden=True)
	@commands.is_owner()
	async def reload_cog(self, ctx, *, cog: str):
		"""This commands reloads the selected cog, as long as that cog is in the `./cogs` folder.
		"""
		message = await ctx.send('<a:connecting:859859518569840660> ┃ Reloading')
		await ctx.message.delete()
		try:
			self.bot.reload_extension(self.check_cog(cog))
		except Exception as exc:
			await message.edit(content=f'<:UV_No_Tick:853483191977115688> ┃ An error has occurred: {exc}', delete_after=20)
		else:
			await message.edit(content=f'<:UV_uppu:792060506982711376> ┃ {self.check_cog(cog)} has been reloaded.', delete_after=20)




def setup(bot):
	bot.add_cog(Dev(bot))