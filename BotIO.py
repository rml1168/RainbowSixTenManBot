# Work with Python 3.6
from discord.ext.commands import Bot

TOKEN = 'NjM2NzA2NzA0OTkzNTUwMzM2.XbDiYg.hA69bZEhxZRxHiP7T78RdqSWaYs'

BOT_PREFIX = "!"
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)