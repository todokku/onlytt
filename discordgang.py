import discord
from discord.ext.commands import Bot
from discord.ext import commands
import time
import os

bot = discord.Client()
bot = commands.Bot(command_prefix = 'p/')

@bot.event
async def on_ready():
    game = discord.Activity(name="GodsDevil Network", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.dnd, activity=game)


bot.run(os.getenv('TOKEN'))
