import discord
from discord import User
from discord import Game
from discord.utils import get
from discord.ext.commands import Bot, guild_only
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CheckFailure, BadArgument
from discord.ext import commands
from discord import Member
from discord import emoji
import random
import o
import asyncio

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    game = discord.Activity(name="Youtubers Discord[beta]", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        g = await ctx.send('```Unknown command try ;help```')
        await asyncio.sleep(3)
        await g.delete()

@bot.command()
async def ping(ctx):
    await ctx.send('{} is my ping sir!'.format(round(bot.latency, 1)))


@bot.command(name='8ball')
async def _8ball(ctx, reason=None):
    if reason is None:
        f = await ctx.send('Please ask a question also')
        await asyncio.sleep(3)
        await f.delete()
        await ctx.message.delete()
    elif 'your' in reason.content.strip().lower():
        await ctx.send('NOU')
    else:
        await ctx.send(random.choice(['```Maybe```',
                                      '```Yes```',
                                      '```No```',
                                      '```100%```',
                                      '```Scince says **Yes** ```',
                                      '```Scince says **No**```',
                                      '```Can\'t say```']))

@bot.command()
async def say(ctx, *,reason=None):
    await ctx.author.send_message(reason)

@bot.event
async def on_message(message):
    ctx = message.channel
    if 'cry thon' in message.content.strip().lower():
        await ctx.send('CRY YA ASS OF NAB NOW GET THE FUCK OUT')
    elif 'thon' in message.content.strip().lower():
        if message.author.id == '618340711749910539':
            return
        else:
            await ctx.send('IMA FR BEAT U UP WITH THE THANOS HAMMER')
    elif 'hi itzbot' in message.content.strip().lower():
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
    
bot.run(os.getenv('TOKEN'))
