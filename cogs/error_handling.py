from discord.ext import commands
import discord

class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return 
        elif isinstance(error, commands.CommandOnCooldown):
            embed=discord.Embed(title="Command Cooldown", description=f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.", color=0xce2167)
        elif isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(title="Permission Denied", description=f"{ctx.message.author.mention} baka!, Get permissions to run this command!", color=0xce2167)
        elif isinstance(error, commands.UserInputError):
            embed=discord.Embed(title="Input Error", description=f"{ctx.message.author.mention} baka!, Something about your input was wrong!\n**Do `{ctx.prefix}help {ctx.command}` for more information on it**", color=0xce2167)
        else:
            embed=discord.Embed(title="Unknown Error", description="Oh no! Something went wrong while running the command!", color=0xce2167)
     

        await ctx.reply(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
