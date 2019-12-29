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

bot = commands.Bot(command_prefix=';')
token = 'NjYwNzYyNTQ1OTcxMjY1NTUy.XghlKg.mrt6KPIQodz4RQEpe--JFaQtDGE'

@bot.command()
async def ping(ctx):
    await ctx.send('{} is my ping sir!'.format(round(bot.latency, 1)))

@bot.command()
async def hi(ctx):
    await ctx.send('hi')

@bot.event
async def on_ready():
    game = discord.Activity(name="Itzdvbravo", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.event
async def on_message(message):
    ctx = message.channel
    if 'go cry bot tester' in message.content.strip().lower():
        await ctx.send(random.choice(['NO CRY YA ASS OF NAB',
                                      'Breh, No you go cry \n My rymes gonna make you fry \n You won\'t be able to even tho you try \n Now you gonna cry']))
    elif 'bot tester your gay' in message.content.strip().lower():
        await ctx.send('IMA FR BEAT U UP WITH THE THANOS HAMMER')
    elif 'hi bot tester' in message.content.strip().lower():
        await ctx.send('Hi {}'.format(message.author.mention))
        await asyncio.sleep(0.9)
        await ctx.send('Need help?')
        msg = await bot.wait_for('message', timeout=30)
        if 'yes' in msg.content.strip().lower():
            await ctx.send(random.choice(['I won\'t help you LOL',
                                          'HELL NO, i won\'t help a nab like u',
                                          'ok, if u need help, please do /ban me',
                                          'L NO']))
            await asyncio.sleep(1.5)
            await ctx.send('AH ok, do `;help`')
        elif 'no' in msg.content.strip().lower():
            await ctx.send('ok bye NAB')
    else:
        await bot.process_commands(message)


@bot.command()
async def suggest(ctx,*,arg=None):
    channel = bot.get_channel(660750866713804880)
    member = ctx.message.author
    if arg == None:
        await ctx.send('Suggest us something idiot')
    else:
        embed=discord.Embed(title="Suggestion: {}".format(arg), description="", color=0x1d04f4)
        embed.set_author(name="{}#{}".format(member.name, member.discriminator), icon_url='{}'.format(member.avatar_url))
        embed.set_footer(text="")
        await channel.send(embed=embed)
    

bot.run(token)
