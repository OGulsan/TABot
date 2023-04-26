import discord

def getGeneralTextChannelFromGuilds(guilds):
    for guild in guilds: # for each guild
            general_chat = discord.utils.get(guild.text_channels, name = "general") # grabs the general text channel
    return general_chat

def isCommand(message):
      if(message.content.startswith('!')):
            return True
      return False