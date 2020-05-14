import time
import discord
from discord.ext import commands
import time
import inspect
import csv
import os
import datetime
from random import randint
import asyncio
from random import getrandbits
from ipaddress import IPv4Address, IPv6Address
import json

logs = 607601125000216577

start_time = time.time()

with open('Config.csv', 'r') as f:
    ConfigReader = csv.reader(f)
    Config = list(ConfigReader)
footertext = Config[2][1]
disabledcommandslist = Config[4]
magic8ballresponces = Config[5]
print(magic8ballresponces)
magic8ballresponces.pop(0)
print(magic8ballresponces)
prefix = Config[0][1]


with open("prefixes.json", 'r') as f:
    prefixes = json.load(f)

async def get_pre(bot, message):
    try:
        prefix = prefixes[str(message.guild.id)]
        if prefix == "":
            prefix = Config[0][1]
    except KeyError:
        prefix = str(Config[0][1])
    botmention = "<@{}> ".format(bot.user.id)
    pre = [prefix, botmention]

    return pre

bot = commands.Bot(command_prefix=get_pre)

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Bot Is Online\nBot User Name: {bot.user.name}\nBot User ID: {bot.user.id}\nDefault Prefix: wu!")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} Servers! wu!help"))
    for cmd in Config[4]:
        if cmd == 'Discommand':
            print('Discommand')
        else:
            cmdstr = cmd
            print("Disabling command('s) '{}'!".format(cmd))
            try:
                cmd = bot.get_command(cmd)
                cmd.enabled = False
            except AttributeError:
                print("Failed to disable command '{}' as it does not exist! Check config file for unknown disabled commands.".format(cmdstr))

@bot.command()
async def hack(ctx, *, target: discord.Member = None):
    if target is None:
      target = ctx.message.author
    v = 4
    if v == 4:
      bits = getrandbits(32) # generates an integer with 32 random bits
      addr = IPv4Address(bits) # instances an IPv4Address object from those bits
      a = str(addr) # get the IPv4Address object's string representation
    elif v == 6:
      bits = getrandbits(128) # generates an integer with 128 random bits
      addr = IPv6Address(bits) # instances an IPv6Address object from those bits
      # .compressed contains the short version of the IPv6 address
      # str(addr) always returns the short address
      # .exploded is the opposite of this, always returning the full address with all-zero groups and so on
      a = addr.compressed
    async def random_with_N_digits(n):
      range_start = 10**(n-1)
      range_end = (10**n)-1
      return randint(range_start, range_end)
    f = await random_with_N_digits(4)
    b = target.name.lower()
    b = b.replace(" ", "")
    j = await random_with_N_digits(5)
    if j > 65535:
      j = 65535
    message = await ctx.send("```fix\nHacking...```")
    await asyncio.sleep(2)
    await message.edit(content="```fix\nHacking...\nMember found!```")
    await asyncio.sleep(2)
    await message.edit(content="```fix\nHacking...\nMember found!\nGetting ip...```")
    await asyncio.sleep(2)
    await message.edit(content="```fix\nHacking...\nMember found!\nGetting ip...\nip found```")
    await message.edit(content=f"```fix\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address```")
    await asyncio.sleep(2)
    await message.edit(content=f"```fix\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...```")
    await asyncio.sleep(2)
    await message.edit(content=f"```fix\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com```")
    await message.edit(content=f"```fix\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******```")
    await asyncio.sleep(2)
    await message.edit(content=f"```fix\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...```")
    await asyncio.sleep(2)
    await message.edit(content=f"```fix\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.```")
    await asyncio.sleep(2)
    await message.edit(content=f"```fix\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...```")
    await asyncio.sleep(2)
    await message.edit(content=f"```fix\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...\nConnection Closed.```")
    await message.edit(content=f"```fix\nHacking...\nMember found!\nGetting ip...\nip found\nip={a}\nVirus pushed to ip address\nGetting info...\nemail={b}{f}@gmail.com\npassword=******\nDeleting files...\nFiles deleted.\nClosing Connection...\nConnection Closed.\nExited port {j}```")
    await asyncio.sleep(2)
    await ctx.send(f"Finished hacking user **{target.display_name}**.")


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.startswith('rave'):
        em=discord.Embed(description="PARTY TIME")
        em.set_image(url="https://cdn.discordapp.com/attachments/538877256630534178/619904193444053047/632816750170128emoji.gif")
        await message.channel.send(embed=em)
    elif message.content.startswith('<a:rave:619993871249834004>'):
        em=discord.Embed(description="PARTY TIME")
        em.set_image(url="https://cdn.discordapp.com/attachments/538877256630534178/619904193444053047/632816750170128emoji.gif")
        await message.channel.send(embed=em)
    else:
        print(f"{message.guild.name}: #{message.channel}: {message.author}: {message.content}")
        await bot.process_commands(message)

import datetime
current_time = time.time()
difference = int(round(current_time - start_time))
text = str(datetime.timedelta(seconds=difference))

#@bot.command()
#async def test(ctx):
#    message = await ctx.send("Ping!")
#    await message.edit(content='Pong!')

@bot.command(aliases=['suggestions', 'SUGGESTIONS'])
async def Suggestions(ctx, name, *, Reply):
    embed = discord.Embed(Title="Command Ideas", value="Command Ideas For The Bot", colour=0x301d8c)
    embed.set_footer(text='Invoked by {}'.format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="Command Name", value=name)
    embed.add_field(name="Bot Reply", value=Reply)
    embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
    embed.timestamp = datetime.datetime.now()
    await ctx.send(embed=embed)

    embed = discord.Embed(name="Command Request", description="Command Request From a User", colour=0x301d8c)
    embed.set_footer(text="Windows Bot Developed By Unicornboy776#6831")
    embed.add_field(name="The person who requested support was", value=ctx.author.name, inline=False)
    embed.add_field(name='The discriminator of the request', value=ctx.author.discriminator, inline=False)
    embed.add_field(name='The user ID of the request', value=ctx.author.id, inline=False)
    embed.add_field(name='Command Name', value=name, inline=False)
    embed.add_field(name="Bot Reply", value=Reply)
    embed.set_thumbnail(url=str(ctx.author.avatar_url))
    await bot.get_user(391353718538502145).send(embed=embed)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def changeprefix(ctx, *, prefix):
    
    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)

    embed = discord.Embed(title="Changed server prefix", colour=0x301d8c)
    embed.add_field(name="Changed Prefix To", value=prefix)
    embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
    embed.timestamp = datetime.datetime.now()
    await ctx.send(embed=embed)

    #await ctx.send(f"Changed Prefix To : `{prefix}`")

@bot.event
async def on_member_remove(ctx):

    await bot.get_user(628287540646117391).send(f"<@{ctx.id}> left {ctx.guild.name}")

@bot.event
async def on_member_join(ctx):

    await bot.get_channel(628287497041870848).send(f" <@{ctx.id}> joined {ctx.guild.name}")

@bot.event
async def on_guild_remove(ctx):
    activeGuilds = bot.guilds
    totalguilds = len(activeGuilds)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{totalguilds} Servers! wu!help"))   
    await bot.get_channel(628287526498729984).send(f"Removed {bot.user.name} From {ctx.name}")

    with open("prefixes.json", 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(ctx.id))

    with open("prefixes.json", 'w') as f:
        json.dump(prefixes, f, indent=4)



@bot.event
async def on_guild_join(ctx):
    activeGuilds = bot.guilds
    totalguilds = len(activeGuilds)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{totalguilds} Servers! wu!help"))
    message = f"Hello Thanks For Adding {bot.user.name}™ We Have Commands Such As \n wu!CMD \n wu!emojis \n wu!ping \n If You Need Support For The Bot Use wu!helpme <issue/question> But Replace `<issue/question>` With Your Issue/Question"
    await ctx.owner.send(message)
    members = str(len(list(ctx.members)))
    embed=discord.Embed()
    if str(ctx.region) == "brazil":
        region = ":flag_br: Brazil :flag_br:"
    elif str(ctx.region) == "eu-central":
        region = ":flag_eu: EU Central :flag_eu:"
    elif str(ctx.region) == "hongkong":
        region = ":flag_hk: Hong Kong :flag_hk:"
    elif str(ctx.region) == "india":
        region = ":flag_in: India :flag_in:"
    elif str(ctx.region) == "japan":
        region = ":flag_jp: Japan :flag_jp:"
    elif str(ctx.region) == "russia":
        region = ":flag_ru: Russia :flag_ru:"
    elif str(ctx.region) == "singapore":
        region = ":flag_sg: Singapore :flag_sg:"
    elif str(ctx.region) == "southafrica":
        region = ":flag_za: South Africa :flag_za:"
    elif str(ctx.region) == "sydney":
        region = ":flag_au: Sydney :flag_au:"
    elif str(ctx.region) == "us-central":
        region = ":flag_us: US Central :flag_us:"
    elif str(ctx.region) == "us-east":
        region = ":flag_us: US East :flag_us:"
    elif str(ctx.region) == "us-south":
        region = ":flag_us: US South :flag_us:"
    elif str(ctx.region) == "us-west":
        region = ":flag_us: US West :flag_us:"
    elif str(ctx.region) == "eu-west":
        region = ":flag_eu: EU West :flag_eu:"
    embed.add_field(name="Server Name", value=ctx.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.id, inline=True)
    embed.add_field(name="Server Owner", value=ctx.owner, inline=True)
    embed.add_field(name="Roles", value=str(len(ctx.roles)), inline=True)
    embed.add_field(name="Custom Emojis", value=str(len(ctx.emojis)), inline=True)
    embed.add_field(name="Region", value=region ,inline=True)
    embed.add_field(name="Member Count", value=members, inline=True)
    embed.add_field(name="Channels", value=str(len(ctx.channels)), inline=True)
    embed.add_field(name="Date Created", value=ctx.created_at, inline=True)
    await bot.get_channel(628287481569345557).send(embed=embed)



    #message = "Server Join - I just joined {} with a server ID of {} and {} as the owner! It has {} roles, {} custom emojies, {} as the server region, {} members and {} channels".format(ctx.name, str(ctx.id), ctx.owner, str(len(ctx.roles)), str(len(ctx.emojis)), str(ctx.region), members, str(len(ctx.channels)))
    #await bot.get_channel(logs).send(content=message)

bot.load_extension("cogs.Music")
bot.load_extension("cogs.Utility")
bot.load_extension("cogs.OwnerCommands")
bot.load_extension("cogs.shop")
bot.load_extension('jishaku')
bot.load_extension('cogs.mod')
bot.load_extension('cogs.help')
bot.load_extension('cogs.fun')

bot.run("notoken")

