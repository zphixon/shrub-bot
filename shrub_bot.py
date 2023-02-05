#!/usr/bin/env python3

import discord
from discord.ext import commands
import random
import datetime
import sys
import subprocess
import toml

config_file = sys.argv[1] or 'shrub-bot.toml'
config = toml.load(open(config_file))

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def test(ctx):
    """
    Verify shrub_bot is working.
    """
    await ctx.send("hello!")

@bot.command()
async def parrot(ctx):
    """
    Show a parrot picture.
    """
    parrotURLs = [
            "https://b.thumbs.redditmedia.com/wYE6URJBFHf56SjdSFNFtK8-2lgMKS9dHuPjG7uf5WI.png",
            "https://i.imgur.com/LXaBdyo.jpg",
            #"https://giant.gfycat.com/SneakyElementaryFrogmouth.webm",
            "https://i.imgur.com/o5xPmOC.jpg",
            "https://i.reddituploads.com/2370f1974cd7439f87186484df90922a?fit=max&h=1536&w=1536&s=c7f62ed2c90ee9eb2dbda7fa00fc56b0",
            "https://i.imgur.com/qm5hDLp.png",
            "https://i.imgur.com/JXrbr74.png",
            "http://i.imgur.com/5JMs5fA.jpg",
            "https://i.redd.it/l00qvfi6am9x.jpg",
            "https://cdn.discordapp.com/attachments/264646094493843456/264646792354725898/amw.png",
            ]
    await ctx.send(random.choice(parrotURLs))

@bot.command()
async def shrub(ctx):
    """
    Show a shrub picture.
    """
    shrubURLs = [
            "http://orig00.deviantart.net/4c2a/f/2011/002/f/2/shrub_png_by_dbszabo1-d368txl.png",
            "http://www.talklocal.com/blog/wp-content/uploads/2013/04/How-To-Remove-Shrubs-Landscapers.jpg",
            "http://thehoneytreenursery.com/images/2010_0906logan40007.jpg",
            "http://s.hswstatic.com/gif/lighting-projects-shrub-light-360x240.jpg",
            "http://i.3dxy.us/3d-model/shrub/201409/201409302253_87426.jpg",
            "https://img1.cgtrader.com/items/48310/dc73e5c772/realistic-shrub-bush-set-3d-model-max-obj.jpg",
            "https://img-new.cgtrader.com/items/48310/dc7e246a47/realistic-shrub-bush-set-3d-model-max-obj.jpg",
            "http://www.tedsgardens.com/images/plants/shrubs/Shrub_Arborvitae_HetzMidget.jpg",
            "http://www.clintar.com/img/clintar-landscaping-tip-shrub.png"
            ]
    await ctx.send(random.choice(shrubURLs))

@bot.command()
async def roll(ctx, dice: str):
    """
    Roll some dice.
    """
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        await ctx.send("Format must be NdN, e.g. 1d6")
        return
    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def choose(ctx, *choices: str):
    """
    Choose from some options.
    """
    maybes = ["How about",
            "Let's go with",
            "I'd choose",
            "Let me see...",
            "I want",
            "The obvious choice is",
            "We should go with"]
    await ctx.send("{} {}".format(random.choice(maybes), random.choice(choices)))

@bot.command()
async def birb(ctx):
    """
    Birdie wanna cracker? Good birdie.
    """
    noises = ["sqwak",
            "scree",
            "squak",
            "squek",
            "squack",
            "screk",
            "flutter",
            "flap",
            "screech"]
    await ctx.send("{}".format(random.choice(noises)))

@bot.command()
async def card(ctx):
    """
    Draw a GeothermalShrub card
    """
    cards = [
            "http://i.imgur.com/eDKPYZM.jpg",
            "http://i.imgur.com/P4y7qxC.jpg",
            "http://i.imgur.com/fggPrpU.jpg",
            "http://i.imgur.com/3IGUKAr.jpg",
            "http://i.imgur.com/31KZOog.jpg",
            "http://i.imgur.com/D6UgOcs.jpg",
            "http://i.imgur.com/TUeqsYn.jpg",
            "http://i.imgur.com/GB70icP.jpg",
            "http://i.imgur.com/toKDlm2.jpg",
            ]
    await ctx.send("{}".format(random.choice(cards)))

@bot.command()
async def sauce(ctx):
    """
    Invoke the spirit of the Sauce Hoss.
    """
    await ctx.send("Ｐ Ｒ Ｏ Ｔ Ｅ Ｃ Ｔ   Ｔ Ｈ Ｅ   Ｓ Ａ Ｕ Ｃ Ｅ")

@bot.command()
async def draw(ctx):
    """
    Draw a playing card.
    """
    suits = ["clubs", "hearts", "diamonds", "spades"]
    nums = ["ace", "2", "3", "4", "5", "6", "7", "8",
            "9", "10", "jack", "queen", "king"]
    await ctx.send(random.choice(nums) + " of " + random.choice(suits))

@bot.command()
async def uptime(ctx):
    """
    Get shrub_bot's uptime.
    """
    await ctx.send("Uptime: " + str(subprocess.check_output(["uptime", "-p"]))[2:-3])

@bot.event
async def on_message(message):
    if message.content.startswith("!peenis"):
        await bot.close()
    if message.content.startswith("!"):
        await bot.process_commands(message)
        return
    noises = ["sqwak",
            "scree",
            "squak",
            "squek",
            "squack",
            "screk",
            "screech"]
    for members in message.mentions:
        if message.author.name != "shrub_bot" and members.name == "shrub_bot":
            await message.channel.send(message.content.replace("<@!" + str(bot.user.id) + ">", "").upper() + " " + random.choice(noises))
            break

try:
    bot.run(config['key'])
except Exception:
    pass

bot.close()

