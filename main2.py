# import database as db
import config
import discord
from discord.utils import get
import logging as logger
from cogs import eventCog
from discord.ext import commands

#import all the config data
dataConfig = config.Oauth()
TOKEN, ownerID = dataConfig.discordTOKEN()
intents = discord.Intents().all()
client = commands.Bot(command_prefix="reg ",
                      help_command=None,
                      owner_ids=ownerID,intents=intents)
logger.basicConfig(level=logger.INFO)

cogs = [eventCog]
for i in range(len(cogs)):
  cogs[i].setup(client)
  
# @client.event
# async def on_guild_channel_delete(channel):
#   pass


# @client.event
# async def on_guild_channel_create(channel):
#     pass

@client.command(name="hello")
async def hello(message):
    guild = message.guild
    print(guild)
    await message.channel.send("Hi")


@client.event
async def on_ready():
    logger.info("The bot is ready")



# @client.event
# async def on_disconnect():
#     logger.info("Bot disconnected ")


# @client.event
# async def on_memeber_join(member):
#     pass

# @client.command(name='delete')
# @commands.has_permissions(manage_roles=True)
# async def delete(message):
#   textChannel = message.channel.name
#   if textChannel=="events-schedule":
#     textChannel.delete()


@client.event
async def on_guild_join(guild):
  # Ch
  overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.owner: discord.PermissionOverwrite(read_messages=True),
        # adminRole: discord.PermissionOverwrite(read_messages=True)
    }
  channel = await guild.create_text_channel('Events-schedule',overwrites=overwrites)

  # Necessary Arguments
  # serverID = str(guild.id)
  # serverName = guild.name
  # channelGuild = guild.text_channels
  # roleGuild = guild.roles
  # textChannelsList = []
  # events = []
  # rolesList = []

  # List append
  # for role in roleGuild:
  #     rolesList.append(role.name)
  # for channel in channelGuild:
  #     textChannelsList.append(channel.name)
  
  # Database creation
  # db.addServerInfo(serverID, serverName, textChannelsList, rolesList, events)

  #category = await guild.create_category

# @client.event
# async def on_guild_remove(guild):
#   serverId = str(guild.id)
#   # db.removeServerInfo(serverId)
#   # Remove the created channels
#   logger.info("Removed from database")




@client.event
async def on_message(message):
  # channels = ['events-schedule']
  if message.author == client.user: 
    return 
      
  # if message.channel.name in channels:
  #   if message.content.startswith("create"):
  #     msg = message.content.split(' ')
      
  #     logger.info(message)
  #     guild = message.guild
  #     logger.info(guild)
  #     # db.createEvent(str(guild.serverID),event)
  #     category = await guild.create_category(msg[2],overwrites=None,reason=None)
  #     await guild.create_text_channel(f'{msg[2]}-registartion',category=category)
  #     await guild.create_text_channel(f'{msg[2]}-chat',category=category)
  #     await guild.create_text_channel(f'{msg[2]}-announcements',category=category)
  #     await guild.create_voice_channel(f'{msg[2]}',category=category)
  #     # await guild.create_roles(name=event,colour=discord.Colour.random())
  #     await guild.channel.send('Event is created')
    
  await client.process_commands(message)
  


client.run(TOKEN)