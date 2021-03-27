from discord.ext import commands
import discord
from cogs import databasemongo as db
import logging as logger

logger.basicConfig(level=logger.INFO)

class eventCreate(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_ready(self):
    logger.info("eventCreate cog is ready")

  @commands.command(name="clear")
  async def clear(self,message,value=None):
    pass


  @commands.command(name='delete')
  async def delete(self,message,event= None):
    channel = ['events-schedule']
    if message.channel.name in channel:
      for category in message.guild.categories:
        if category.name == f'{event}':
          for channel in category.channels:
            await channel.delete()
          await category.delete()
      await channel.send(f'{event} deleted.')
    db.deleteEvent(message.guild.id,event)

  @commands.command(name="data")
  async def data(self,message,event= None):
    channel = ['events-schedule']
    if message.channel.name in channel:
      pass

  @commands.command(name="create",aliases=['Event','evenT','EVENT'])
  async def create(self,message,event="None"):
    """
    Create event related text and voice channels.
    """
    channels = ['events-schedule']
    logger.info(message)
    guild = message.guild
    if message.channel.name in channels:
      db.createEventAdmin(str(guild.id),event)
      category = await guild.create_category(event,overwrites=None,reason=None)
      channelregi= await guild.create_text_channel(f'{event}-registration',category=category)
      embed = discord.Embed(description="""
      1. Type in reg event following the event name as 
      example `reg event huehacks`
      2. if your team is registering for a first-time bot will send the passcode to the first member who has registered the team he will share the passcode with other members.
      3. Following the event name enter your details as
      `reg event event_name,Team_name,Name,Age,email@example.com,passcode.`
      Example - 
      reg event huehacks,LaziX,Rutvik,21,rj@gmail.com,1463.
      4. Best of luck with event!👍
      """,title="How to register❓:",colour=0x00ff00)
      # await channelregi.send("""
      # How to register❓:
      # 1. Type in reg event following the event name as 
      # example `reg event huehacks`
      # 2. if your team is registering for a first-time bot will send the passcode to the first member who has registered the team he will share the passcode with others member.
      # 3. Following the event name enter your details as
      # `reg event event_name,Team_name,Name,Age,email@example.com,passcode.`
      # Example - 
      # reg event huehacks,LaziX,Rutvik,21,rj@gmail.com,1463.
      # 4. Best of luck with event!👍
      # """)
      await channelregi.send(embed=embed)

      await guild.create_text_channel(f'{event}-chat',category=category)
      await guild.create_text_channel(f'{event}-announcements',category=category)
      await guild.create_voice_channel(f'{event}',category=category)
      await guild.create_role(name=event,colour=discord.Colour.random())
      await message.channel.send(f'{event} is created.')

  @commands.command(name='event')
  async def on_message(self,message,*args):
    """
    Registeration for users.
    """
    logger.info(args)
    event = args[0]
    logger.info(event)
    eventData = event.split(",")
    eventName = eventData[0]
    serverID = str(message.guild.id)
    teamName = eventData[1]
    discordID= message.author.id
    discordUsername = message.author.name
    #logger.info(discordID)
    name = eventData[2]
    age = eventData[3]
    emailID = eventData[4]
    if len(eventData)==6:
      passcode=int(eventData[5])
    else:
      passcode=None
    if message.channel.name==f'{eventName}-registration':
      print(passcode)
      tag, passcode = db.mainTemplate(serverID,eventName,teamName,discordID,discordUsername,name,age,emailID,passcode)

      if passcode is None:
        await message.channel.send(tag)
      else:
        await message.author.send(f' Your team passcode is {passcode}.\n {tag}')
      await message.author.add_roles(discord.utils.get(message.author.guild.roles,name=f'{eventName}'))
    else:
      await message.channel.send(f'please check {eventName}-registration channel')
    await message.message.delete()

def setup(client):
  client.add_cog(eventCreate(client))