import discord                                  # discord.py module.
from discord.ext import commands, tasks         # discord.py commands module.
import asyncio                                  # time.sleep function.
import json                                     # json module for reading and writing into json file(s).
from datetime import datetime                   # datetime for getting current time. 
import datetime as dt                           # datetime for setting time.



client = commands.Bot(command_prefix = "<3 ")   # global bot delcaration.

#for Attendance reaction
@client.command(pass_contest=True)
async def testi(ctx):
    await ctx.message.add_reaction("👍🏿") #adding reaction to the comand
    embed = discord.Embed(
        title = "Attendance 📋",
        description = " React below to Mark your attendance  ",
        color= discord.Color.purple()


    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("✅") #adding reaction to embed

#taking user 
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['✅']
#checking condition
    while True:

        reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
        if str(reaction.emoji) == "✅":
                await ctx.send('{} Done!'.format(user))
                

    else:
        await msg.remove_reaction(reaction, user) 
    
    






     


  

    
    


def get_routine():
    """
    get details about routines from routine.json
    Args:
        openfile, json_object, pairs = variables req by json module (honestly idk what it does). 
        cr_year, cr_month, cr_day    = Current year/month/day.
        week_days                    = array of weeks (starts with monday and ends with monday to fit internation week format).
        week_num                     = a int which acts as index to get current week from week_days array.
        today_routine                = return value containing informations about the workouts.
    Returns:
        wokrout, video, thumnail_link, gif_link, rounds, etc.
    """

    with open('routine.json', 'r') as openfile:
        json_object = json.load(openfile)
        pairs = json_object.items()

        week_days = ['monday', 'tuesday', 'wednesday', 'thirsday', 'friday', 'saturday', 'sunday']
        cr_year = datetime.today().strftime('%Y')
        cr_month = datetime.today().strftime('%m')
        cr_day = datetime.today().strftime('%d')
        week_num  = dt.date(int(cr_year), int(cr_month), int(cr_day)).weekday() 

        routine_title = json_object[str(week_days[week_num])]['title']
        _1_title = json_object[str(week_days[week_num])]['1']['name']
        _1_reps  = json_object[str(week_days[week_num])]['1']['reps']
        _1_link  = json_object[str(week_days[week_num])]['1']['link']

        _2_title = json_object[str(week_days[week_num])]['2']['name']
        _2_reps  = json_object[str(week_days[week_num])]['2']['reps']
        _2_link  = json_object[str(week_days[week_num])]['2']['link']

        _3_title = json_object[str(week_days[week_num])]['3']['name']
        _3_reps  = json_object[str(week_days[week_num])]['3']['reps']
        _3_link  = json_object[str(week_days[week_num])]['3']['link']

        _4_title = json_object[str(week_days[week_num])]['4']['name']
        _4_reps  = json_object[str(week_days[week_num])]['4']['reps']
        _4_link  = json_object[str(week_days[week_num])]['4']['link']

        _5_title = json_object[str(week_days[week_num])]['5']['name']
        _5_reps  = json_object[str(week_days[week_num])]['5']['reps']
        _5_link  = json_object[str(week_days[week_num])]['5']['link']

        _6_title = json_object[str(week_days[week_num])]['6']['name']
        _6_reps  = json_object[str(week_days[week_num])]['6']['reps']
        _6_link  = json_object[str(week_days[week_num])]['6']['link']

        _7_title = json_object[str(week_days[week_num])]['7']['name']
        _7_reps  = json_object[str(week_days[week_num])]['7']['reps']
        _7_link  = json_object[str(week_days[week_num])]['7']['link']
    return routine_title, _1_title, _1_reps, _1_link, _2_title, _2_reps, _2_link, _3_title, _3_reps, _3_link, _4_title, _4_reps, _4_link, _5_title, _5_reps, _5_link, _6_title, _6_reps, _6_link, _7_title, _7_reps, _7_link




# bot on ready function
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('<3/ Workout'))
    print(f'{client.user.name} deployed!')


@client.command()
async def schedule(ctx):
    title,_1_title, _1_reps, _1_link,  _2_title, _2_reps, _2_link, _3_title, _3_reps, _3_link, _4_title, _4_reps, _4_link, _5_title, _5_reps, _5_link, _6_title, _6_reps, _6_link, _7_title, _7_reps, _7_link = get_routine()
    schedule_embed = discord.Embed(
        title = "📋",
        color = discord.Color.purple(),
        description = 'Do all reps for 4 rounds each!'
    )
    schedule_embed.add_field(name = _1_title,  value  = f"{_1_reps} reps", inline = True)
    schedule_embed.add_field(name = _2_title,  value  = f"{_2_reps} reps", inline = True)
    schedule_embed.add_field(name = _3_title,  value  = f"{_3_reps} reps", inline = True)
    schedule_embed.add_field(name = _4_title,  value  = f"{_4_reps} reps", inline = True)
    schedule_embed.add_field(name = _5_title,  value  = f"{_5_reps} reps", inline = True)
    schedule_embed.add_field(name = _6_title,  value  = f"{_6_reps} reps", inline = True)
    
    await ctx.send(embed = schedule_embed)

# lists outs schedule of the week
@client.command()
async def routine(ctx):
    routine_embed = discord.Embed(
        title = "\📋: Routine",
        color = discord.Color.purple(),
        description = "7 days, 6 grind, 1 rest."
    )
    routine_embed.add_field(name = "Sun",  value  = "Push day", inline = True)
    routine_embed.add_field(name = "Mon",  value  = "Pull. day", inline = True)
    routine_embed.add_field(name = "Tues", value  = "Leg day", inline = True)
    routine_embed.add_field(name = "Wed",  value  = "Abs day", inline = True)
    routine_embed.add_field(name = "Thrs", value  = "Pull day", inline = True)
    routine_embed.add_field(name = "Sat",  value  = "Pull day")
    routine_embed.set_thumbnail(url = 'https://media4.giphy.com/media/3o7qE4gcYTW1zZPkre/source.gif')
    routine_embed.set_footer(text = 'Friday rest  🛌')
    await ctx.send(embed = routine_embed)








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
client.run("Tero bau")
