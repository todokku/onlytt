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
import urllib.request
import random
import json
import asyncio
import os

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    game = discord.Activity(name="Itzdvbravo's Server", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.dnd, activity=game)

async def background_task():
    await bot.wait_until_ready()
    channel = bot.get_channel(683711122808766524)
    pong = await channel.fetch_message(683960600988352512)
    while not bot.is_closed():
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC0DdJlY_b6ySlOp3YtDjvxA&key=AIzaSyCsfglSpz_K17iqA_ezeA5oD01pmhSerZ0").read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        vid = json.loads(data)["items"][0]["statistics"]["videoCount"]
        view = json.loads(data)["items"][0]["statistics"]["viewCount"]
        embed=discord.Embed(title="Click to view my channel", url="https://www.youtube.com/channel/UC0DdJlY_b6ySlOp3YtDjvxA")
        embed.set_author(name="Itzdvbravo's Youtube Live Status", icon_url="https://cdn.discordapp.com/avatars/533894799577841665/d44545c7c57ef5bde8ffa6a35c75e269.png?size=256")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/683648447903039500/683700959473565726/minecraft-1469255_1920.png")
        embed.add_field(name="Subsribers", value="{}".format(int(subs)), inline=True)
        embed.add_field(name="Total Veiws", value="{}".format(int(view)), inline=True)
        embed.add_field(name="Total Videos", value="{}".format(int(vid)), inline=True)
        embed.set_footer(text="*Updates every 10 minutes*")
        bod=discord.Embed(title="Click to view my channel", url="https://www.youtube.com/channel/UC0DdJlY_b6ySlOp3YtDjvxA")
        bod.set_author(name="Itzdvbravo's Youtube Live Status", icon_url="https://cdn.discordapp.com/avatars/533894799577841665/d44545c7c57ef5bde8ffa6a35c75e269.png?size=256")
        bod.set_thumbnail(url="https://cdn.discordapp.com/attachments/683648447903039500/683700959473565726/minecraft-1469255_1920.png")
        bod.add_field(name="Subsribers", value="{}".format(int(subs)), inline=True)
        bod.add_field(name="Total Veiws", value="{}".format(int(view)), inline=True)
        bod.add_field(name="Total Videos", value="{}".format(int(vid)), inline=True)
        bod.set_footer(text="*Updates every 10 minutes*")
        await pong.edit(embed=bod)
        await asyncio.sleep(600)
        await pong.edit(embed=embed)
        await asyncio.sleep(600)
    
@bot.command()
async def check(ctx, arg=None):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC0DdJlY_b6ySlOp3YtDjvxA&key=AIzaSyCsfglSpz_K17iqA_ezeA5oD01pmhSerZ0").read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    vid = json.loads(data)["items"][0]["statistics"]["videoCount"]
    view = json.loads(data)["items"][0]["statistics"]["viewCount"]
    if arg == None:
        await ctx.send("Please use `;check <option>`, options are *subs* and *videocount/vc* and *veiws*")
    elif arg == 'subs':
        await ctx.send("Itzdvbravo has {} Subscribers".format(int(subs)))
    elif arg == 'videocount':
        await ctx.send("Itzdvbravo has uploaded {} videos till now".format(int(vid)))
    elif arg == 'vc':
        await ctx.send("Itzdvbravo has uploaded {} videos till now".format(int(vid)))
    elif arg == 'views':
        await ctx.send("Itzdvbravo, in total he has {} views, in all his videos".format(int(view)))
    else:
        await ctx.send("Please use `;check <option>`, options are *subs* and *videocount/vc* and *veiws*")    

bot.loop.create_task(background_task())        
bot.run(os.getenv('TOKEN'))
