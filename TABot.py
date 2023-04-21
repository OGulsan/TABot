import discord
import os
import HelperFunctions
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        general_chat = HelperFunctions.getGeneralTextChannelFromGuilds(self.guilds)
        await general_chat.send("Greetings students!") # sends a greeting message into the channel

    async def on_member_join(self, member):
        general_chat = discord.utils.get(member.guild.text_channels, name = "general") # grabs the general text channel
        await general_chat.send((f'Hello {member.name} and welcome to the {member.guild.name} server!'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if(HelperFunctions.isCommand(message)):
            await message.channel.send('Commands coming to a server near you very soon!')
        

intents = discord.Intents.default() # establish intents to pass into Client constructor
intents.message_content = True
intents.members = True

load_dotenv(".env")  # loads variables from .env
token = os.getenv("DISCORD_BOT_TOKEN") # retrieve my BOT's token

client = MyClient(intents=intents) # create an instance of MyClient and pass in wanted intents
client.run(token)
