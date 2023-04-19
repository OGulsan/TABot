import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Hey! {self.user.name} here and ready to roll')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await message.channel.send("Hi!")


intents = discord.Intents.default() # establish intents to pass into Client constructor
intents.message_content = True

load_dotenv(".env")  # take environment variables from .env.
token = os.getenv("DISCORD_BOT_TOKEN")

client = MyClient(intents=intents) # create an instance of MyClient and pass in wanted intents
client.run(token)
