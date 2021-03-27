import discord

from discord.ext import commands
client = commands.Bot(command_prefix="<3")
@client.event
async def on_ready():
    #status of bot
    await client.change_presence(activity=discord.Game('<3/ Workout'))
    
    print("The bot is ready")


    

    
   

    #ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong {round(client.latency*1000)}ms')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    

import asyncio
@client.command()
async def test(ctx, arg):
    await ctx.send(arg)
 

 
#Send anonymous DM's
@client.command()
async def send_anonymous_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(content) # send whatever in the content to the mentioned user.
# Usage: !send_anonymous_dm @mention_user <your message here>
 
# THIS FUNCTION WILL SEND A DM WITH THE AUTHORS NAME.
@client.command()
async def sendDM(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(f"**{ctx.message.author} said:** {content}") # send whatever in the content to the mentioned user along with the author's name.
 
# Usage: !send_anonymous_dm @mention_user <your message here>
 
 
client.run("Tero Bau")
