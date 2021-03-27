from discord.ext import commands
import discord
# import database as db


class eventCreate(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_ready(self):
    print("eventCreate cog is ready")

  @commands.command(name='create',aliases=['Create','creatE'])
  async def create(self, message, event):
    channels = ['events-schedule']
    print(message)
    guild = message.guild
    print(guild)
    if message.channel.name in channels:
      db.createEvent(str(guild.serverID),event)
      category = await guild.create_category(event,overwrites=None,reason=None)
      await guild.create_text_channel(f'{event}-registartion',category=category)
      await guild.create_text_channel(f'{event}-chat',category=category)
      await guild.create_text_channel(f'{event}-announcements',category=category)
      await guild.create_voice_channel(f'{event}',category=category)
      await guild.create_roles(name=event,colour=discord.Colour.random())
      await guild.send('Event is created')

  # @commands.Cog.listener()
  # async def on_message(self,message):
  #   if message.author == self.client.user:  # if the message is send by bot it will return None
  #     return None
    
  #   if message.channel.name =='events-schedule':
  #     await message.channel.send("event")
  #   # eventInfo = message.content.split(",")
  #   # eventName = eventInfo[0]
  #   # serverID = message.guild.id
  #   # teamName = eventInfo[1]
  #   # discordID=[]
  #   # name =[]
  #   # age =[]
  #   # emailID = []
  #   # for i in range(2,len(eventInfo)):
  #   #   name.append(eventInfo[i])
  #   # db.mainTemplate(serverID,eventName,teamName,discordID,name,age,emailID)


def setup(client):
  client.add_cog(eventCreate(client))