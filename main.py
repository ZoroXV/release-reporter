# import releasereporter as rr

# def main():
#     rr.hello()

# if __name__ == "__main__":
#     main()

import os
import discord

intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.environ.get('DISCORD_TOKEN')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello, {message.author.nick}!')

client.run(TOKEN)
