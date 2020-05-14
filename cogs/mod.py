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

class mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear10(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)
        print("Cleared 10 Messages")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear5(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        print("Cleared 5 Messages")

    @commands.group()
    @commands.has_permissions(manage_guild=True)
    async def channelmanager(self,ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid Channel Manager Command Passed')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await ctx.send(f"Banned {member} For {reason}")
        await member.ban(reason=reason)

    @channelmanager.command()
    @commands.has_permissions(manage_guild=True)
    async def remove(self, ctx, member: discord.Member, channel=None):
        """"Remove as member to a text channel"""
        if not channel:
            channel = ctx.channel
        await channel.set_permissions(member, read_messages=False)
        await channel.set_permissions(member, send_messages=False)

    @channelmanager.command()
    @commands.has_permissions(manage_guild=True)
    async def add(self, ctx, member: discord.Member, channel=None):
        """"Adds as member to a text channel"""
        if not channel:
            channel = ctx.channel
        await channel.set_permissions(member, read_messages=True)
        await channel.set_permissions(member, send_messages=True)

    @commands.command()
    @commands.has_permissions (manage_messages = True)
    async def clear(self,ctx, amount = 5):
        await ctx.channel.purge(limit = amount)
        import random
        embed=discord.Embed(color = discord.Colour.from_hsv(random.random(), 1, 1))
        embed.add_field(name= "Message Cleared", value= f"{amount} messages have been cleared!", inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed,delete_after=5)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        await ctx.send(f"Kicked {member} For {reason}")
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.has_permissions(ban_members=True)
    async def warn(self, ctx, member:discord.Member ,* ,reason=None):
        if reason is None: 
            memid = member.id
            print(f"{member} Has Been Warned")
            await ctx.send(f"{member} Has Been Warned **Read The Rules So You Wont Be Warned**")
            await self.bot.get_user(memid).send(f"You Was Warned In {ctx.guild.name} By {ctx.message.author.name}")
        else:
            memid = member.id
            print(f"{member} Has Been Warned For {reason}")
            await ctx.send(f"{member} Has Been Warned For {reason} **Read The Rules So You Wont Be Warned For This**")
            await self.bot.get_user(memid).send(f"You Was Warned In {ctx.guild.name} By {ctx.message.author.name} For {reason}")

def setup(bot):
    bot.add_cog(mod(bot))