import functools
from random import choice

import discord
import config
import responses
import sys

# ////////////////////////////////////////////////////////////////////////////////////

# SELECT RESPONSE
async def respond(message : discord.Message):
    for keywords in responses.responses:
        if any(x in str(message.content) for x in (keywords if isinstance(keywords, tuple) else (keywords,))):

            # CHECK IF TUPLE
            response = responses.responses.get(keywords)
            if type(response) == tuple:
                response = choice(response)

            # STRING
            if type(response) == str:
                await message.channel.send(f"{response}")

            # FILE
            elif type(response) == discord.File:
                await message.channel.send(file=response)

            # ADDON
            elif isinstance(response, functools.partial):
                kwargs = {}
                if 'message' in response.keywords:
                    kwargs['message'] = message
                if 'client' in response.keywords:
                    kwargs['client'] = client
                await response(**kwargs)

            return

# ////////////////////////////////////////////////////////////////////////////////////

# INITIALIZATION
intents : discord.Intents = discord.Intents.all()
client : discord.Client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready() -> None:
    await tree.sync()
    print(f'{client.user} is now online!')
    sys.stdout.flush()

# ////////////////////////////////////////////////////////////////////////////////////

# ON MESSAGE
@client.event
async def on_message(message: discord.Message) -> None:

    # IGNORE SELF
    if message.author == client.user:
        return

    # CASE SENSITIVE
    if not config.case_sensitive:
        message.content = message.content.lower()


    is_relevant : bool = any(x in message.content for x in responses.triggers) or config.no_trigger

    # PRINT INPUT
    if config.print_input and (config.print_unrelevant or is_relevant):
        username: str = str(message.author)
        user_message: str = message.content
        channel: str = str(message.channel)
        print(f'[{channel}] {username} : {user_message}')
        sys.stdout.flush()

    # FIND RESPONSE
    if is_relevant:
        await respond(message)


def main() -> None:
    client.run(token=config.TOKEN)

if __name__ == '__main__':
    main()

