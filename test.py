import discord
from discord.ext import commands
import asyncio
from datetime import datetime
import datetime as dt

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    # status of bot
    await client.change_presence(activity=discord.Game('<3/ Workout'))
    print(f'{client.user.name} deployed!')

@client.command()
async def remind(ctx, time, *, about):
    await ctx.send(f'Okey, **{ctx.author.mention}**, you will be reminder after {time}secs about {about}')
    await asyncio.sleep(float(time))
    await ctx.send(f'{ctx.author.mention}! you gotta {about}')

# import datetime

# x = datetime.time(12, 0, 0)
# print(x) 


async def check_reminder():
    while(True):
        await asyncio.sleep(1)
        now = datetime.now()
        current_time  = now.strftime("%H:%M:%S")
        x = dt.time(17, 40, 0)
        if current_time == str(x):
            channel = client.get_channel(813017363443482645)
            await channel.send(f'<@&{825697640560853004}> its time to workout!!')
            # print("YES")
        else:
            print("NO")


client.loop.create_task(check_reminder())


client.run("ODIyMjcxMjM3Nzk4ODg3NDI0.YFP1xA.KX75SdHwkOra-bVKkr4Oz71LZh4")
