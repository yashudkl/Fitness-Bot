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


client = commands.Bot(command_prefix = "<3 ")   # global bot delcaration.

def get_routine(week_day):
    """
    get details about routines from routine.json
    Takes:
        week_day = week of the day eg: sunday, monday tuesday.
    Args:
        openfile, json_object, pairs = variables req by json module (honestly idk what it does). 
        today_routine                = return value containing informations about the workouts.
    Returns:
        wokrout, video, thumnail_link, gif_link, rounds, etc.
    """

    with open('routine.json', 'r') as openfile:
        json_object = json.load(openfile)
        pairs = json_object.items()
        
        routine_title = json_object[str(week_day)]['title']
        _1_title = json_object[str(week_day)]['1']['name']
        _1_reps  = json_object[str(week_day)]['1']['reps']
        _1_link  = json_object[str(week_day)]['1']['link']

        _2_title = json_object[str(week_day)]['2']['name']
        _2_reps  = json_object[str(week_day)]['2']['reps']
        _2_link  = json_object[str(week_day)]['2']['link']

        _3_title = json_object[str(week_day)]['3']['name']
        _3_reps  = json_object[str(week_day)]['3']['reps']
        _3_link  = json_object[str(week_day)]['3']['link']

        _4_title = json_object[str(week_day)]['4']['name']
        _4_reps  = json_object[str(week_day)]['4']['reps']
        _4_link  = json_object[str(week_day)]['4']['link']

        _5_title = json_object[str(week_day)]['5']['name']
        _5_reps  = json_object[str(week_day)]['5']['reps']
        _5_link  = json_object[str(week_day)]['5']['link']

        _6_title = json_object[str(week_day)]['6']['name']
        _6_reps  = json_object[str(week_day)]['6']['reps']
        _6_link  = json_object[str(week_day)]['6']['link']

    return routine_title, _1_title, _1_reps, _1_link, _2_title, _2_reps, _2_link, _3_title, _3_reps, _3_link, _4_title, _4_reps, _4_link, _5_title, _5_reps, _5_link, _6_title, _6_reps, _6_link

async def print_routine(ch):
    """
    displays the schedule of the day (today).
    Args:
        cr_year, cr_month, cr_day    = Current year/month/day.
        week_days                    = array of weeks (starts with monday and ends with monday to fit internation week format).
        week_num                     = a int which acts as index to get current week from week_days array.
        title......**                = retuned value which contains information about the embed.

        schedule_embed               = embed containing info about todays schedule.
    """
    
    channel = client.get_channel(ch)
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    cr_year   = datetime.today().strftime('%Y')
    cr_month  = datetime.today().strftime('%m')
    cr_day    = datetime.today().strftime('%d')
    week_num  = dt.date(int(cr_year), int(cr_month), int(cr_day)).weekday()
    print(week_num)

    if week_num == 4: #if its friday (rest day)
        rest_embed = discord.Embed(
            title = f'🛌: Rest! ' ,
            color = discord.Color.purple(),
            description = 'Great! You did awsome! Lets get some rest, and call this a skip day today!'
        )
        rest_embed.set_image(url = 'https://github.com/Eclipsu/Fitness-Bot/blob/MAIN/assets/rest.gif')
        rest_embed.set_thumbnail(url = 'https://github.com/Eclipsu/Fitness-Bot/blob/MAIN/assets/rest.webp')
        await channel.send(embed = rest_embed)
        return

    title,_1_title, _1_reps, _1_link,  _2_title, _2_reps, _2_link, _3_title, _3_reps, _3_link, _4_title, _4_reps, _4_link, _5_title, _5_reps, _5_link, _6_title, _6_reps, _6_link = get_routine(week_days[week_num])
    schedule_embed = discord.Embed(
        title = f'📋 {title}',
        color = discord.Color.purple(),
        description = 'Do 4 rounds of each reps!'
    )
    schedule_embed.add_field(name = _1_title,  value  = f"[{_1_reps}]({_1_link}) reps", inline = True)
    schedule_embed.add_field(name = _2_title,  value  = f"[{_2_reps}]({_2_link}) reps", inline = True)
    schedule_embed.add_field(name = _3_title,  value  = f"[{_3_reps}]({_3_link}) reps", inline = True)
    schedule_embed.add_field(name = _4_title,  value  = f"[{_4_reps}]({_4_link}) reps", inline = True)
    schedule_embed.add_field(name = _5_title,  value  = f"[{_5_reps}]({_5_link}) reps", inline = True)
    schedule_embed.add_field(name = _6_title,  value  = f"[{_6_reps}]({_6_link}) reps", inline = True)
    schedule_embed.set_footer(text = 'DM us for more info')

    await channel.send(embed = schedule_embed)


# bot on ready function
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('<3/ Workout'))
    print(f'{client.user.name} deployed!')


@client.command()
async def schedule(ctx):
    """
    displays the schedule of the day (today).
    Calls:
        print_routine()
    Args:
        channe_id = channel id 
    """

    channel_id = ctx.channel.id
    await print_routine(ch = int(channel_id))

# lists outs schedule of the week
@client.command()
async def routine(ctx):
    """
    Displays routine of the whole week.
    Args:
        routine_embed = Embed with information about the routine of the whole week.
    """

    routine_embed = discord.Embed(
        title = "\📋: Routine",
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

# @client.command() 
# async def schedule(ctx):
#     embed = discord.Embed(
#         title= "Schedule ",
#         color = discord.Color.purple(),
#         description = "Follow the Schedule provided."
#         )
#     embed.add_field(name="Weight gain", value="Workouts:-Push , Pull , Leg", inline=True)
#     embed.add_field(name="Fat Loss", value="Workouts:- Cardio ", inline=True)
#     embed.set_image(url='https://th.bing.com/th/id/OIP.1NfnV_pv0VI4QaQJBgHdVQHaEc?w=300&h=180&c=7&o=5&pid=1.7')
#     embed.set_thumbnail(url='https://th.bing.com/th/id/OIP.W1Sy8iy9IUMxY5nxgUVeZwHaHa?w=182&h=182&c=7&o=5&pid=1.7')
#     await ctx.send(embed=embed)

# information about pull
# @client.command() 
# async def push(ctx):
#     embed = discord.Embed(
#         title= "Push Day Workouts",
#         color = discord.Color.purple(),
#         description = "We have some push day workouts here:-"
#     )
#     embed.add_field(name="Weighted Pushups", value="Do Pushups (<3 weightedpushups)", inline=True)
#     embed.add_field(name="Dips", value="Do some dips (<3 dips)", inline=True)
#     await ctx.send(embed=embed)

# # information about pushups
# @client.command() 
# async def weightedpushups(ctx):
#     embed = discord.Embed(
#         title= "How to do Weighted pushups",
#         color = discord.Color.purple(),
#         description = "Just add weights (book in bags) in Normal pushups"
#     )
#     embed.set_image(url='https://media.discordapp.net/attachments/813017363443482645/825259653846925342/SmartVapidCaribou-small.gif')
#     await ctx.send(embed=embed)

# # information about dips
# @client.command() 
# async def dips(ctx):
#     embed = discord.Embed(
#         title= "How to do Dips",
#         color = discord.Color.purple(),
#         description = "See in GIF below"
#     )
#     embed.set_image(url='')
#     await ctx.send(embed=embed)

# # information about pull
# @client.command() 
# async def pull(ctx):
#     embed = discord.Embed(
#         title= "Pull Day Workouts",
#         color = discord.Color.purple(),
#         description = "We have some pull day workouts here:-"
#     )
#     embed.add_field(name="Pullups", value="Do (<3 pullups)", inline=True)
#     embed.add_field(name="Bicep curls", value="Do (<3 bicepcurl)", inline=True)

#     await ctx.send(embed=embed)

# # information about pullups
# @client.command() 
# async def pullups(ctx):
#     embed = discord.Embed(
#         title= "How to do Pullups",
#         color = discord.Color.purple(),
#         description = "See in GIF below"
#     )
#     embed.set_image(url='https://media.discordapp.net/attachments/813017363443482645/825262153883451422/4Fhl.gif')
    
#     await ctx.send(embed=embed)

# # information about bicepcurls
# @client.command() 
# async def bicepcurls(ctx):
#     embed = discord.Embed(
#         title= "How to do bicepcurls",
#         color = discord.Color.purple(),
#         description = "See in GIF below (warning don't use cat)"
#     )
#     embed.set_image(url='https://media.discordapp.net/attachments/813017363443482645/825276894098227240/9ViG.gif')  
#     await ctx.send(embed=embed)

# # information about squats
# @client.command() 
# async def squats(ctx):
    # embed = discord.Embed(
    #     title= "How to do Squats",
    #     color = discord.Color.purple(),
    #     description = "See in GIF below (warning dog compulsary)"
    # )
    # embed.set_image(url='https://media.discordapp.net/attachments/813017363443482645/825276133524242472/1q0G.gif')    
    # await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    """
    Displays the latency of the bot (TEST COMMAND)
    """
    
    await ctx.send(f'Pong! 🏓 {round(client.latency*1000)}ms')

async def check_reminder():
    """
    a function loop for checking reminder every sec.
    Args:
        now: current time
          x: workout times
    """
    
    while(True):
        await asyncio.sleep(1)
        now = datetime.now()
        current_time  = now.strftime("%H:%M:%S")
        x = dt.time(11, 16, 0)
        if current_time == str(x):
            print('time')
            channel = client.get_channel(813017363443482645)
            await channel.send(f'<@&{825697640560853004}> Its time to grind!\n your schedule for today: ')
            await print_routine(ch = 813017363443482645)
        
client.loop.create_task(check_reminder())
client.run(get_token())

