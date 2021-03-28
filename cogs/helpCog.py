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
        embed.add_field(name=':regional_indicator_c: Create', value=f"`{prefix}help create`", inline=True)
        embed.add_field(name=':x: Delete', value=f"`{prefix}help delete`", inline=True)
        embed.add_field(name=':clipboard: Data', value=f"`{prefix}help data`", inline=True)
        embed.add_field(name=':man_technologist: Participants', value=f"`{prefix}help givecount`",inline=True)
        embed.add_field(name=':no_entry_sign: clear', value=f"`{prefix}help clear`",inline=True)
        await message.channel.send(embed=embed)
      elif help_type.upper()=='CREATE':
        embed = discord.Embed(title=":regional_indicator_c: Create",description=f'You can create event using command:\n `{prefix}create event_name` \n example: `reg create hackathons`',colour=0x00ff00)
        await message.channel.send(embed=embed)
      elif help_type.upper()=='DELETE':
        embed = discord.Embed(title=":x: Delete",description=f'You can delete event using command:\n `{prefix}delete event_name` \n example: `reg delete hackathons`',colour=0x00ff00)
        await message.channel.send(embed=embed)
      elif help_type.upper()=='DATA':
        embed = discord.Embed(title=":clipboard: Data",description=f'You can export the registered users in a csv file using: \n `{prefix}data event_name` \n example: `reg data hackathons`',colour=0x00ff00)
        await message.channel.send(embed=embed)
      elif help_type.upper()=='GIVECOUNT':
        embed = discord.Embed(title=":man_technologist: Participants",description=f'You can get the total count of members in the event using: \n `{prefix}givecount event_name` \n example: `reg givecount hackathons`',colour=0x00ff00)
        await message.channel.send(embed=embed)
      elif help_type.upper()=='CLEAR':
        embed = discord.Embed(title=":no_entry_sign: clear",description=f' You can clear all messages in chat using: \n `{prefix}data event_name` \n example: `reg data hackathons`',colour=0x00ff00)
        await message.channel.send(embed=embed)

def setup(client):
  client.add_cog(Help(client))
