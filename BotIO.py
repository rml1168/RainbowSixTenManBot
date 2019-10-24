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
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    """
    What the bot will do when a message is received
    :param message: Represents a message from discord
    :return:
    """
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    """
    What the bot does on launch
    :return:
    """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)