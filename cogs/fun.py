import discord
from discord.ext import commands
import datetime
import time
import random
import csv
from random import randint
from yaspin import yaspin
import asyncio
from random import getrandbits
from ipaddress import IPv4Address, IPv6Address

CHARS_MAP = {'a': ':regional_indicator_a:', 'b': ':regional_indicator_b:', 'c': ':regional_indicator_c:',
            'd': ':regional_indicator_d:', 'e': ':regional_indicator_e:', 'f': ':regional_indicator_f:',
            'g': ':regional_indicator_g:', 'h': ':regional_indicator_h:', 'i': ':regional_indicator_i:',
            'j': ':regional_indicator_j:', 'k': ':regional_indicator_k:', 'l': ':regional_indicator_l:',
            'm': ':regional_indicator_m:', 'n': ':regional_indicator_n:', 'o': ':regional_indicator_o:',
            'p': ':regional_indicator_p:', 'q': ':regional_indicator_q:', 'r': ':regional_indicator_r:',
            's': ':regional_indicator_s:', 't': ':regional_indicator_t:', 'u': ':regional_indicator_u:',
            'v': ':regional_indicator_v:', 'w': ':regional_indicator_w:', 'x': ':regional_indicator_x:',
            'y': ':regional_indicator_y:', 'z': ':regional_indicator_z:', '1': ':one:', '2': ':two:',
            '3': ':three:', '4': ':four:', '5': ':five:', '6': ':six:', '7': ':seven:', '8': ':eight:',
            '9': ':nine:', "#": ":hash:", "*": ":asterisk:"}


with open('Config.csv', 'r') as f:
    ConfigReader = csv.reader(f)
    Config = list(ConfigReader)
footertext = Config[2][1]
disabledcommandslist = Config[4]
magic8ballresponces = Config[5]

def user_is_owner(ctx):
    return str(ctx.author.id) in Config[3][1]

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def format(self, ctx, *, thing=None):
        if thing is None:
            await ctx.send("Choose A Drive To Format")
        else:
            message = await ctx.send("```\nFormating\n```")
            await asyncio.sleep(2)
            await message.edit(content="```\nFormating 1%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 2%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 3%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 4%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 5%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 6%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 7%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 8%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 9%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 10%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 11%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 12%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 13%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 14%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 16%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 30%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 34%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 40%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 44%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 47%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 55%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 58%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 60%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 64%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 67%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 70%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 74%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 76%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 82%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 85%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 88%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 90%\n```")
            await asyncio.sleep(1)
            await message.edit(content="```\nFormating 99%\n```")
            await asyncio.sleep(5)
            await message.edit(content="```\nFormating 100%\n```")
            await ctx.send(f"Formated Drive {thing}")

    @commands.command()
    async def spoiler(self,ctx,*,text):
        await ctx.send(f"||{text}||")

    @commands.command(aliases=['CMD', 'Cmd'])
    async def cmd(self, ctx, ver, *, cmd):
        await ctx.send("Command Prompt")
        await ctx.send("Version 10.0 " + ver)
        await ctx.send("C:/Windows/System32> " + cmd)    

    @commands.command()
    async def echo(self, ctx, *, text):
        if '@everyone' or '@here' in text:
            return
        else:
            await ctx.send(text)    

    @commands.command()
    async def ascii(self, ctx, *, inp: commands.clean_content):
        from pyfiglet import figlet_format
        ascii_banner = figlet_format(inp, font="small")
        await ctx.send(f"```\n{ascii_banner}```")


    @commands.command(name="emojis")
    async def emojitext(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        actual = []

        for char in text:
            maybe_emote = CHARS_MAP.get(char.lower())

            if maybe_emote is None:
                actual.append(char)
            else:
                actual.append(maybe_emote + "\u200b")
        try:
            await ctx.send("".join(actual))
        except discord.HTTPException:
            await ctx.send("Content too long, sorry.")

    @commands.command()
    async def reverse(self, ctx, *, message: commands.clean_content):
        if '@' in message:
            await ctx.send("Sorry but I'm not pinging")
        else:
            message = message[::-1]
            await ctx.send(message)


def setup(bot):
    bot.add_cog(fun(bot))

