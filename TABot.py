import discord

from typing import Any
import canvas
import OpenAI
import os
import HelperFunctions
from dotenv import load_dotenv

courseID = 123546

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents, **options: Any) -> None:
        super().__init__(intents=intents, **options)
        self.AIbot = OpenAI.TABotAI()

    async def on_ready(self):
        general_chat = HelperFunctions.getGeneralTextChannelFromGuilds(self.guilds)
        await general_chat.send("Greetings students!") # sends a greeting message into the channel

    async def on_member_join(self, member):
        general_chat = discord.utils.get(member.guild.text_channels, name = "general") # grabs the general text channel
        await general_chat.send((f'Hello {member.mention} and welcome to the {member.guild.name} server!'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if(HelperFunctions.isCommand(message)):
            if(message.content.strip()[1:] == "assignments"):
                # grab assignments from canvas API
                assignments = canvas.returnAssignmentsDict(courseID=courseID)

                # build out Clients response to command
                response = '```'
                for key, value in assignments.items():
                    response += '{}: {}\ndue on {}\n{} possible points\n-----------------\n'.format(key, value['assignment_name'], value['assignment_due_date'], value['points_possible'])
                response += '```'

                await message.channel.send(response)
            elif message.content.strip() == "!question":
                await message.channel.send('Hey {}. It seems as if you are trying to use the {} command but forgot to ask the question!\nPlease enter the question in the following format: ```!question {}```'.format(message.author.mention, "'!question'", "{question here}"))
            elif(message.content.strip()[1:10] == "question "):
                await message.channel.send("{}".format(self.AIbot.answerQuestion(message=message)))



            
        

intents = discord.Intents.default() # establish intents to pass into Client constructor
intents.message_content = True
intents.members = True

load_dotenv(".env")  # loads variables from .env
token = os.getenv("DISCORD_BOT_TOKEN") # retrieve my BOT's token

client = MyClient(intents=intents) # create an instance of MyClient and pass in wanted intents
client.run(token) # type: ignore
