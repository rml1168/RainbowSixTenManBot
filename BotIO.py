"""
file: BotIO.py
purpose: Handles IO from server text channels to bot and vice versa
author: rml1168@rit.edu (Ryan Lei)
author: jdesig8@aol.com (Jordan Disciglio)
"""
from discord.ext.commands import Bot

polling_for_interest = False
people_interested = list()
MAX_PEOPLE = 10

# Bot token
TOKEN = 'NjM2NzA2NzA0OTkzNTUwMzM2.XbDiYg.hA69bZEhxZRxHiP7T78RdqSWaYs'

# Bot prefix
BOT_PREFIX = "!"
bot = Bot(command_prefix=BOT_PREFIX)


@bot.command(name='10interest', description="Poll for 10 man interest",
            brief="Polls for 10s", aliases=['10i'], pass_context=True)
async def tens_interest():
    """
    Start polling interest for 10mans
    :return:
    """
    await bot.say("Polling for interest")
    global polling_for_interest
    polling_for_interest = True


@bot.command(name='10not', description="Stop polling for 10 mans interest.",
             brief="Stop polling.", pass_context=True)
async def tens_not():
    """
    Turn polling flag false and clear the people_interested list
    :return:
    """
    await bot.say("Stopping polling...")
    global polling_for_interest
    global people_interested
    polling_for_interest = False
    people_interested.clear()


@bot.command(name='10poll', description="Add yourself as interested.",
             brief="Interested?", pass_context=True)
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
    people_interested.append(context.message.author)
    if len(people_interested) == MAX_PEOPLE:
        polling_for_interest = False
        await bot.say("We have 10 people!")
        mention = "Get in here! "
        for user in people_interested:
            mention += user.mention + " "
        await bot.say(mention)


@bot.event
async def on_ready():
    """
    What the bot does on launch
    :return:
    """
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


bot.run(TOKEN)
