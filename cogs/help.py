import discord
from discord.ext import commands
from datetime import datetime
import datetime
import time
import os
import csv
import inspect

with open('Config.csv', 'r') as f:
    ConfigReader = csv.reader(f)
    Config = list(ConfigReader)
footertext = Config[2][1]
disabledcommandslist = Config[4]
magic8ballresponces = Config[5]

def user_is_owner(ctx):
    return str(ctx.author.id) in Config[3][1]

class helpcommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["HELP","Help"])
    async def help(self, ctx, cog=None):
        if cog is None:
            embed = discord.Embed(title="Use `wu!help *cog*` to find out more about them!",description="Windows Help")
            embed.add_field(name="Cogs", value="Utility",inline=False)
            embed.add_field(name="\uFEFF", value="Fun",inline=False)
            embed.add_field(name="\uFEFF", value="Music",inline=False)
            embed.add_field(name="\uFEFF", value="ChannelManager",inline=False)
            embed.add_field(name="No Category", value="Help\nSuggestions\nneofetch\nchangeprefix",inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'Music' in cog:
            embed = discord.Embed(Title="Music", value="Music Commands")
            embed.add_field(name="connect", value="Connect to voice.", inline=False)
            embed.add_field(name="now_playing", value="Display information about the currently playing song.", inline=False)
            embed.add_field(name="pause", value="Pause the currently playing song.", inline=False)
            embed.add_field(name="play", value="Request a song and add it to the queue.", inline=False)
            embed.add_field(name="queue", value="Retrieve a basic queue of upcoming songs.", inline=False)
            embed.add_field(name="resume", value="Resume the currently paused song.", inline=False)
            embed.add_field(name="skip", value="Skip the song.")
            embed.add_field(name="stop", value="Stop the currently playing song and destroy the player.", inline=False)
            embed.add_field(name="volume", value="Change the player volume.", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)
        elif 'Fun' in cog:
            embed = discord.Embed(Title="Fun", value="Fun Commands!")
            embed.add_field(name="emojis", value="Turns Text Into Emojis", inline=False)
            embed.add_field(name="CMD", value="To Use This Command Type wu!cmd **windowsversion** **command**", inline=False)
            embed.add_field(name="hack", value="Hacks A User Fun Command", inline=False)
            embed.add_field(name="reverse", value="Reverses Text", inline=False)
            embed.add_field(name="cool", value="Is A User Cool?", inline=False)
            embed.add_field(name="echo", value="Echos Text", inline=False)
            embed.add_field(name="format", value="Format A Drive", inline=False)
            embed.add_field(name="ascii", value="Turns Text In To Ascii", inline=False)
            embed.add_field(name="spoiler", value="Puts Text In A Spoiler")
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)    
        elif 'Utility' in cog:
            embed = discord.Embed(Title="Utility", value="Utility Commands!")
            embed.add_field(name="8ball", value="Magic8Ball Command", inline=False)
            embed.add_field(name="askmestuff", value="Answers A Yes/No Question", inline=False)
            embed.add_field(name="botinfo", value="Info About The Bot", inline=False)
            embed.add_field(name="helpme", value="Use this command for any issues with the bot", inline=False)
            embed.add_field(name="invite", value="Gets The Bot Invite Link", inline=False)
            embed.add_field(name="pfp", value="Gets A Profile Picture Link And Sends It In Discord", inline=False)
            embed.add_field(name="ping", value="Pong!", inline=False)
            embed.add_field(name="serverinfo", value="Get information about the server the command is executed in", inline=False)
            embed.add_field(name="uptime", value="How Long Has The Bot Been Online For?", inline=False)
            embed.add_field(name="userinfo", value="Recieve information about the mentioned user", inline=False)
            embed.add_field(name="perms", value="Perms That A User Has", inline=False)
            embed.add_field(name="joined", value="Says The Time Someone Joined", inline=False)
            embed.add_field(name="source", value="Gets The Source Code For A Command", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)    
        elif 'Mod' in cog:
            embed = discord.Embed(Title="Mod", value="Mod Commands!")
            embed.add_field(name="clear5", value="Clears 5 Messages", inline=False)
            embed.add_field(name="clear10", value="Clears 10 Messages", inline=False)
            embed.add_field(name="ban", value="Bans A Member", inline=False)
            embed.add_field(name="kick", value="Kicks A Member", inline=False)
            embed.add_field(name="warn", value="Warns A Member", inline=False)
            embed.add_field(name="clear", value="Clears Messages", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)    
        elif 'ChannelManager' in cog:
            embed = discord.Embed(Title="ChannelManager", value="ChannelManager Commands - Must have manange permissions on the server")
            embed.add_field(name="remove", value="Removes a user to the channel command is ran in.", inline=False)
            embed.add_field(name="add", value="Adds a user to the channel command is ran in.", inline=False)
            embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.now()
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(helpcommand(bot))


