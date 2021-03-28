from discord.ext import commands
import discord
from discord.utils import get
from cogs import databasemongo as db
from cogs import databasetocsv as data
import logging as logger
import os

logger.basicConfig(level=logger.INFO)

def delete(fileName):
  os.remove(fileName)

class eventCreate(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_ready(self):
    logger.info("EventCreate cog is ready")

  @commands.command(name="clear")
  async def clear(self,message,value=5):
    await message.channel.purge(limit=value)
    


  @commands.command(name='delete')
  async def delete(self,message,event=None):
    channel = ['events-schedule']
    if message.channel.name in channel:
      if event is not None:
        tag,value= db.eventCheck(str(message.guild.id),event)
        if value is not None:
          for category in message.guild.categories:
            if category.name == f'{event}':
              for channel in category.channels:
                await channel.delete()
              await category.delete()
              channelRole = get(message.guild.roles,name=f'{event}')
              await channelRole.delete()
          await message.channel.send(f'Event {event} deleted.')
          db.deleteEvent(str(message.guild.id),event)
        else:
          embed = discord.Embed(title="Falied",description=f'**No such event named {event}**',color=0xff0000)
          await message.channel.send(embed=embed)
      else:
        embed = discord.Embed(title="Failed",description=f'Event Name Cannot be None',color=0x0000ff)
        await message.channel.send(embed=embed)


  @commands.command(name="data")
  async def data(self,message,event= None):
    channel = ['events-schedule']
    if message.channel.name in channel and event is not None:
      tag,value= db.eventCheck(str(message.guild.id),event)
      if value is not None:
        csvFile = data.mongoToCsv(str(message.guild.id),event)
        await message.channel.send(file=discord.File(csvFile))
        delete(csvFile)
      else:
        embed = discord.Embed(title="Falied",description=f'**{event}, no such event found.**',color=0xff0000)
        await message.channel.send(embed=embed)
    else:
      embed = discord.Embed(title="Failed",description=f'Event Name Cannot be None',color=0xff0000)
      await message.channel.send(embed=embed)
  
  @commands.command(name="givecount")
  async def givecount(self,message,event=None):
    channel = ['events-schedule']
    if message.channel.name in channel:
      if event is not None:
        count = data.totalParticipant(str(message.guild.id),event)
        embed = discord.Embed(title=f'{event}',description=f'Total number of participants register for event: {count}',colour=discord.Colour.random())
        await message.channel.send(embed=embed)
      else:
        embed = discord.Embed(title="Failed",description=f'Event Name Cannot be None',color=0xff0000)
        await message.channel.send(embed=embed)

  @commands.command(name="create",aliases=['Event','evenT','EVENT'])
  async def create(self,message,event=None):
    """
    Create event related text and voice channels.
    """
    channels = ['events-schedule']
    logger.info(message)
    guild = message.guild
    if message.channel.name in channels:
      if event is not None:
        db.createEventAdmin(str(guild.id),event)
        category = await guild.create_category(event,overwrites=None,reason=None)
        await guild.create_role(name=event,colour=discord.Colour.random())
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
        channelRole = get(guild.roles,name=f'{event}')
        overwrites = {
          guild.default_role: discord.PermissionOverwrite(read_messages=False),
          guild.owner: discord.PermissionOverwrite(read_messages=True),
          channelRole: discord.PermissionOverwrite(read_messages=True)
        }
        await channelregi.send(embed=embed)
        await guild.create_text_channel(f'{event}-chat',category=category,overwrites=overwrites)
        await guild.create_text_channel(f'{event}-announcements',category=category)
        await guild.create_voice_channel(f'{event}',category=category,overwrites=overwrites)
        
        await message.channel.send(f'{event} is created.🎉')
      else:
        embed = discord.Embed(title="Failed",description=f'Event Name Cannot be None',colour=0xff0000)
        await message.channel.send(embed=embed)

  @commands.command(name='event')
  async def event(self,message,*args):
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
      #logger.info(passcode)
      tag, teamName, passcode = db.mainTemplate(serverID,eventName,teamName,discordID,discordUsername,name,age,emailID,passcode)
      if passcode is None:
        await message.channel.send(tag)
      else:
        #logger.info(tag,teamName,passcode)
        if tag==teamName:
          await message.author.send(f'Your team name is {teamName} and passcode is {passcode} for event {eventName} at {message.guild.name}.') 
        elif tag.startswith("Registration done"):
          await message.author.send(f'{tag} for event {eventName} at {message.guild.name}.')
        else:
          await message.author.send(f'You are already registered in team {teamName} for event {eventName} at {message.guild.name}.')
          
      await message.author.add_roles(discord.utils.get(message.author.guild.roles,name=f'{eventName}'))
    else:
      tag,value = db.eventCheck(str(message.guild.id),eventName)
      if value is None:
        embed = discord.Embed(title="Falied",description=f'**{eventName} no such event found.**')
        #await message.channel.send(f'**Please check {eventName}-registration channel.**')
        await message.channel.send(embed=embed)
      else:
        embed = discord.Embed(description=f'**Please check {eventName}-registration channel.**')
        #await message.channel.send(f'**Please check {eventName}-registration channel.**')
        await message.channel.send(embed=embed)
    await message.message.delete()

def setup(client):
  client.add_cog(eventCreate(client))