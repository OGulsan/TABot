import discord
import os
import commands
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        for guild in self.guilds: # for each guild
            for channel in guild.channels: # for each channel in each guild
                if isinstance(channel, discord.TextChannel) and channel.name == "general": # display a greeting message to all text channels named 'general'
                    await channel.send("Greetings students!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        
intents = discord.Intents.default() # establish intents to pass into Client constructor
intents.message_content = True

load_dotenv(".env")  # loads variables from .env
token = os.getenv("DISCORD_BOT_TOKEN") # retrieve my BOT's token

client = MyClient(intents=intents) # create an instance of MyClient and pass in wanted intents
client.run(token)
