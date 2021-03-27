from cogs import database as db
from cogs import config
import discord
from discord.utils import get
from cogs import eventCog
import logging as logger
from discord.ext import commands

cogs = [eventCog]

#import all the config data
dataConfig = config.Oauth()
TOKEN, ownerID = dataConfig.discordTOKEN()
# intents = discord.Intents().all()
client = commands.Bot(command_prefix='!',
                      help_command=None,
                      owner_ids=ownerID)



for i in range(len(cogs)):
    cogs[i].setup(client)


@client.command(name='hello')
async def hello(message):
  guild = message.guild
  print(guild)
  await message.channel.send("HI")

@client.command()
async def hi(ctx):
  print(ctx)
  await ctx.channel.send("Hi")

@client.event
async def on_guild_channel_delete(channel):
  pass


@client.event
async def on_guild_channel_create(channel):
    pass


@client.event
async def on_connect():
    logger.info("Bot connected ")


@client.event
async def on_disconnect():
    logger.info("Bot disconnected ")


@client.event
async def on_memeber_join(member):
    pass

@client.event
async def on_guild_join(guild):
  # checking if admin role is exist if not exist it will create it
  # adminRole = get(guild.roles, name="admin")
  # print(adminRole,"outside")
  # if adminRole is None:
  #   await guild.create_role(name='admin',colour=discord.Colour.random())
  #   adminRole = get(guild.roles,name='admin')
  #   print(adminRole,"inside")

  # user with role admin and server owner can see the text_channel
  # botRole = get(guild.roles,name="Regbot")
  # overwrites = {
  #       guild.default_role: discord.PermissionOverwrite(read_messages=False),
  #       guild.owner: discord.PermissionOverwrite(read_messages=True)
  #   }
  channel = await guild.create_text_channel('Events-schedule')
  await channel.send('Event-schedule channel is created')

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

  #category = await guild.create_category

@client.event
async def on_guild_remove(guild):
  serverId = str(guild.id)
  db.removeServerInfo(serverId)
  # Remove the created channels
  logger.info("Removed from database")


@client.event
async def on_ready():
  logger.info("Bot logged in to ")  #Add the server name


@client.event
async def on_message(message):
  if message.author == client.user:  # if the message is send by bot it will return None
      return None

  if message.channel.name=='events-schedule':
    if message.content.startswith("create"):
        await message.channel.send("Hello")


client.run(TOKEN)