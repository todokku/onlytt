import discord
from discord.ext.commands import CommandNotFound
from discord import Game
from discord.ext import commands
from discord import Member
from discord import emoji
import random
import asyncio

bot = commands.Bot(command_prefix='p/')
bot.remove_command('help')

@bot.event
async def on_ready():
    game = discord.Activity(name="GodsDevil Network", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.online, activity=game)

bot.run(os.getenv('TOKEN'))
