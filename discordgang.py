import discord
from discord.ext.commands import CommandNotFound, BadArgument, CheckFailure
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game
from discord import Member
from discord import emoji
from json import load
import random
import asyncio
import os

bot = discord.Client()
bot = commands.Bot(command_prefix = '/')
bot.remove_command('help')

@bot.event
async def on_ready():
    game = discord.Activity(name="GodsDevil Network", type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        g = await ctx.send('```Unknown command try /help```')
        await asyncio.sleep(3)
        await g.delete()
    else:
        raise error

@bot.event
async def on_member_join(member):
    guild = member.guild
    role = discord.utils.get(member.guild.roles, name='Member')
    role1 = discord.utils.get(member.guild.roles, name='Applyes')
    a = bot.get_channel(565632081569382415)
    channel = bot.get_channel(559254248550957057)
    await member.add_roles(role1)
    await member.add_roles(role)    
    await member.send('Hello {} Welcome to GodsDevil Network,**Please Read Our Rules**'.format(member.mention))
    await channel.send('Hello {} \n Welcome to GodsDevil Network \n please read our rules in {}'.format(member.mention, a.mention))

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
async def clear(ctx, amount: int):
    if get(ctx.message.author.role, name="Co-Owner"):
        await ctx.channel.purge(limit=amount)
        await asyncio.sleep(1)
        mg = await ctx.send('```Deleted {} Messages```'.format(amount))
        await asyncio.sleep(3)
        await mg.delete()
    elif not get(ctx.message.author.role, name="Co-Owner"):
        await ctx.send('```You don\'t have perms to use this command```')
    else:
        mag = await ctx.send('```/clear [amount]```')
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
        ctx.send('```/rps [r or p or s], r for rock, p for paper, s for scissors```')
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
async def _8ball(ctx, reason=None):
    y = bot.get_channel(559253532759425044)
    x = (559253532759425044)
    channel = bot.get_channel(559253532759425044)
    if ctx.channel.id != x:
        abc = await ctx.send('Please write this command in {}'.format(y.mention))
        await asyncio.sleep(3)
        await abc.delete()
        await ctx.message.delete()
    elif reason is None:
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
            await ctx.send('```/enable (role) and do /enable info for info of the available roles```')

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
        await ctx.send(embed = discord.Embed(title='Other Stuffs', colour=discord.Colour(0x7ed321), description='`/enable` - adds some special roles do /enable info for more information \n `More Comming Soon...`'))

@help.command(pass_context=True)
async def fun(ctx):
    y = bot.get_channel(559253532759425044)
    x = (559253532759425044)
    if ctx.channel.id != x:
        abc = await ctx.send('Please write this command in {}'.format(y.mention))
        await asyncio.sleep(3)
        await abc.delete()
        await ctx.message.delete()
    else:
        await ctx.send(embed = discord.Embed(title='Fun Commands', colour=discord.Colour(0x7ed321), description='`/8ball`- Ask a question the 8ball will answer it with yes or no \n `/rps`- Rock paper scissors game /rps (r/p/s)'))

@bot.command(name='announce')
async def announce(ctx, *,arg2):
    role = discord.utils.get(ctx.guild.roles, name="Notification")
    if get(ctx.message.author.role, name="Co-Owner"):
        await ctx.message.delete()
        await ctx.send(embed = discord.Embed(title="Announcement", colour=discord.Colour(0x7ed321), description="{} \n {}".format(role.mention, arg2)))
    else:
        await ctx.send('```You don\'t have perms to use this command```')
        
@bot.command()
async def kick(ctx, member: discord.Member, *,reason=None):
    d = datetime.datetime.now()
    embed=discord.Embed(title='**Kicked By:** {}#{}'.format(ctx.message.author.name, ctx.message.author.discriminator), colour=discord.Colour(0x7ed321), description='**Reason:** {} \n **Time:** {}/{}/{}'.format(reason, d.year, d.month, d.day))
    embed.set_author(name='{}#{}'.format(member.name, member.discriminator), url="https://discordapp.com", icon_url='{}'.format(member.avatar_url, member.name, member.discriminator))
    embed.set_thumbnail(url="{}".format(ctx.message.author.avatar_url))
    role = discord.utils.get(ctx.guild.roles, name="Retired Staff")
    if ctx.message.author.top_role < role:
            await ctx.send('```Only staff Can kick anyone```')
    elif reason is None:
        await ctx.send('You can\'t kick anyone without a reason')
    else:
        if ctx.message.author.top_role > role:
            if ctx.message.author.top_role > member.top_role:
                await ctx.send(embed=embed)
        else:
            if ctx.message.author.top_role <= member.top_role:
                await ctx.send('```You can\'t ban a staff member higher than you```')
@kick.error
async def kick_error(ctx, error):
    if isinstance(ctx, BadArgument):
        await ctx.send('Something Went Wrong')
    else:
        await ctx.send('```/kick [Member] [Reason]```')   
    
bot.run(os.getenv('TOKEN'))
