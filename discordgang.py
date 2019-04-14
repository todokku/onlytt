import discord
from discord.ext.commands import Bot
from discord.ext import commands
import time
import os

bot = discord.Client()
bot = commands.Bot(command_prefix = '//')

bot.run(os.getenv('TOKEN'))
