import discord
from discord.ext import commands

bot = discord.Client()
bot = commands.Bot(command_prefix = '//')

bot.run(os.getenv('TOKEN'))
