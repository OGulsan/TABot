import os
from typing import Any

import discord
from dotenv import load_dotenv

import canvas
import helpers
import ta_bot_ai

load_dotenv(".env")  # Loads variables from .env
courseID = os.getenv("CANVAS_COURSE_ID")

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents, **options: Any) -> None:
        super().__init__(intents=intents, **options)
        self.AIbot = ta_bot_ai.TABotAI()

    async def on_ready(self):
        general_chat = helpers.getGeneralTextChannelFromGuilds(self.guilds)
        await general_chat.send("Greetings students!") # Sends a greeting message into the channel

    async def on_member_join(self, member):
        general_chat = discord.utils.get(member.guild.text_channels, name = "general") # Grabs the general text channel
        await general_chat.send((f'Hello {member.mention} and welcome to the {member.guild.name} server!'))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if(helpers.isCommand(message)):
            if(message.content.strip() == "!help"):
                # Open the text file
                with open('help.txt', 'r') as file:
                    # Read the contents of the file
                    help_output = file.read()
                await message.channel.send(help_output)
            elif(message.content.strip()[1:] == "assignments"):
                # Grab assignments from canvas API
                assignments = canvas.returnAssignmentsDict(courseID=courseID)

                # Build out Clients response to command
                response = '```'
                for key, value in assignments.items():
                    if(value['assignment_due_date'] == 'No due date'):
                        response += '{}: {}\n{}\n{} possible points\n-----------------\n'.format(key, value['assignment_name'], value['assignment_due_date'], value['points_possible'])
                    else:
                        response += '{}: {}\ndue on {}\n{} possible points\n-----------------\n'.format(key, value['assignment_name'], value['assignment_due_date'], value['points_possible'])

                    
                response += '```'

                await message.channel.send(response)
            elif message.content.strip() == "!question":
                await message.channel.send('Hey {}. It seems as if you are trying to use the {} command but forgot to ask the question!\nPlease enter the question in the following format: ```!question {}```'.format(message.author.mention, "'!question'", "{question here}"))
            elif(message.content.strip()[1:10] == "question "):
                await message.channel.send("{}".format(self.AIbot.answerQuestion(message=message)))


intents = discord.Intents.default() # Establish intents to pass into Client constructor
intents.message_content = True
intents.members = True

token = os.getenv("DISCORD_BOT_TOKEN") # Retrieve my BOT's token

client = MyClient(intents=intents) # Create an instance of MyClient and pass in wanted intents
client.run(token) # type: ignore
