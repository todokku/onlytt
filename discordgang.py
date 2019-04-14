import discord
from discord.ext.commands import CommandNotFound
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
from discord import Member
from discord import emoji
import random
import asyncio
import os

bot = discord.Client()
bot = commands.Bot(command_prefix = 'p/')

@bot.event
async def on_ready():
    game = discord.Activity(name="GodsDevil Network", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        g = await ctx.send('```Unknown command try p/help```')
        await asyncio.sleep(3)
        await g.delete()
    else:
        raise error

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "Starter")
    channel = bot.get_channel(559254248550957057) 
    guild = member.guild
    message ='hello{} welcome to our {} server. Please read the rules so u don\'t get in trouble'.format(member.mention, guild.name)
    await channel.send(message)
    await member.add_roles(role)
    await member.send('Welcome {}, Please read the rules and accept the rules by clicking on :white_check_mark: or decline it by clicking on :negative_squared_cross_mark:, Only after that u can procced in the server'.format(member.mention))

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(559254248550957057)
    guild = member.guild
    await channel.send(random.choice(['**{}#{}** Has left our server.NOOOOOOOOOOOOOOOOOOOOOOOOOO'.format(member.name, member.discriminator),
                                      '**{}#{}** Has left our server. Guess they were just air'.format(member.name, member.discriminator),
                                      '**{}#{}** Has left our server. Who cares'.format(member.name, member.discriminator),
                                      '**{}#{}** Has left our server. L'.format(member.name, member.discriminator),
                                      '**{}#{}** Has left our server. What a loser'.format(member.name, member.discriminator)]))

bot.run(os.getenv('TOKEN'))
