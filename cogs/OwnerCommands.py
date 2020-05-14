import discord
from discord.ext import commands
from datetime import datetime
import datetime
import time
import os
import csv
import inspect
import asyncio 
import random



with open('Config.csv', 'r') as f:
    ConfigReader = csv.reader(f)
    Config = list(ConfigReader)
footertext = Config[2][1]
ids = "391353718538502145"
disabledcommandslist = Config[4]
magic8ballresponces = Config[5]
ownerid = ids

def user_is_owner(ctx):
    return str(ctx.author.id) == 391353718538502145

class OwnerCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.group()
    @commands.check(user_is_owner)
    async def owner(self, ctx):
        'Bot Owner Commands'
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid Owner Command Passed')

    @owner.command()
    async def installpypackage(self, ctx, pkg):
        os.system(f'sudo -H python3.7 -m pip install {pkg}')

    @commands.group()
    @commands.check(user_is_owner)
    async def cogs(self,ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid Cog Command Passed')

    @cogs.command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f"cogs.{extension}")
        embed=discord.Embed(color = 0x00FF00)
        embed.add_field(name="Cog load", value=(f"Cog {extension}.py has been loaded!"), inline=False)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

    @cogs.command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f"cogs.{extension}")
        embed=discord.Embed(color = 0xFF0000)
        embed.add_field(name="Cog Unload", value=(f"Cog {extension}.py has been unloaded!"), inline=False)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(embed=embed)

    @cogs.command()
    async def reload(self, ctx, extension):
        self.bot.unload_extension(f"cogs.{extension}")
        self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f":white_check_mark: Reloaded {extension}.py")

    @owner.command()
    async def help(self,ctx):
        await ctx.send("shutdown")
        await ctx.send("disablecommand")
        await ctx.send("enablecommand")
        await ctx.send("disabledcommands")
        await ctx.send("dmuser")
        

    @owner.command()
    @commands.check(user_is_owner)
    async def shutdown(self, ctx):
        await ctx.send(":wave:")
        await self.bot.logout()
        await os._exit(0)

    @owner.command()
    @commands.check(user_is_owner)
    async def disablecommand(self, ctx, *, cmd: str='None'):
        print(cmd)
        cmdstr = cmd
        if cmd is 'None':
            await ctx.send('Missing command argument')
        elif cmd in disabledcommandslist:
            await ctx.send('This command is already disabled!')
        else:
            try:
                cmd = self.bot.get_command(cmd)
                cmd.enabled = False
                await ctx.send("Disabling command '{}'".format(cmd))
                Config[4].append(cmdstr)
                TEMPConfig = open('Config.csv', 'w', newline='')
                csv_writer = csv.writer(TEMPConfig)
                csv_writer.writerows(Config)
                TEMPConfig.close()
                #await bot.get_channel(548207122589024389).send(message)
            except AttributeError:
                await ctx.send("Attempt to disable command '{}' failed, possibly due to the command not existing".format(cmdstr))
                #message = "Attempted to disable command '{}' but failed as the command does not exist. Command sent by {}.".format(cmdstr, ctx.author)
                #await bot.get_channel(548207122589024389).send(message)

    @owner.command()
    @commands.check(user_is_owner)
    async def enablecommand(self, ctx, *, cmd: str='None'):
        print(cmd)
        cmdstr = cmd
        if cmd is 'None':
            await ctx.send('Missing command argument')
        elif cmd not in disabledcommandslist:
            print(disabledcommandslist)
            await ctx.send('Command is not disabled!')
        else:
            try:
                cmd = self.bot.get_command(cmd)
                cmd.enabled = True
                print(disabledcommandslist)
                Config[4].remove(cmdstr)
                TEMPConfig = open('Config.csv', 'w', newline='')
                csv_writer = csv.writer(TEMPConfig)
                csv_writer.writerows(Config)
                TEMPConfig.close()
                await ctx.send("Enabling command '{}'".format(cmd))
                #message = "Enabled command '{}'. Command sent by {}.".format(cmdstr, ctx.author)
                #await bot.get_channel(548207122589024389).send(message)
            except AttributeError:
                await ctx.send("Attempt to enable command '{}' failed, possibly due to the command not existing".format(cmdstr))
                #message = "Attempted to enable command '{}' but failed as the command does not exist. Command sent by {}.".format(cmdstr, ctx.author)
                #await client.get_channel(548207122589024389).send(message)

    @owner.command()
    async def disabledcommands(self, ctx):
        discommand = []
        for cmd in disabledcommandslist:
            if cmd == 'Discommand':
                continue
            else:
                discommand.append(cmd)
        if discommand == []:
            discommand = 'None'
        await ctx.send('Disabled commands {}'.format(discommand))

    @owner.command()
    @commands.is_owner()
    async def dmuser(self, ctx, user: discord.Member=None, *, msg: str=None):
        if user is None:
            embed = discord.Embed(title='Member DM', description='Have the bot DM a user', colour=65280)
            embed.set_author(name='Windows Bot')
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.add_field(name='You have missed the user argument!', value='Missing argument')
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_author(name='Windows Bot', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        elif msg is None:
            embed = discord.Embed(title='Member DM', description='Have the bot DM a user', colour=65280)
            embed.set_author(name='Windows Bot ')
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.add_field(name='You have missed the message argument!', value='Missing argument')
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_author(name='Windows Bot', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        elif (msg is None) and (user is None):
            embed = discord.Embed(title='Member DM', description='Have the bot DM a user', colour=65280)
            embed.set_author(name='Windows Bot')
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.add_field(name='You have missed the user and message argument!', value='Missing argument')
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.set_author(name='Windows Bot', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Member DM', description='Have the bot DM a user', colour=65280)
            embed.set_author(name='Windows Bot')
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.add_field(name='Sending DM', value='Sending')
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_author(name='Windows Bot', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
            
            embed = discord.Embed(title='Member DM', description='You have revieved a bot DM', colour=65280)
            embed.set_author(name='Windows Bot')
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.add_field(name=msg, value='Message from {}'.format(ctx.author))
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            embed.set_author(name='Windows Bot', icon_url=self.bot.user.avatar_url)
            await user.send(embed=embed)

def setup(bot):
    bot.add_cog(OwnerCommands(bot))
