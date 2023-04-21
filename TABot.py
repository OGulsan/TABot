import discord
import os
import commands
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        for guild in self.guilds: # for each guild
            general_chat = discord.utils.get(guild.channels, name = "general") # grabs the general text channel
            await general_chat.send("Greetings students!") # sends a greeting message into the channel

    async def on_message(self, message):
        if message.author == self.user:
            return
        

intents = discord.Intents.default() # establish intents to pass into Client constructor
intents.message_content = True

load_dotenv(".env")  # loads variables from .env
token = os.getenv("DISCORD_BOT_TOKEN") # retrieve my BOT's token

client = MyClient(intents=intents) # create an instance of MyClient and pass in wanted intents
client.run(token)
