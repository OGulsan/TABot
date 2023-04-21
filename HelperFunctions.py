import discord

def getGeneralTextChannel(guilds):
    for guild in guilds: # for each guild
            general_chat = discord.utils.get(guild.channels, name = "general") # grabs the general text channel
    return general_chat
