import discord
import re
from enum import Enum
import random

# ////////////////////////////////////////////////////////////////////////////////////

# GET RANDOM USER
async def random_user(message : discord.Message):
    all_users = message.channel.guild.members
    random_user = random.choice(all_users)
    await message.channel.send(f"<@{random_user.id}>")

# ////////////////////////////////////////////////////////////////////////////////////

# RENAME

class RenameType(Enum):
    REPLACE = 0
    APPEND = 1
    PREPEND = 2

async def rename(message : discord.Message, text : str,
                 success : str, failure: str,
                 type : RenameType = RenameType.REPLACE):

    #CHECH IF TARGET IS OTHER USER
    target : discord.Member = message.author
    match = re.search(r'<@(\d+)>', message.content.lower())
    if match:
        target = await message.channel.guild.fetch_member(match.group(1))

    # CREATE NEW NAME STRING
    new_name = text
    if type == RenameType.APPEND:
        new_name =str(target.display_name) + text
    elif type == RenameType.PREPEND:
        new_name = text + str(target.display_name)

    # SET NEW NAME
    try:
        await target.edit(nick=str(new_name))
        if success:
            await message.channel.send(f"<@{target.id}> " + success)
    # NO PERMISSIONS
    except discord.Forbidden as e:
        await message.channel.send(f"No permissions :(")
    # NAME TOO LONG
    except:
        if failure:
            await message.channel.send(f"<@{target.id}> " + failure)


