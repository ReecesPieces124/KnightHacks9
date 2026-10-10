import discord


# WHAT FUNCTION SHOULD LOOK LIKE

# discord.Message should always be last parameter
async def example(num : int, word : str, message : discord.Message, client : discord.Client):
    await message.channel.send(f"number : {num}, word : {word}, bot : {client}")


# WHAT responses.py DECLARATION SHOULD LOOK LIKE

#   from addons._example import example
#   EXAMPLE = functools.partial(example, message=None, client=None,
#                                       num=10, word="hello")

# ////////////////////////////////////////////////////////////////////////////////////

# HELPFUL CODE
# await message.channel.send(f"")
# await random_user.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=random_num), reason="bad luck")
# all_users = message.channel.guild.members

# ////////////////////////////////////////////////////////////////////////////////////

# CODE FOR TARGETING
import re

async def target_code(message : discord.Message):

    # GET TARGET
    target : discord.Member = None
    match = re.search(r'<@(\d+)>', message.content.lower())
    if match:
        target = await message.channel.guild.fetch_member(match.group(1))

    # NO TARGET FOUND
    if not target:
        pass # CODE

    # TARGET IS SELF
    elif target.id == message.author.id:
        pass # CODE

    # TARGET IS BOT
    elif target.bot:
        pass # CODE

    #TARGET FOUND
    else:
        pass # CODE