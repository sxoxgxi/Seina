# Used for ModMail on UkatoVerse server (https://ukatoverse.com/discord/)

import discord
from discord.ext import commands

class UkatoVerse(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        meow = []
        cat_house = self.bot.get_channel(876000147543310376)

        # message from cat
        if message.author == self.bot.user:
         return
        if str(message.channel.type) == "private":
            if message.attachments != meow:
                files = message.attachments
                await cat_house.send(f"**{message.author.display_name}  | {message.author.id}**")

                for file in files:
                    await cat_house.send(file.url)
            else:
                await cat_house.send(f"**{message.author.display_name} | {message.author.id} ::** {message.content}")
                
        # responding to cat
        elif message.channel == cat_house and message.content.startswith("<"):
            cat = message.mentions[0]
            if message.attachments != meow:
                files = message.attachments
                
              

                for file in files:
                    await cat.send(file.url)
        
  
def setup(bot):
    bot.add_cog(UkatoVerse(bot))
