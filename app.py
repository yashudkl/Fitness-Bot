import discord

from discord.ext import commands
client = commands.Bot(command_prefix="<3 ")
@client.event
async def on_ready():
    #status of bot
    await client.change_presence(activity=discord.Game('<3/ Workout'))
    
    print("The bot is ready")

   #Embed
@client.command() 
async def shedule(ctx):
    embed = discord.Embed(
        title= "Shedule ",
        color = discord.Color.purple(),
        description = "Follow the Shedule provided."
    )
    embed.add_field(name="Weight gain", value="Workouts:-Push Day, Pull day, Leg Day", inline=True)
    embed.add_field(name="Fat Loss", value="Workouts:- Cardio Workouts always", inline=True)
    embed.set_image(url='https://th.bing.com/th/id/OIP.1NfnV_pv0VI4QaQJBgHdVQHaEc?w=300&h=180&c=7&o=5&pid=1.7')
    embed.set_thumbnail(url='https://th.bing.com/th/id/OIP.W1Sy8iy9IUMxY5nxgUVeZwHaHa?w=182&h=182&c=7&o=5&pid=1.7')

    await ctx.send(embed=embed)

@client.command() 
async def pushday(ctx):
    embed = discord.Embed(
        title= "Push Day Workouts",
        color = discord.Color.purple(),
        description = "We have some push day workouts here:-"
    )
    embed.add_field(name="Weighted Pushups", value="Do Pushups With Weight For eg:-Bags", inline=True)
    embed.add_field(name="Dips", value="Do some dips (you can add wighths)", inline=True)

    
    
    

    await ctx.send(embed=embed)

@client.command() 
async def weightedpushups(ctx):
    embed = discord.Embed(
        title= "How to do Weighted pushups",
        color = discord.Color.purple(),
        description = "Just add weights (book in bags) in Normal pushups"
    )
    embed.set_image(url='https://tenor.com/view/captain-america-push-up-army-gif-15310843')
    
    await ctx.send(embed=embed)
    
@client.command() 
async def pull(ctx):
    embed = discord.Embed(
        title= "Push Day Workouts",
        color = discord.Color.purple(),
        description = "We have some pull day workouts here:-"
    )
    embed.add_field(name="Pullups", value="Do Pullups ", inline=True)
    embed.add_field(name="Bicep curls", value="Do Bicep curls", inline=False)


    
   

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
 
 
client.run("Aachi Khau")
