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
    print("eventCreate cog is ready")



  @commands.command(name='delete')
  async def delete(self,message,event= None):
    logger.info(message.guild.categories)
    for category in message.guild.categories:
      if category.name == f'{event}':
        await category.channels.delete()
        
  



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
      await guild.create_text_channel(f'{event}-registration',category=category)
      await guild.create_text_channel(f'{event}-chat',category=category)
      await guild.create_text_channel(f'{event}-announcements',category=category)
      await guild.create_voice_channel(f'{event}',category=category)
      await guild.create_role(name=event,colour=discord.Colour.random())
      await message.channel.send('Event is created')

  @commands.command(name='event')
  async def on_message(self,message,*args):
    """
    Registeration for users.
    """
    event = str(args[0])
    eventData = event.split(",")
    eventName = eventData[0]
    serverID = str(message.guild.id)
    teamName = eventData[1]
    discordID= message.author.id
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
      tag, passcode = db.mainTemplate(serverID,eventName,teamName,discordID,name,age,emailID,passcode)

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