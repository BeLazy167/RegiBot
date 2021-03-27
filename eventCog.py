from dicord.ext import commands
import discord
import database as db

class eventCreate(commands.Cog):
  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_ready(self):
    print("eventCreate cog is ready")

  @commands.command(name="create",aliases=['Event','evenT','EVENT'])
  async def event(self,message,event="None"):
    channels = ['events-schedule']
    guild = message.guild
    if message.channel.name in channels:
      db.createEvent(str(guild.serverID),event)

  @commands.Cog.listener()
  async def on_message(self,message):
    eventInfo = message.content.split(",")
    eventName = eventInfo[0]
    serverID = message.guild.id
    teamName = eventInfo[1]
    discordID=[]
    name =[]
    age =[]
    emailID = []
    for i in range(2,len(eventInfo)):
      name.append(eventInfo[i])
    db.mainTemplate(serverID,eventName,teamName,discordID,name,age,emailID)
