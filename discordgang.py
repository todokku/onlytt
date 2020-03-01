import discord
from discord.ext import commands
from discord import User
from discord import Game
from discord.utils import get
from discord.ext.commands import Bot, guild_only
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CheckFailure, BadArgument
from discord.ext import commands
from discord import Member
from discord import emoji
import datetime
import random
import asyncio
import os

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    game = discord.Activity(name="Itzdvbravo's Server", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.command()
async def check(ctx, arg=None):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC0DdJlY_b6ySlOp3YtDjvxA&key=AIzaSyCsfglSpz_K17iqA_ezeA5oD01pmhSerZ0").read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    vid = json.loads(data)["items"][0]["statistics"]["videoCount"]
    veiw = json.loads(data)["items"][0]["statistics"]["viewCount"]
    if arg == None:
        await ctx.send("Please use `;check <option>`, options are *subs* and *videocount/vc* and *veiws*")
    elif arg == 'subs':
        await ctx.send("Itzdvbravo has {} Subscribers".format(int(subs)))
    elif arg == 'videocount':
        await ctx.send("Itzdvbravo has uploaded {} videos till now".format(int(vid)))
    elif arg == 'vc':
        await ctx.send("Itzdvbravo has uploaded {} videos till now".format(int(vid)))
    elif arg == 'veiws':
        await ctx.send("Itzdvbravo, in total he has {} veiws, in all his videos".format(int(veiw)))
    else:
        await ctx.send("Please use `;check <option>`, options are *subs* and *videocount/vc* and *veiws*")    

bot.run(os.getenv('TOKEN'))
