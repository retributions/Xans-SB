import discord
from discord.ext import commands
from colorama import Fore 
import asyncio
import random
import traceback

Token = ""

Xans = commands.Bot(command_prefix='x!', self_bot=True)
Xans.remove_command('help')



@Xans.event
async def on_ready():
  print(f'''
  
       {Fore.BLUE}         ██╗  ██╗     █████╗     ███╗   ██╗    ███████╗
       {Fore.BLUE}         ╚██╗██╔╝    ██╔══██╗    ████╗  ██║    ██╔════╝
       {Fore.BLUE}          ╚███╔╝     ███████║    ██╔██╗ ██║    ███████╗
       {Fore.BLUE}          ██╔██╗     ██╔══██║    ██║╚██╗██║    ╚════██║
       {Fore.BLUE}         ██╔╝ ██╗    ██║  ██║    ██║ ╚████║    ███████║
       {Fore.BLUE}         ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝    ╚══════╝
       
                    {Fore.WHITE}Made By Chriz And Rxge
       
       {Fore.RED}         Logged In As : {Xans.user.name}
       {Fore.RED}         Prefix : {Xans.command_prefix}
       {Fore.RED}         Users ID : {Xans.user.id}
       {Fore.RED}         Discrim : {Xans.user.discriminator}  
                ''')

Xans.copycat = None

@Xans.event
async def on_message(message):
    if Xans.copycat is not None and Xans.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    await Xans.process_commands(message)

@Xans.command()
async def scopy(ctx):
    await ctx.message.delete()
    if Xans.user is None:
        return
    Xans.copycat = None


@Xans.command()
async def copy(ctx, user: discord.User):
    await ctx.message.delete()
    Xans.copycat = user

@Xans.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    embed = discord.Embed(title=f":repeat: {message}", color=ctx.author.colour)
    await ctx.send(embed=embed)

@Xans.command()
async def help(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Xans Selfbot", timestamp=ctx.message.created_at,color=discord.Colour.from_rgb(93, 151, 245))
 
  embed.add_field(name="Help", value="shows this command.", inline=False)
  embed.add_field(name="Fun", value="shows fun commands.", inline=False)
  embed.add_field(name="Utility", value="shows utility commands.", inline=False)
  embed.add_field(name="Commands", value="shows basic  commands.", inline=False)
  embed.add_field(name="DM", value="shows dank memer commands.", inline=False)
  embed.add_field(name="Status", value="shows status commands.", inline=False)
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/778272174791327785/785739855371829269/image0_31.gif')

  await ctx.send(embed=embed)

##ignore 


 
@Xans.command()
async def DM(ctx):
      embed = discord.Embed(title="Dank Memer Commands", color=ctx.author.colour)
      embed.add_field(name="Farm", value="Starts Grinding Normal Dank Memer", inline=False)
      embed.add_field(name="PFarm", value="Starts Grinding Premium Dank Memer", inline=False)
      embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/ma6Kcc6vmwywJ_YZwyk8iDyUMSR0Rde9ollrkJU50GY/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png?width=427&height=427")
      await ctx.send(embed=embed)
  
@Xans.command()
async def Farm(ctx):
  await ctx.message.delete()
  lol = "n", "e", "r", "d"
  await asyncio.sleep(1)
  await ctx.send("pls beg")
  await asyncio.sleep(2)
  await ctx.send("pls fish")
  await asyncio.sleep(3)
  await ctx.send("pls pm")
  await asyncio.sleep(2)
  await ctx.send(random.choice(lol))
  await asyncio.sleep(3)
  await ctx.send("pls hunt")
  await asyncio.sleep(60)
  await ctx.send("pls Farm")

@Xans.command()
async def PFarm(ctx):
  await ctx.message.delete()
  lol = "n", "e", "r", "d"
  aha = "a", "b", "c", "d"
  await asyncio.sleep(1)
  await ctx.send("pls beg")
  await asyncio.sleep(2)
  await ctx.send("pls fish")
  await asyncio.sleep(3)
  await ctx.send("pls pm")
  await asyncio.sleep(2)
  await ctx.send(random.choice(lol))
  await asyncio.sleep(3)
  await ctx.send("pls hunt")
  await asyncio.sleep(4)
  await ctx.send("pls trivia")
  await asyncio.sleep(2)
  await ctx.send(random.choice(aha))
  await asyncio.sleep(45)
  await ctx.send("pls PFarm")

@Xans.command(pass_contex=True)
async def utility(ctx):
 await ctx.message.delete()
 embed=discord.Embed(title="Utility Commands!", timestamp=ctx.message.created_at, color=discord.Colour.from_rgb(94, 148, 235))
 embed.add_field(name="Ban", value="bans the mentioned member.", inline=False)
 embed.add_field(name="Kick", value="kicks the mentioned member.", inline=False)
 embed.add_field(name="Avatar", value="shows the mentioned users avatar.", inline=False)
 embed.add_field(name="Whois", value="shows who is the mentioned user.", inline=False)
 embed.add_field(name="Purge", value="purges the listed amount of msgs.", inline=False)
 embed.add_field(name="Serverinfo", value="shows info about the server.", inline=False)
 await ctx.send(embed=embed)

@Xans.command(pass_contex=True)
async def status(ctx):
 await ctx.message.delete()
 embed=discord.Embed(title="Status Commands!", timestamp=ctx.message.created_at, color=discord.Colour.from_rgb(113, 163, 245))
 embed.add_field(name="Stream", value="sets status to streaming.", inline=False)
 embed.add_field(name="Play", value="sets status to playing.", inline=False)
 embed.add_field(name="Watch", value="sets status to watching.", inline=False)
 embed.add_field(name="Listen", value="sets status to listening.", inline=False)
 await ctx.send(embed=embed)

@Xans.command(pass_contex=True)
async def commands(ctx):
 await ctx.message.delete()
 embed=discord.Embed(title="Basic Commands!", timestamp=ctx.message.created_at, color=discord.Colour.from_rgb(68, 121, 207))
 embed.add_field(name="Ping", value="shows clients latency.", inline=False)
 embed.add_field(name="Spam", value="spams the listed amount of msgs.", inline=False)
 embed.add_field(name="Info", value="gives more info on this selfbot.", inline=False)
 await ctx.send(embed=embed)

@Xans.command()
async def ping(ctx):
 await ctx.message.delete()
 message = await ctx.send("**Pong!🏓**")
 await asyncio.sleep(2)
 await message.edit(content=f"**{round(Xans.latency *10)} ms**")

@Xans.command(pass_contex=True)
async def spam(ctx, amount: int, *, message):
  await ctx.message.delete()
  for _i in range(amount):
      await ctx.send(message)

@Xans.command()
async def stream(ctx, *, text):
  await ctx.message.delete()
  await Xans.change_presence(activity=discord.Streaming (url = "https://www.twitch.tv/chrizhub", name= text))
  await ctx.channel.send(f"**{Xans.user.name}, your now streaming {text}**")

@Xans.command()
async def play(ctx, *, text):
 await ctx.message.delete()
 await Xans.change_presence(activity=discord.Game (name = text))
 await ctx.channel.send(f"**{Xans.user.name}, your now playing {text}**")
 
@Xans.command(pass_contex=True)
async def whois(ctx, member: discord.Member):
  await ctx.message.delete()
  member = ctx.author if not member else member
  roles = [role for role in member.roles]

  embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
  
  embed.set_author(name=f"User Info - {member}")
  embed.set_thumbnail(url=member.avatar_url)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  embed.add_field(name="User ID", value=member.id)
  embed.add_field(name="Nickname", value=member.display_name)

  embed.add_field(name="Creation Date", value=member.created_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))
  embed.add_field(name="Guild Join Date", value=member.joined_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))

  embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
  embed.add_field(name="Highest Role", value=member.top_role.mention)

  embed.add_field(name="Bot?", value=member.bot)

  await ctx.send(embed=embed)

@Xans.command(pass_contex=True)
async def fun(ctx):
  await ctx.message.delete()
  embed=discord.Embed(title="Fun Commands!", timestamp=ctx.message.created_at, color=discord.Colour.from_rgb(109, 163, 252))
  embed.add_field(name="8ball", value="ask any question.", inline=False)
  embed.add_field(name="Say", value="say any message as a embed.", inline=False)
  embed.add_field(name="Gayr8", value="shows the gay rate of the mentioned.", inline=False)
  embed.add_field(name="Load", value="loads a something with a custom message.", inline=False)
  embed.add_field(name="Hug", value="hugs the mentioned user.", inline=False)
  embed.add_field(name="copy", value=f"Copys Mention User To Stop Do {Xans.command_prefix}scopy", inline=False)
  embed.add_field(name="PP", value="shows the mentioned users pp size.", inline=False)
  embed.set_footer(text="More Coming Soon!")
  await ctx.send(embed=embed)

@Xans.command()
async def Nuke(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Nuke Commands!", timestamp=ctx.message.created_at, color=ctx.author.colour)
  
  embed.add_field(name="Massban", value="Bans everyone", inline=False)
  embed.add_field(name="Massunban", value="Unbans everyone", inline=False)
  embed.add_field(name="Masskick", value="Kicks everyone", inline=False)
  
  await ctx.send(embed=embed)
  
@Xans.command(pass_contex=True)
async def av(ctx, member: discord.Member):
  embed = discord.Embed(color = discord.Color.from_rgb(147,112,219), timestamp=ctx.message.created_at)
  embed.set_author(name=f"hey look at {member} cool pfp") 
  embed.set_image(url='{}'.format(member.avatar_url))
  embed.set_footer(text=member.id)
  await ctx.send(embed=embed)
  await ctx.message.delete()
  
@Xans.command()
async def load(ctx, *, load):
  await ctx.message.delete()
  message = await ctx.send("```[ █▒▒▒▒▒▒▒▒▒▒▒ ] - 4% Loading.```")
  await asyncio.sleep(2)
  await message.edit(content="```[██▒▒▒▒▒▒▒▒▒▒] \ 11% Loading..```")
  await message.edit(content="```[███▒▒▒▒▒▒▒▒▒] | 24% Loading...```")
  await message.edit(content="```[████▒▒▒▒▒▒▒▒] / 36% Loading.```")
  await message.edit(content="```[█████▒▒▒▒▒▒▒] - 43% Loading..```")
  await message.edit(content="```[██████▒▒▒▒▒▒] \ 48% Loading...```")
  await message.edit(content="```[███████▒▒▒▒▒] | 57% Loading.```")
  await message.edit(content="```[████████▒▒▒▒] / 69% Loading..```")
  await message.edit(content="```[█████████▒▒▒] - 78% Loading...```")
  await message.edit(content="```[██████████▒▒] \ 81% Loading.```")
  await message.edit(content="```[███████████▒] | 95% Loading..```")
  await message.edit(content="```[████████████] / 100% Loading...```")
  await message.edit(content=f"```{load}```")

@Xans.command(aliases=['8ball', 'question'])
async def _8ball(ctx, *, question):
    await ctx.message.delete()
    responses = ['no','yes','maybe','probably','couldnt find the answer','Don’t count on it','Outlook not so good','My sources say no','Very doubtful','My reply is no','Reply hazy try again','Better not tell you now','Ask again later','Cannot predict now','Concentrate and ask again','It is certain','Without a doubt','You may rely on it','Yes definitely','It is decidedly so','As I see it, yes','Most likely','Yes','Outlook good','Signs point to yes']
    em = discord.Embed(description=f'Question: {question}\nAnswer: {random.choice(responses)}',colour=0x9999)

    await ctx.send(embed=em)

@Xans.command()
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
            print(f"[+] UnBanned")
        except:
            pass

@Xans.command()
async def masskick(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                pass
        print ("Action Completed: masskick")

@Xans.command()
async def massban(ctx):
 await ctx.message.delete()
 guild = ctx.guild
 for member in list(ctx.guild.members):
  try:
    await guild.ban(member)
    print(f"User" + member.name + f"Has been Banned From {ctx.guild.name}")
  except:
      pass
  print("")
  print("Successfully Massbanned")

@Xans.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Xans.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@Xans.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Xans.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))
    
@Xans.command()
async def stop(ctx):
    await ctx.message.delete()
    await Xans.change_presence(activity=None, status=discord.Status.dnd)

@Xans.command(aliases=["logout"])
async def off(ctx):
    embed = discord.Embed(title="Turning SelfBot Off", description=f"_Selfbot Now Leaving.... bye {Xans.user.name}_" )

    embed.set_thumbnail (url="https://cdn.discordapp.com/emojis/660599121039851530.png?v=1")
    await ctx.send(embed=embed)
    await ctx.message.delete()
    await Xans.logout()

@Xans.command(pass_contex=True)
async def say(ctx, *, say):
  embed=discord.Embed(description=f"{say}", color=discord.Colour.from_rgb(92, 151, 247))
  await ctx.send(embed=embed)

@Xans.command(aliases=['pp', 'Pp', 'penis'])
async def PP(ctx, *, user: discord.Member = None):
  await ctx.message.delete()
  if user is None:
      user = ctx.author
  size = random.randint(1, 32)
  dong = ""
  for _i in range(0, size):
     penis += "="
  embed = discord.Embed(title=f"{user}'s Penis Size",
desciption=f"8{penis}D", color=discord.Colour.from_rgb(73, 137, 242))
  await ctx.send(embed=embed)


try:    
  Xans.run(Token, bot=False)
except:
 file = open("traceback.txt", "w")
 file.write(traceback.format_exc())
 file.close()
 exit(0)
