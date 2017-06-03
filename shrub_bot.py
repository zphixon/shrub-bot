#!/usr/bin/env python3
#import yagmail
import traceback
import discord
from discord.ext import commands
import random
import asyncio
import datetime
import sys
import _thread
import time
from concurrent.futures import ProcessPoolExecutor

#yag = yagmail.SMTP('zack.zslash')

bot = commands.Bot(command_prefix='!')

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
@asyncio.coroutine
def test():
    """
    Verify shrub_bot is working.
    """
    yield from bot.say("hello!")

@bot.command()
@asyncio.coroutine
def parrot():
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
    yield from bot.say(random.choice(parrotURLs))

@bot.command()
@asyncio.coroutine
def shrub():
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
    yield from bot.say(random.choice(shrubURLs))

@bot.command()
@asyncio.coroutine
def roll(dice: str):
    """
    Roll some dice.
    """
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        yield from bot.say("Format must be NdN, e.g. 1d6")
        return
    result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
    yield from bot.say(result)

@bot.command()
@asyncio.coroutine
def choose(*choices: str):
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
    yield from bot.say("{} {}".format(random.choice(maybes), random.choice(choices)))

@bot.command()
@asyncio.coroutine
def birb():
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
    yield from bot.say("{}".format(random.choice(noises)))

@bot.command()
@asyncio.coroutine
def card():
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
    yield from bot.say("{}".format(random.choice(cards)))

@bot.command()
@asyncio.coroutine
def draw():
    """
    Draw a playing card
    """
    cards = [
            # aces
            "http://i.imgur.com/YoEexxn.png",
            "http://i.imgur.com/wVEvUvN.png",
            "http://i.imgur.com/MaNid5O.png",
            "http://i.imgur.com/HFv2fXi.png",
            # 2
            "http://i.imgur.com/3NpspDX.png",
            "http://i.imgur.com/JOjPCaq.png",
            "http://i.imgur.com/wBBiVMR.png",
            "http://i.imgur.com/1ji8NOS.png",
            # 3
            "http://i.imgur.com/aUaLoEv.png",
            "http://i.imgur.com/y6yjrO5.png",
            "http://i.imgur.com/wAFgz9c.png",
            "http://i.imgur.com/31A5OI0.png",
            # 4
            "http://i.imgur.com/Srdqkwk.png",
            "http://i.imgur.com/H5ngCWy.png",
            "http://i.imgur.com/728NsaQ.png",
            "http://i.imgur.com/u98A5cf.png",
            # 5
            "http://i.imgur.com/ntvq876.png",
            "http://i.imgur.com/mSc6nYc.png",
            "http://i.imgur.com/mga6Pwc.png",
            "http://i.imgur.com/uGctejO.png",
            # 6
            "http://i.imgur.com/fTEueBh.png",
            "http://i.imgur.com/geZkgpa.png",
            "http://i.imgur.com/R04qUaI.png",
            "http://i.imgur.com/EaGCX5z.png",
            # 7
            "http://i.imgur.com/BloHFfl.png",
            "http://i.imgur.com/qdKmt4R.png",
            "http://i.imgur.com/Io8HAVS.png",
            "http://i.imgur.com/Nfsr3Uy.png",
            # 8
            "http://i.imgur.com/RXBK5ZR.png",
            "http://i.imgur.com/9fQ4hfk.png",
            "http://i.imgur.com/nDvS4zI.png",
            "http://i.imgur.com/gAhkqTH.png",
            # 9
            "http://i.imgur.com/3v8xc80.png",
            "http://i.imgur.com/ShBTAiw.png",
            "http://i.imgur.com/6OWglP7.png",
            "http://i.imgur.com/j0ub25i.png",
            # 10
            "http://i.imgur.com/ngqZ7OY.png",
            "http://i.imgur.com/nPMfQm0.png",
            "http://i.imgur.com/DoJYRyR.png",
            "http://i.imgur.com/EbR78Wz.png",
            # jack
            "http://i.imgur.com/ACsM21c.png",
            "http://i.imgur.com/l0zeouz.png",
            "http://i.imgur.com/tHFcp75.png",
            "http://i.imgur.com/pq5hDJy.png",
            # queen
            "http://i.imgur.com/glOAmk1.png",
            "http://i.imgur.com/3LUosvb.png",
            "http://i.imgur.com/mn3BodI.png",
            "http://i.imgur.com/JFTJabr.png",
            # king
            "http://i.imgur.com/RebKlGi.png",
            "http://i.imgur.com/8Dqnrdi.png",
            "http://i.imgur.com/tzMj7G1.png",
            "http://i.imgur.com/OAr6Yk5.png",
            # jokers?
            ]
    yield from bot.say(random.choice(cards))

@bot.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith("!"):
        yield from bot.process_commands(message)
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
            yield from bot.send_message(message.channel, message.content.replace("<@" + str(bot.user.id) + ">", "").upper() + " " + random.choice(noises))
            break

#try:
bot.run("afdsadf@airmail.cc", "SHRUB_BOT2222")
#except Exception as e:
#    traceback.print_exc()
#    yag.send('zackh@firemail.cc', 'shrub_bot is down', 'shrub_bot has crashed.\n\n' + traceback.format_exc())

