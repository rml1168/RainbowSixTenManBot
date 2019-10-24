"""
file: BotIO.py
purpose: Handles IO from server text channels to bot and vice versa
author: rml1168@rit.edu (Ryan Lei)
author: jdesig8@aol.com (Jordan Disciglio)
"""
from discord.ext.commands import Bot
import random
import TabAPI

polling_for_interest = False
people_interested = list()
MAX_PEOPLE = 10

# Bot token
TOKEN = 'NjM2NzA2NzA0OTkzNTUwMzM2.XbDiYg.hA69bZEhxZRxHiP7T78RdqSWaYs'

# Bot prefix
BOT_PREFIX = "!"
bot = Bot(command_prefix=BOT_PREFIX)


@bot.command(name='register', description="Register yourself into the bot",
             brief="Register", aliases=['r'], pass_context=True)
async def register(context, arg):
    result = TabAPI.find_by_username(arg)
    if result == TabAPI.FAILURE:
        await bot.say("Invalid username. Try again.")
        return
    await bot.say(result)


@bot.command(name='interest', description="Poll for 10 man interest",
             brief="Polls for 10s", aliases=['i'], pass_context=True)
async def tens_interest():
    """
    Start polling interest for 10mans
    :return:
    """
    global polling_for_interest
    if polling_for_interest:
        await bot.say("Already polling for interest.")
    else:
        await bot.say("Polling for interest")
        polling_for_interest = True


@bot.command(name='not', description="Stop polling for 10 mans interest.",
             brief="Stop polling.", aliases=['n'], pass_context=True)
async def tens_not():
    """
    Turn polling flag false and clear the people_interested list
    :return:
    """
    global polling_for_interest
    if not polling_for_interest:
        await bot.say("We weren't polling in the first place.")
    else:
        await bot.say("Stopping polling...")
        global people_interested
        polling_for_interest = False
        people_interested.clear()


@bot.command(name='poll', description="Add yourself as interested.",
             brief="Interested?", aliases=['p'], pass_context=True)
async def tens_polling(context):
    """
    Start taking names for 10 mans interest
    If we reach max, ping everyone and tell them to get in the voice channel
    :return:
    """
    global polling_for_interest
    global people_interested
    if not polling_for_interest:
        await bot.say("Not currently polling for interest.")
        return
    elif context.message.author in people_interested:
        await bot.say("You are already queued.")
        return
    people_interested.append(context.message.author)
    await bot.say("Added! Amount of people currently waiting: " + str(len(people_interested)))
    if len(people_interested) == MAX_PEOPLE:
        polling_for_interest = False
        await bot.say("We have 10 people!")
        mention = "Get in here! "
        for user in people_interested:
            mention += user.mention + " "
        await bot.say(mention)


@bot.command(name='waiting', description="Display how many people are waiting.",
             brief="How many do we have?", aliases=['w'], pass_context=True)
async def waiting():
    people_waiting = len(people_interested)
    if people_waiting == 0:
        await bot.say("No one is currently waiting.")
    elif people_waiting == 1:
        await bot.say(str(people_waiting) + " person is currently waiting.")
    else:
        await bot.say(str(len(people_interested)) + " people are currently waiting.")


@bot.command(name='t', description="Create 2 random teams.",
             brief="2 teams", pass_context=True)
async def create_team(context):
    global people_interested
    a = random.randint(0, (len(people_interested) - 1))
    b = random.randint(0, (len(people_interested) - 1))
    print(people_interested - 1)
    while a == b:
        b = random.randint(0, (len(people_interested) - 1))
    captainA = people_interested[a]
    captainB = people_interested[b]
    await context.send("Team A Captain: " + str(captainA))
    await context.send("Team B Captain: " + str(captainB))
    await context.send("Incase you dont want Captains....")
    random.shuffle(people_interested)
    random.shuffle(people_interested)
    print("Team A is: " + str(people_interested[0:5]))
    await context.send("Team A is: " + str(people_interested[0:5]))
    print("Team B is: " + str(people_interested[5:10]))
    await context.send("Team B is: " + str(people_interested[5:10]))


@bot.event
async def on_ready():
    """
    What the bot does on launch
    :return:
    """
    print('Logged in as: ' + bot.user.name)
    print('Bot user ID: ' + bot.user.id)
    print('------')


bot.run(TOKEN)
