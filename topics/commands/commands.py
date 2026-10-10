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

