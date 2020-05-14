import discord
from discord.ext import commands
from datetime import datetime
import datetime
import time
import random
import platform
import csv
import asyncio
start_time = time.time()

from jishaku.paginators import PaginatorInterface, WrappedFilePaginator, WrappedPaginator


botinvitelnk="https://discordapp.com/oauth2/authorize?client_id=601076117545418774&scope=bot&permissions=0"

with open('Config.csv', 'r') as f:
    ConfigReader = csv.reader(f)
    Config = list(ConfigReader)
footertext = Config[2][1]
disabledcommandslist = Config[4]
magic8ballresponces = Config[5]

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=65280)
        embed.add_field(name='Uptime', value=text)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.set_author(name='Windows', icon_url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined in {0.joined_at} '.format(member))

    @commands.command()
    async def invite(self, ctx):
        'Gets the invite for the bot'
        embed = discord.Embed(title='Invite bot', url=botinvitelnk, description='Bot invite link')
        embed.set_author(name='Windows (Click here for invite)', url=botinvitelnk)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.set_author(name='Windows', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def screenshare(self, ctx, channelid):
        await ctx.send(f"https://discordapp.com/channels/{ctx.guild.id}/{channelid} \nOnly Works On PC Sorry Moblie \nWont Work On Firefox Too!")

    @commands.command(aliases=["profile", "ui", "pf"])
    async def userinfo(self, ctx, user: discord.Member='own'):
        'Recieve information about the mentioned user'
        if user == 'own':
            user = ctx.author
        roles = ""
        for role in user.roles:
            roles += "{}, ".format(role.name)
        embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=65280)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.set_author(name='Windows', icon_url=self.bot.user.avatar_url)
        embed.add_field(name='Name', value=user.name, inline=True)
        embed.add_field(name='Discriminator', value=user.discriminator, inline=True)
        embed.add_field(name='ID', value=user.id, inline=True)
        embed.add_field(name='Status', value=user.status, inline=True)
        embed.add_field(name='Highest Role', value=user.top_role, inline=True)
        embed.add_field(name='Server Join Date', value=user.joined_at, inline=True)
        embed.add_field(name='Account Created At', value=user.created_at, inline=True)
        embed.add_field(name='Nickname', value=user.nick, inline=True)
        embed.add_field(name='Status', value=user.status, inline=True)
        embed.add_field(name='Is On Mobile', value=user.is_on_mobile(), inline=True)
        embed.add_field(name='Voice State', value=user.voice, inline=True)
        embed.add_field(name='Is Bot?', value=user.bot, inline=True)
        embed.add_field(name='Roles', value=roles, inline=True)
        embed.add_field(name='Is Avatar Image Animated?', value=user.is_avatar_animated(), inline=True)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="source", aliases=["src"])
    async def a(self, ctx: commands.Context, *, command_name: str):
        """
        Displays the source code for a command.
        """
        import inspect

        command = self.bot.get_command(command_name)
        if not command:
            return await ctx.send(f"Couldn't find command `{command_name}`.")

        try:
            source_lines, _ = inspect.getsourcelines(command.callback)
        except (TypeError, OSError):
            return await ctx.send(f"Was unable to retrieve the source for `{command}` for some reason.")

        # getsourcelines for some reason returns WITH line endings
        source_lines = ''.join(source_lines).split('\n')

        paginator = WrappedPaginator(prefix='```py', suffix='```', max_size=1985)
        for line in source_lines:
            paginator.add_line(line)

        interface = PaginatorInterface(ctx.bot, paginator, owner=ctx.author)
        await interface.send_to(ctx)

    @commands.command(name='8ball')
    async def eightball(self, ctx):
        await ctx.send(random.choice(["It is certain :8ball:",
                                    "It is decidedly so :8ball:",
                                    "Without a doubt :8ball:",
                                    "Yes, definitely :8ball:",
                                    "You may rely on it :8ball:",
                                    "As I see it, yes :8ball:",
                                    "Most likely :8ball:",
                                    "Outlook good :8ball:",
                                    "Yes :8ball:",
                                    "Signs point to yes :8ball:",
                                    "Reply hazy try again :8ball:",
                                    "Ask again later :8ball:",
                                    "Better not tell you now :8ball:",
                                    "Cannot predict now :8ball:",
                                    "Concentrate and ask again :8ball:",
                                    "Don't count on it :8ball:",
                                    "My reply is no :8ball:",
                                    "My sources say no :8ball:",
                                    "Outlook not so good :8ball:",
                                    "Very doubtful :8ball:"]))


    @commands.command()
    async def askmestuff(self, ctx, *, question):
        'Ask Me A Question And I will Answer It'
        await ctx.send(f'Question:{question}\nAnswer: {random.choice(magic8ballresponces)}')

    @commands.command(aliases=['guildinfo', 'guild'])
    async def serverinfo(self, ctx):
        'Get information about the server the command is executed in'
        embed = discord.Embed(name="{}'s info".format(ctx.guild.name), description="Here's what I could find.", colour=0x008cff)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_author(name='{}'.format(ctx.guild.name))
        embed.add_field(name='Server Name', value=ctx.guild.name, inline=True)
        embed.add_field(name='ID', value=ctx.guild.id, inline=True)
        embed.add_field(name='Roles', value=len(ctx.guild.roles), inline=True)
        embed.add_field(name='Members', value=len(ctx.guild.members))
        await ctx.send(embed=embed)

    @commands.command(aliases=['about', 'info'])
    async def botinfo(self, ctx):
        'Get the information about the bot (like uptime, ping, server count, etc)'
        current_time = time.time()
        difference = int(round(current_time - start_time))
        ut = str(datetime.timedelta(seconds=difference))
        activeGuilds = self.bot.guilds
        totalguilds = len(activeGuilds)
        membertotal = 0
        channeltotal = 0
        roletotal = 0
        import psutil
        import humanize
        if psutil:
            proc = psutil.Process()

            with proc.oneshot():
                mem = proc.memory_full_info()
                a = f"Using {humanize.naturalsize(mem.rss)} physical memory."  
                b = f"{humanize.naturalsize(mem.vms)} virtual memory."
                c = f"{humanize.naturalsize(mem.uss)} of which unique to this process."

        for s in activeGuilds:
            #print(s.name)
            membertotal += len(s.members)
            channeltotal += len(s.channels)
            roletotal += len(s.roles)
        embed = discord.Embed(title='Bot Information', colour=65280)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.add_field(name='--Versions--', value='Versions of applications/libraries used', inline=False)
        embed.add_field(name="Bot Version", value="1.0.0A", inline=True)
        embed.add_field(name="Discord.PY Version", value=discord.__version__, inline=True)
        embed.add_field(name='--General Bot Information--', value='Information about the bot in general', inline=False)
        embed.add_field(name='Uptime', value=ut, inline=True)
        embed.add_field(name='Ping', value=f"{round(self.bot.latency * 1000, 2)}ms", inline=True)
        embed.add_field(name='Bot ID', value=self.bot.user.id, inline=True)
        embed.add_field(name='Members visible to bot', value=membertotal, inline=True)
        embed.add_field(name='Servers visible to bot', value=totalguilds, inline=True)
        embed.add_field(name='Channels visible to bot', value=channeltotal, inline=True)
        embed.add_field(name='Roles visable to bot', value=roletotal, inline=True)
        embed.add_field(name='--System Information--', value='Information about the system running the bot', inline=False)
        embed.add_field(name='Opperating System Type', value=platform.system(), inline=True)
        embed.add_field(name='Machine Archetecture', value=platform.machine(), inline=True)
        embed.add_field(name='Machine Platform', value=platform.platform(), inline=True)
        embed.add_field(name='Physical Memory', value=a, inline=True)
        embed.add_field(name='Virtual Memory', value=b, inline=True)
        embed.add_field(name='Memory Used', value=c, inline=True)
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['latency', 'PING'])
    async def ping(self, ctx):
        embed = discord.Embed(Title='Ping', description='Loading results', colour=0x008cff)
        message = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await message.delete()
        embed1 = discord.Embed(Title='Ping', description='Ping results', colour=0x008cff)
        embed1.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed1.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed1.timestamp = datetime.datetime.now()
        embed1.add_field(name='Pong', value=f"{round(self.bot.latency * 1000, 2)}ms")
        await ctx.send(ctx.author.mention, embed=embed1)
        print(f'{ctx.message.author.name} Pinged {round(self.bot.latency * 1000, 2)}ms')

    @commands.command()
    async def pfp(self, ctx, member: discord.Member):
        await ctx.send(f"Here Is {member}'s Profile Picture {member.avatar_url}")

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        print(f'{user.name}-{user.id} was banned from {guild.name}-{guild.id}')

    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member=None):
        """A simple command which checks a members Guild Permissions.
        If member is not provided, the author will be checked."""

        if not member:
            member = ctx.author

        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        await ctx.send(content=None, embed=embed)
        # Thanks to Gio for the Command.

    @commands.command()
    async def helpme(self, ctx, helprequest):
        'Use this command for any issues with the bot'
        embed = discord.Embed(name="Windows Support", description="Support for questions/issues with the bot", colour=0x008cff)
        embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.datetime.now()
        embed.add_field(name="Your support reason was", value=helprequest, inline=False)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.add_field(name='Please wait for your support', value='You may need to wait a few hours to about a day depending on your timezone.', inline=False)
        await ctx.send(embed=embed)

        MEMID = ctx.author.id

        asyncio.sleep(5)
        await self.bot.get_user(MEMID).send("Your Support Request Has Been Sent")

        embed = discord.Embed(name="Support Request", description="Support Request From a User", colour=0x008cff)
        embed.set_footer(text="Windows Bot Developed By Unicornboy776#6831")
        embed.add_field(name="The person who requested support was", value=ctx.author.name, inline=False)
        embed.add_field(name='The discriminator of the request', value=ctx.author.discriminator, inline=False)
        embed.add_field(name='The user ID of the request', value=ctx.author.id, inline=False)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.add_field(name='The reason they requested support was', value=helprequest, inline=False)
        embed.set_thumbnail(url=str(ctx.author.avatar_url))
        await self.bot.get_user(391353718538502145).send(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot))
