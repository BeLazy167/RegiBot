from cogs import databasemongo as db
from cogs import configbot as config
from cogs import eventCog
import discord
from discord.utils import get
from discord.ext import commands
import logging as logger


cogs = [eventCog]

#import all the config data
dataConfig = config.Oauth()
TOKEN, ownerID = dataConfig.discordTOKEN()
intents = discord.Intents().all()
client = commands.Bot(command_prefix='reg ',
                      help_command=None,
                      owner_ids=ownerID,intents=intents)



for i in range(len(cogs)):
    cogs[i].setup(client)


@client.event
async def on_disconnect():
  logger.info("Bot disconnected.")


@client.event
async def on_guild_join(guild):
  #create events-schedule
  overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.owner: discord.PermissionOverwrite(read_messages=True)
    }
  channel = await guild.create_text_channel('Events-schedule',overwrites=overwrites)
  await channel.send(""" Welcome to Regibot ®
  1. Only admin or server owners can access and use this channel to plan the events.
  2. You can create event using command:
      `reg create event_name` 
      example: `reg create hackathons`
  3. You can delete event using command:
      `reg delete event_name`
      example: `reg delete hackathons`
  4. You can export the registered users using this command:
      `reg data event_name`
  """)

  # Necessary Arguments
  serverID = str(guild.id)
  serverName = guild.name
  channelGuild = guild.text_channels
  roleGuild = guild.roles
  textChannelsList = []
  events = []
  rolesList = []

  # List append
  for role in roleGuild:
      rolesList.append(role.name)
  for channel in channelGuild:
      textChannelsList.append(channel.name)
  
  # Database creation
  db.addServerInfo(serverID, serverName, textChannelsList, rolesList, events)


@client.event
async def on_guild_remove(guild):
  serverId = str(guild.id)
  db.removeServerInfo(serverId)
  # Remove the created channels
  logger.info("Removed from database")


@client.event
async def on_ready():
  logger.info("Bot ready.")  #Add the server name


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  await client.process_commands(message)


client.run(TOKEN)