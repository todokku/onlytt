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
bot.remove_command('help')

@bot.event
async def on_ready():
    game = discord.Activity(name="GodsDevil Network", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.idle, activity=game)

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

@bot.command(name='clear')
@commands.has_permissions(ban_members=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    mg = await ctx.send('```Deleted {} Messages```'.format(amount))
    await asyncio.sleep(3)
    await mg.delete()
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        a = await ctx.send('```U don\'t have the permissions to use clear command```')
        await asyncio.sleep(3)
        await a.delete()
    else:
        mag = await ctx.send('```p/clear [amount]```')
        await asyncio.sleep(2)
        await mag.delete()
@bot.command()
async def rps(ctx, arg=None):
    y = bot.get_channel(559253532759425044)
    x = (559253532759425044)
    channel = bot.get_channel(559253532759425044)
    if ctx.channel.id != x:
        abc = await ctx.send('Please write this command in {}'.format(y.mention))
        await asyncio.sleep(3)
        await abc.delete()
        await ctx.message.delete()
    elif arg is None:
        ctx.send('```p/rps [r or p or s], r for rock, p for paper, s for scissors```')
    elif 'p' in arg:
        await ctx.send(random.choice(['Rock, You won',
                                      ':newspaper: , Its a tie',
                                      ':scissors: , I won']))
    elif 'r' in arg:
        await ctx.send(random.choice(['Rock, Its a tie',
                                      ':newspaper: , I won',
                                      ':scissors: , You won']))
    elif 's' in arg:
        await ctx.send(random.choice(['Rock, I won',
                                          ':newspaper: , You won',
                                          ':scissors: , Its a tie']))
@bot.command(name='8ball')
async def _8ball(ctx, arg=None):
    y = bot.get_channel(559253532759425044)
    x = (559253532759425044)
    channel = bot.get_channel(559253532759425044)
    if ctx.channel.id != x:
        abc = await ctx.send('Please write this command in {}'.format(y.mention))
        await asyncio.sleep(3)
        await abc.delete()
        await ctx.message.delete()
    elif arg is None:
        f = await ctx.send('Please ask a question also')
        await asyncio.sleep(3)
        await f.delete()
        await ctx.message.delete()
    else:
        await ctx.send(random.choice(['```Maybe```',
                                      '```Yes```',
                                      '```No```',
                                      '```100%```',
                                      '```Scince says **Yes** ```',
                                      '```Scince says **No**```',
                                      '```Can\'t say```']))



@bot.group(name='help')
async def help(ctx):
    y = bot.get_channel(559253532759425044)
    x = (559253532759425044)
    if ctx.channel.id != x:
        abc = await ctx.send('Please write this command in {}'.format(y.mention))
        await asyncio.sleep(3)
        await abc.delete()
        await ctx.message.delete()
    else:
        if ctx.invoked_subcommand is None:
            await ctx.send(embed = discord.Embed(title='Help Command', colour=discord.Colour(0x7ed321), description=' Categories  \n `Other` - Commands for soem extra stuff (included some important stuff) \n  `Fun -` Game commands for Everyone \n'))

@bot.group(name='enable')
async def enable(ctx):
    y = bot.get_channel(559253532759425044)
    x = (559253532759425044)
    channel = bot.get_channel(559253532759425044)
    if ctx.channel.id != x:
        abc = await ctx.send('Please write this command in {}'.format(y.mention))
        await asyncio.sleep(3)
        await abc.delete()
        await ctx.message.delete()
    else:
        if ctx.invoked_subcommand is None:
            await ctx.send('```p/enable (role) and do p/enable info for info of the available roles```')

@enable.command(pass_context=True)
async def info(ctx):
    y = bot.get_channel(559253532759425044)
    x = (559253532759425044)
    if ctx.channel.id != x:
        abc = await ctx.send('Please write this command in {}'.format(y.mention))
        await asyncio.sleep(3)
        await abc.delete()
        await ctx.message.delete()
    else:
        await ctx.send(embed = discord.Embed(title='roles Info', colour=discord.Colour(0x7ed321), description='**Roles** \n `Notify` - If this is enabled you get Notified/Pinged if there is any announcments/new staff member \n `More Comming Soon...`'))




@enable.command(pass_context=True)
async def notify(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Notification")
    y = bot.get_channel(559253532759425044)
    x = (559253532759425044)
    if ctx.channel.id != x:
        abc = await ctx.send('Please write this command in {}'.format(y.mention))
        await asyncio.sleep(3)
        await abc.delete()
        await ctx.message.delete()                                   
    elif role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await  ctx.send('```Removed notification role```')
    else:
        await ctx.author.add_roles(role)
        await ctx.send('```Added notification role```')

@help.command(pass_context=True)
async def moderation(ctx):
    await ctx.send('The command is not added yet')

@help.command(pass_context=True)
async def other(ctx):
    y = bot.get_channel(559253532759425044)
    x = (559253532759425044)
    if ctx.channel.id != x:
        abc = await ctx.send('Please write this command in {}'.format(y.mention))
        await asyncio.sleep(3)
        await abc.delete()
        await ctx.message.delete()
    else:
        await ctx.send(embed = discord.Embed(title='Other Stuffs', colour=discord.Colour(0x7ed321), description='`p/enable` - adds some special roles do p/enable info for more information \n `More Comming Soon...`'))

bot.run(os.getenv('TOKEN'))
