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

  @commands.command(name="create",aliases=['Event','evenT','EVENT'])
  async def event(self,message,event="None"):
    """
    Create event related text and voice channels.
    """
    channels = ['events-schedule']
    logger.info(message)
    guild = message.guild
    if message.channel.name in channels:
      db.createEventAdmin(str(guild.id),event)
      category = await guild.create_category(event,overwrites=None,reason=None)
      await guild.create_text_channel(f'{event}-registartion',category=category)
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
    print(message)
    print()
    event = str(args[0])+str(args[2])
    eventData = event.split(",")
    print(eventData)
    eventName = eventData[0]
    serverID = message.guild.id
    teamName = eventData[1]
    discordID= str(args[1])
    print(discordID.member)
    logger.info(discordID)
    name = eventData[3]
    age = eventData[4]
    emailID = eventData[5]
    if len(eventData)==7:
      passcode=eventData[6]
    else:
      passcode=None
    print(passcode)
    # db.mainTemplate(serverID,eventName,teamName,discordID,name,age,emailID,passcode)

def setup(client):
  client.add_cog(eventCreate(client))