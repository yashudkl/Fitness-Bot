import discord                                  # discord.py module.
from discord.ext import commands, tasks         # discord.py commands module.
import asyncio                                  # time.sleep function.
import json                                     # json module for reading and writing into json file(s).
from datetime import datetime                   # datetime for getting current time. 
import datetime as dt                           # datetime for setting time.

def get_token():
    """
    token grabber. returns: client's token  
    """
    with open('bot_config.json', 'r') as openfile:
        json_object = json.load(openfile)
        pairs = json_object.items()
        bot_token = json_object["token"]
    return bot_token


client = commands.Bot(command_prefix = "test ")   # global bot delcaration.
# bot on ready function
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('<3/ Workout'))
    print(f'{client.user.name} deployed!')

# lists outs schedule of the week
@client.command()
async def routine(ctx):
    routine_embed = discord.Embed(
        title = "📋: Routine",
        color = discord.Color.purple(),
        description = "7 days, 6 grind, 1 rest."
    )
    routine_embed.add_field(name = "Sun",  value  = "Push day", inline = True)
    routine_embed.add_field(name = "Mon",  value  = "Pull day", inline = True)
    routine_embed.add_field(name = "Tues", value  = "Leg day", inline = True)
    routine_embed.add_field(name = "Wed",  value  = "Abs day", inline = True)
    routine_embed.add_field(name = "Thrs", value  = "Pull day", inline = True)
    routine_embed.add_field(name = "Sat",  value  = "Pull day")
    routine_embed.set_thumbnail(url = 'https://media4.giphy.com/media/3o7qE4gcYTW1zZPkre/source.gif')
    routine_embed.set_footer(text = 'Friday rest  🛌')
    await ctx.send(embed = routine_embed)


@client.command() 
async def schedule(ctx):
    embed = discord.Embed(
        title= "Schedule ",
        color = discord.Color.purple(),
        description = "Follow the Schedule provided."
        )
    embed.add_field(name="Weight gain", value="Workouts:-Push , Pull , Leg", inline=True)
    embed.add_field(name="Fat Loss", value="Workouts:- Cardio ", inline=True)
    embed.set_image(url='https://th.bing.com/th/id/OIP.1NfnV_pv0VI4QaQJBgHdVQHaEc?w=300&h=180&c=7&o=5&pid=1.7')
    embed.set_thumbnail(url='https://th.bing.com/th/id/OIP.W1Sy8iy9IUMxY5nxgUVeZwHaHa?w=182&h=182&c=7&o=5&pid=1.7')
    await ctx.send(embed=embed)

# information about pull
@client.command() 
async def push(ctx):
    embed = discord.Embed(
        title= "Push Day Workouts",
        color = discord.Color.purple(),
        description = "We have some push day workouts here:-"
    )
    embed.add_field(name="Weighted Pushups", value="Do Pushups (<3 weightedpushups)", inline=True)
    embed.add_field(name="Dips", value="Do some dips (<3 dips)", inline=True)
    await ctx.send(embed=embed)

# information about pushups
@client.command() 
async def weightedpushups(ctx):
    embed = discord.Embed(
        title= "How to do Weighted pushups",
        color = discord.Color.purple(),
        description = "Just add weights (book in bags) in Normal pushups"
    )
    embed.set_image(url='https://media.discordapp.net/attachments/813017363443482645/825259653846925342/SmartVapidCaribou-small.gif')
    await ctx.send(embed=embed)

# information about dips
@client.command() 
async def dips(ctx):
    embed = discord.Embed(
        title= "How to do Dips",
        color = discord.Color.purple(),
        description = "See in GIF below"
    )
    embed.set_image(url='')
    await ctx.send(embed=embed)

# information about pull
@client.command() 
async def pull(ctx):
    embed = discord.Embed(
        title= "Pull Day Workouts",
        color = discord.Color.purple(),
        description = "We have some pull day workouts here:-"
    )
    embed.add_field(name="Pullups", value="Do (<3 pullups)", inline=True)
    embed.add_field(name="Bicep curls", value="Do (<3 bicepcurl)", inline=True)

    await ctx.send(embed=embed)

# information about pullups
@client.command() 
async def pullups(ctx):
    embed = discord.Embed(
        title= "How to do Pullups",
        color = discord.Color.purple(),
        description = "See in GIF below"
    )
    embed.set_image(url='https://media.discordapp.net/attachments/813017363443482645/825262153883451422/4Fhl.gif')
    
    await ctx.send(embed=embed)

# information about bicepcurls
@client.command() 
async def bicepcurls(ctx):
    embed = discord.Embed(
        title= "How to do bicepcurls",
        color = discord.Color.purple(),
        description = "See in GIF below (warning don't use cat)"
    )
    embed.set_image(url='https://media.discordapp.net/attachments/813017363443482645/825276894098227240/9ViG.gif')  
    await ctx.send(embed=embed)

# information about squats
@client.command() 
async def squats(ctx):
    embed = discord.Embed(
        title= "How to do Squats",
        color = discord.Color.purple(),
        description = "See in GIF below (warning dog compulsary)"
    )
    embed.set_image(url='https://media.discordapp.net/attachments/813017363443482645/825276133524242472/1q0G.gif')    
    await ctx.send(embed=embed)


# Test command, tells the latency of the bot
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! 🏓 {round(client.latency*1000)}ms')


async def check_reminder():
    """a function loop for checking reminder every sec.
    Args:
        now: current time
          x: workout times
    """
    while(True):
        await asyncio.sleep(1)
        now = datetime.now()
        current_time  = now.strftime("%H:%M:%S")
        x = dt.time(5, 30, 0)
        if current_time == str(x):
            channel = client.get_channel(813017363443482645)
            await channel.send(f'<@&{825697640560853004}> its time to workout!!')
        

client.loop.create_task(check_reminder())
client.run(get_token())

