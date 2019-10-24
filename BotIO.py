"""
file: BotIO.py
purpose: Handles IO from server text channels to bot and vice versa
author: rml1168@rit.edu (Ryan Lei)
author: jdesig8@aol.com (Jordan Disciglio)
"""
from discord.ext.commands import Bot

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