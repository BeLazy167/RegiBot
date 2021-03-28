import discord
import logging as logger
from discord.ext import commands

class Help(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    logger.info("Help cog ready")

  @commands.command(name="help",aliases=['Help', 'HElp', 'HELp', 'HELP', 'hELP', 'heLP', 'helP', 'HeLp', 'hElP'])
  async def help(self,message,help_type=None):
    channels=['events-schedule']
    prefix ="reg "
    if message.channel.name in channels:
      if help_type is None:
        embed = discord.Embed(title="Bot Commands List", description="we have some really amazing commands")
        embed.add_field(name='<:facts:814823810263547924> Create', value=f"`{prefix}help create`", inline=True)
        embed.add_field(name='<:joke:814826126668726292> Delete', value=f"`{prefix}help delete`", inline=True)
        embed.add_field(name='<:meme:814824521324036096> Data', value=f"`{prefix}help data`", inline=True)
        embed.add_field(name='<:fire:814825327833382942> Participants', value=f"`{prefix}help givecount`",inline=True)
        embed.add_field(name='<:fire:814825327833382942> clear', value=f"`{prefix}help clear`",inline=True)
        await message.channel.send(embed=embed)
      elif help_type.upper()=='CREATE':
        embed = discord.Embed(title="Create",description=f'You can create event using command:\n `{prefix}create event_name` \n example: reg create hackathons',colour=0x00ff00)
        await message.channel.send(embed=embed)
      elif help_type.upper()=='DELETE':
        embed = discord.Embed(title="Delete",description=f'You can delete event using command:\n `{prefix}delete event_name` \n example: reg delete hackathons')
        await message.channel.send(embed=embed)
      elif help_type.upper()=='DATA':
        embed = discord.Embed(title="Data",description=f'You can export the registered users in a csv file using: \n `{prefix}data event_name` \n example: reg data hackathons')
        await message.channel.send(embed=embed)
      elif help_type.upper()=='GIVECOUNT':
        embed = discord.Embed(title="Count",description=f'You can get the total count of members in the event using: \n `{prefix}givecount event_name` \n example: reg givecount hackathons')
        await message.channel.send(embed=embed)
      elif help_type.upper()=='CLEAR':
        embed = discord.Embed(title="Count",description=f' You can clear all messages in chat using: \n `{prefix}data event_name` \n example: reg data hackathons')
        await message.channel.send(embed=embed)

def setup(client):
  client.add_cog(Help(client))
