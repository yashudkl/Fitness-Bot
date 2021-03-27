import discord # Main Module for discord API wrapper
from discord.ext import commands
import asyncio

prefix = '<3'  # Prefix of the bot '<3'

@client.event
async def on_ready():
    #status of bot
    await client.change_presence(activity=discord.Game('^/ Workout'))
    
    print("The bot is ready")
    
       #ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong {round(client.latency*1000)}ms')
    
    #For clear (Purge)
    
    @client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    
#Sends DM
@client.command()
async def send_anonymous_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(content) # send whatever in the content to the mentioned user.
#For using: !send_anonymous_dm @mention_user <your message here>
 
# THIS FUNCTION WILL SEND A DM WITH THE Name and msg
@client.command()
async def sendDM(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(f"**{ctx.message.author} said:** {content}") # send whatever in the content to the mentioned user along with the author's name.
 
# For using: !send_anonymous_dm @mention_user <your message here>





client.run("ODIyMjcxMjM3Nzk4ODg3NDI0.YFP1xA.OACvxooNzRCel98p_ZrrcabSndA") # running the bot
